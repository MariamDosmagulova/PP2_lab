import datetime
import pygame #подключаем библ
pygame.init()#включаем пайгейм

screen = pygame.display.set_mode((1100,1100))
image = pygame.image.load('labs/lab7/m1.png')
minute = pygame.image.load('labs/lab7/minute.png')
seconds = pygame.image.load('labs/lab7/s1.png')

x1 = (1100-577)/2
y1 = (1100-433)/2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255,255,255))        
    screen.blit(image, (x1,y1))
    
    now = datetime.datetime.now()
    min = now.minute #возвр минуты
    sec = now.second #возвр сек
    min_angl = - min*6 #минус нужен тк transform.rotate() идет против часовой стрелки 
    sec_angl = - sec*6
    
    center = (550,550)
    
    rotated_min = pygame.transform.rotate(minute, min_angl)
    rotated_sec = pygame.transform.rotate(seconds, sec_angl)
    
    rect_min = rotated_min.get_rect(center = center)
    rect_sec = rotated_sec.get_rect( center = center)
    
    screen.blit(rotated_min, rect_min)
    screen.blit(rotated_sec, rect_sec)
    
    pygame.display.flip()
    
pygame.quit()

