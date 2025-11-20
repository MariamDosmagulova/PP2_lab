import pygame
from pygame.locals import *
import time
import random

SIZE = 40

BACKGROUND_COLOR = (110, 110, 5)

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        
        self.color = (255, 0, 0)
        self.x = 120
        self.y = 120
        self.weight = random.choice([1,2,3])
        self.update_color()
        self.lifetime =random.randint(3,7)
        self.spawn_time = time.time()

    def draw(self):
        
        pygame.draw.rect(self.parent_screen, self.color, (self.x, self.y, SIZE, SIZE))
    
    def update_color(self):
        if self.weight == 1:
            self.color = (255, 105, 97)       # red
        elif self.weight == 2:
            self.color = (255, 255, 204)     # yellow
        elif self.weight == 3:
            self.color = (119, 221, 119)       # green    
        
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
    # Двигать тело начиная с хвоста: каждый сегмент занимает место предыдущего
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # Двигать только голову
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
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Codebasics Snake And Apple Game")

        self.level = 1
        self.speed = 0.25
        self.surface = pygame.display.set_mode((600, 600))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.score = 0
        
        self.clock = pygame.time.Clock()
        
    def generate_food_position(self):
        while True:
            x = random.randint(0, (600 // SIZE) - 1) * SIZE
            y = random.randint(0, (600 // SIZE) - 1) * SIZE
            if (x, y) not in zip(self.snake.x, self.snake.y):
                return x, y


    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)
        self.score = 0       
        self.level = 1

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
        if self.snake.x[0] < 0 or self.snake.x[0] >= 600 or self.snake.y[0] < 0 or self.snake.y[0] >= 600:
            raise "Hit the wall"
        self.apple.draw()
        # --- check apple timer ---
        now = time.time()
        if now - self.apple.spawn_time > self.apple.lifetime:
            # apple expired → generate a new one
            self.apple.x, self.apple.y = self.generate_food_position()
            self.apple.weight = random.choice([1,2,3])
            self.apple.lifetime = random.randint(3,7)
            self.apple.spawn_time = time.time()
            self.apple.update_color()
        self.display_score()
        
        
        pygame.display.flip()

        
        '''if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            
            self.snake.increase_length()
            self.score += 1'''
            
        # --- snake eats apple ---
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):

            # increase length based on weight
            for _ in range(self.apple.weight):
                self.snake.increase_length()

            # increase score based on weight
            self.score += self.apple.weight

            # generate new apple
            self.apple.x, self.apple.y = self.generate_food_position()
            self.apple.weight = random.choice([1,2,3])
            self.apple.lifetime = random.randint(3,7)
            self.apple.spawn_time = time.time()
            self.apple.update_color()
            
            
            
            if self.score // 15 + 1 > self.level:
                self.level += 1
                self.speed *= 0.9
        

        
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                
                raise "Collision Occurred"

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.score}", True, (0,0,0))
        self.surface.blit(score,(400,10))
        level = font.render(f"Level: {self.level}", True, (0,0,0))
        self.surface.blit(level, (400, 50))

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 25)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (100, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (100, 350))
        
        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        self.reset() 

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

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

            
            self.clock.tick(3 + self.level * 2)
            

if __name__ == '__main__':
    game = Game()
    game.run()