import pygame

pygame.init()
clock = pygame.time.Clock()

s = pygame.display.set_mode((800,700))
l = pygame.image.load('labs/lab7/images/lizo.png')
ss = pygame.image.load('labs/lab7/images/ss.png')

x=25
y=25
r = 25
color = (255,0,0)
speed = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_UP] and y - r >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + r  <= 700:
        y += speed
    if keys[pygame.K_LEFT] and x - r >= 0:
        x -= speed  
    if keys[pygame.K_RIGHT] and x + r  <= 789:
        x += speed     
                         
    s.fill((10,50,40))
    s.blit(l,(325,390))
    s.blit(ss, (200,220))
    
    pygame.draw.circle(s, color,(x,y),r)
    clock.tick(60)
    pygame.display.flip()
    
pygame.quit()
    