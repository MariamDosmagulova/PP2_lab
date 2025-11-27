import pygame
from pygame.locals import *
import time
import random
import psycopg2
from psycopg2 import sql

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)


def get_db_connection():
    
    try:
        conn = psycopg2.connect(
            dbname="phonebook",      
            user="postgres",          
            password="Cici!4566",      
            host="localhost",         
            port="5432"              
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def init_database():
    """Инициализация базы данных и создание таблиц"""
    conn = get_db_connection()
    if conn is None:
        return
    
    cursor = conn.cursor()
    
    # Таблица пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            level INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Таблица результатов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_scores (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER,
            level INTEGER,
            saved_state TEXT,
            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    cursor.close()
    conn.close()
    print("The database is initialized")

def get_user(username):
    """Получить пользователя по имени"""
    conn = get_db_connection()
    if conn is None:
        return None
    
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def create_user(username):
    """Создать нового пользователя"""
    conn = get_db_connection()
    if conn is None:
        return False
    
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username) VALUES (%s)', (username,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except psycopg2.IntegrityError:
        cursor.close()
        conn.close()
        return False

def save_game_state(user_id, score, level, snake_data):
    """Сохранить текущее состояние игры"""
    conn = get_db_connection()
    if conn is None:
        return
    
    cursor = conn.cursor()
    
    # Сохраняем состояние змейки
    state_data = {
        'snake_x': snake_data.x,
        'snake_y': snake_data.y,
        'direction': snake_data.direction,
        'length': snake_data.length
    }
    
    cursor.execute('''
        INSERT INTO user_scores (user_id, score, level, saved_state)
        VALUES (%s, %s, %s, %s)
    ''', (user_id, score, level, str(state_data)))
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"The game is saved in PostgreSQL! Score: {score}, Level: {level}")

def get_last_saved_state(user_id):
    """Получить последнее сохраненное состояние"""
    conn = get_db_connection()
    if conn is None:
        return None
    
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM user_scores 
        WHERE user_id = %s 
        ORDER BY saved_at DESC 
        LIMIT 1
    ''', (user_id,))
    state = cursor.fetchone()
    cursor.close()
    conn.close()
    return state

def update_user_level(user_id, level):
    """Обновить уровень пользователя"""
    conn = get_db_connection()
    if conn is None:
        return
    
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET level = %s WHERE id = %s', (level, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def get_user_level(user_id):
    """Получить уровень пользователя"""
    conn = get_db_connection()
    if conn is None:
        return 1
    
    cursor = conn.cursor()
    cursor.execute('SELECT level FROM users WHERE id = %s', (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else 1

def get_username():
    """Функция для ввода имени пользователя"""
    pygame.init()
    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Enter Username")
    
    font = pygame.font.SysFont('arial', 24)
    input_box = pygame.Rect(100, 80, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return None
            if event.type == MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == KEYDOWN:
                if active:
                    if event.key == K_RETURN:
                        if text.strip():  # Проверяем, что имя не пустое
                            done = True
                    elif event.key == K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) < 15:  # Ограничение длины имени
                            text += event.unicode
        
        screen.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        
        instruction = font.render("Enter username and press Enter:", True, (255, 255, 255))
        screen.blit(instruction, (50, 30))
        
        pygame.display.flip()
    
    pygame.quit()
    return text.strip()


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.color = (255, 0, 0)
        self.x = 120
        self.y = 120
        self.weight = random.choice([1,2,3])
        self.update_color()
        self.lifetime = random.randint(3,7)
        self.spawn_time = time.time()

    def draw(self):
        pygame.draw.rect(self.parent_screen, self.color, (self.x, self.y, SIZE, SIZE))
    
    def update_color(self):
        if self.weight == 1:
            self.color = (255, 105, 97)       
        elif self.weight == 2:
            self.color = (255, 255, 204)    
        elif self.weight == 3:
            self.color = (119, 221, 119)      

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.color = (255, 105, 180)
        self.direction = 'down'
        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # Двигать голову
        if self.direction == 'left':
            self.x[0] -= SIZE
        elif self.direction == 'right':
            self.x[0] += SIZE
        elif self.direction == 'up':
            self.y[0] -= SIZE
        elif self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        for i in range(self.length):
            pygame.draw.rect(self.parent_screen, self.color, (self.x[i], self.y[i], SIZE, SIZE))

    def increase_length(self):
        self.length += 1
        self.x.append(self.x[-1])
        self.y.append(self.y[-1])

class Game:
    def __init__(self, username):
        pygame.init()
        pygame.display.set_caption("Snake Game with PostgreSQL")
        
        self.username = username
        self.user_id = self.get_or_create_user()
        self.level = get_user_level(self.user_id)
        self.score = 0
        
        
        self.levels = {
            1: {'speed': 10, 'walls': []},
            2: {'speed': 12, 'walls': self.create_walls_level2()},
            3: {'speed': 15, 'walls': self.create_walls_level3()},
            4: {'speed': 18, 'walls': self.create_walls_level4()},
            5: {'speed': 20, 'walls': self.create_walls_level5()}
        }
        
        self.surface = pygame.display.set_mode((600, 600))
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)
        self.clock = pygame.time.Clock()
        
        
        self.load_saved_state()

    def get_or_create_user(self):
        """Получить или создать пользователя"""
        user = get_user(self.username)
        if user:
            print(f"Welcome back, {self.username}! Your current level: {user[2]}")
            return user[0]  # user_id
        else:
            if create_user(self.username):
                user = get_user(self.username)
                print(f"A new user has been created: {self.username}")
                return user[0]
            return None

    def create_walls_level2(self):
        """Стены для уровня 2"""
        return [
            {'x': 200, 'y': 200, 'width': 200, 'height': 40},
            {'x': 200, 'y': 360, 'width': 200, 'height': 40}
        ]

    def create_walls_level3(self):
        """Стены для уровня 3"""
        walls = self.create_walls_level2()
        walls.extend([
            {'x': 100, 'y': 100, 'width': 40, 'height': 400},
            {'x': 460, 'y': 100, 'width': 40, 'height': 400}
        ])
        return walls

    def create_walls_level4(self):
        """Стены для уровня 4 - лабиринт"""
        return [
            {'x': 120, 'y': 120, 'width': 360, 'height': 40},
            {'x': 120, 'y': 440, 'width': 360, 'height': 40},
            {'x': 120, 'y': 160, 'width': 40, 'height': 240},
            {'x': 440, 'y': 160, 'width': 40, 'height': 240},
            {'x': 240, 'y': 240, 'width': 120, 'height': 40}
        ]

    def create_walls_level5(self):
        """Стены для уровня 5 - сложный лабиринт"""
        walls = self.create_walls_level4()
        walls.extend([
            {'x': 200, 'y': 320, 'width': 200, 'height': 40},
            {'x': 280, 'y': 160, 'width': 40, 'height': 120}
        ])
        return walls

    def draw_walls(self):
        """Отрисовка стен"""
        walls = self.levels[self.level]['walls']
        for wall in walls:
            pygame.draw.rect(self.surface, (100, 100, 100), 
                           (wall['x'], wall['y'], wall['width'], wall['height']))

    def check_wall_collision(self):
        """Проверка столкновения со стенами"""
        if self.level == 1:  # На уровне 1 нет стен
            return False
            
        walls = self.levels[self.level]['walls']
        snake_head_rect = pygame.Rect(self.snake.x[0], self.snake.y[0], SIZE, SIZE)
        
        for wall in walls:
            wall_rect = pygame.Rect(wall['x'], wall['y'], wall['width'], wall['height'])
            if snake_head_rect.colliderect(wall_rect):
                return True
        return False

    def load_saved_state(self):
        """Загрузить сохраненное состояние"""
        if self.user_id:
            saved_state = get_last_saved_state(self.user_id)
            if saved_state:
                print(f"Saved state found in PostgreSQL: Level {saved_state[3]}, Score: {saved_state[2]}")

    def save_current_state(self):
        """Сохранить текущее состояние игры"""
        if self.user_id:
            save_game_state(self.user_id, self.score, self.level, self.snake)

    def display_user_info(self):
        """Отобразить информацию о пользователе"""
        font = pygame.font.SysFont('arial', 25)
        user_text = font.render(f"User: {self.username}", True, (0, 0, 0))
        level_text = font.render(f"Level: {self.level}", True, (0, 0, 0))
        score_text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        db_text = font.render(f"DB: PostgreSQL", True, (0, 0, 0))
        
        self.surface.blit(user_text, (10, 10))
        self.surface.blit(level_text, (10, 40))
        self.surface.blit(score_text, (10, 70))
        self.surface.blit(db_text, (10, 100))

    def generate_food_position(self):
        while True:
            x = random.randint(0, (600 // SIZE) - 1) * SIZE
            y = random.randint(0, (600 // SIZE) - 1) * SIZE
            
            # Проверяем, чтобы яблоко не появлялось на стенах
            valid_position = True
            if self.level > 1:
                apple_rect = pygame.Rect(x, y, SIZE, SIZE)
                for wall in self.levels[self.level]['walls']:
                    wall_rect = pygame.Rect(wall['x'], wall['y'], wall['width'], wall['height'])
                    if apple_rect.colliderect(wall_rect):
                        valid_position = False
                        break
            
            if valid_position and (x, y) not in zip(self.snake.x, self.snake.y):
                return x, y

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)
        self.score = 0
        # Уровень не сбрасываем, сохраняем прогресс пользователя

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def render_background(self):
        self.surface.fill((173, 216, 230))

    def play(self):
        self.render_background()
        self.snake.walk()
        
        # Проверка границ экрана
        if self.snake.x[0] < 0 or self.snake.x[0] >= 600 or self.snake.y[0] < 0 or self.snake.y[0] >= 600:
            raise "Hit the wall"
        
        # Проверка столкновения со стенами
        if self.check_wall_collision():
            raise "Hit the wall"
        
        self.apple.draw()
        self.draw_walls()
        self.display_user_info()
        
        # Проверка таймера яблока
        now = time.time()
        if now - self.apple.spawn_time > self.apple.lifetime:
            self.apple.x, self.apple.y = self.generate_food_position()
            self.apple.weight = random.choice([1,2,3])
            self.apple.lifetime = random.randint(3,7)
            self.apple.spawn_time = time.time()
            self.apple.update_color()
        
        pygame.display.flip()
        
        # Змея ест яблоко
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            for _ in range(self.apple.weight):
                self.snake.increase_length()

            self.score += self.apple.weight

            self.apple.x, self.apple.y = self.generate_food_position()
            self.apple.weight = random.choice([1,2,3])
            self.apple.lifetime = random.randint(3,7)
            self.apple.spawn_time = time.time()
            self.apple.update_color()
            
            # Обновление уровня
            new_level = self.score // 10 + 1
            if new_level > self.level and new_level <= 5:
                self.level = new_level
                update_user_level(self.user_id, self.level)
                print(f"Congratulations! A new level: {self.level}")
        
        # Проверка столкновения с собой
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Occurred"

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 25)
        line1 = font.render(f"Game Over! User: {self.username}", True, (0, 0, 0))
        line2 = font.render(f"Final Score: {self.score} Level: {self.level}", True, (0, 0, 0))
        line3 = font.render("Press Enter to play again, Escape to exit", True, (0, 0, 0))
        line4 = font.render("Press P to save and pause during game", True, (0, 0, 0))
        line5 = font.render(f"Database: PostgreSQL", True, (0, 0, 0))
        
        self.surface.blit(line1, (100, 250))
        self.surface.blit(line2, (100, 290))
        self.surface.blit(line3, (100, 330))
        self.surface.blit(line4, (100, 370))
        self.surface.blit(line5, (100, 410))
        
        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if event.key == K_p:  # Сохранить и пауза
                        self.save_current_state()
                        pause = True
                        print("The game is on pause. The state is saved in PostgreSQL")

                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            # Скорость в зависимости от уровня
            current_speed = self.levels[self.level]['speed']
            self.clock.tick(current_speed)

if __name__ == '__main__':
    
    init_database()
    
    # Получаем имя пользователя
    username = get_username()
    if username:
        
        game = Game(username)
        game.run()