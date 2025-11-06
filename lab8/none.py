import pygame, sys 
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

font = pygame.font.SysFont("Verdana", 60)#загружает шрифт из системных файлов ос
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("PygameTutorial_3_0\AnimatedStreet.png")

DISPALAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPALAYSURF.fill(WHITE)
pygame.display.set_caption("Game")  #заголовог окна 

class Enemy(pygame.sprite.Sprite): # спрайт это класс, который является объектом в игреб он является родителем для всех объектов и позволяет управлять ими как единым целым
    def __init__(self): #init это спец функц, которая автомат вызывается при создании нового врага
        super().__init__() # супер - это функц род класса, которая сначала инициализирует все атрибуты род класса, а потом добавляет атрибуты уже дочернего класса
        self.image = pygame.image.load("PygameTutorial_3_0\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40 ), 0)#устанавливаем начальную позицию врага, по ширине (от 40 до 360), а высота 0
        
    def move(self): 
        global SCORE# глобал - переменная объявлена снаружи этой функции
        self.rect.move_ip(0,SPEED) #move_ip переместить на месте. по х на 0(те не двиггаем по ширине), по у перемес со скоростью спид
        if (self.rect.top>600): #если верхняя граница варага ушла ниже 600
            SCORE+=1
            self.rect.top = 0 #возвращаем врага в начало 
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("PygameTutorial_3_0\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left>0: 
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right<SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)
        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
        #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("PygameTutorial_3_0\Coin.png")
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    def move(self):
        self.rect.move_ip(0, SPEED)
        
        if self.rect.top>600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
#Setting up Sprites  
P1= Player()
E1= Enemy()
C1= Coin()
#Creating Sprites Groups
enemies= pygame.sprite.Group()#чтобы удобно управлять всеми врагами сразу
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1 #USEREVENT - это спец число, которое пайгейм зарезервировал для моих собственных событий, а +1 означает что это первое событие 
pygame.time.set_timer(INC_SPEED,1000)#сет таймер функц таймера, которая вызывает событие увел. скорости по таймеру с интервалом 1 с или 1000 мс

while True:
    
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED+=0,5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    DISPALAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coins_text = font_small.render("Coins: " + str(COINS), True, BLACK)
    
    DISPALAYSURF.blit(scores, (10,10))
    DISPALAYSURF.blit(coins_text, (300,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPALAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('PygameTutorial_3_0\crash.wav').play()
          time.sleep(0.5)
                    
          DISPALAYSURF.fill(RED)
          DISPALAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()    
              
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1
        
        for coin in coins:
            coin.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) 
               
    pygame.display.update()
    FramePerSec.tick(FPS)

