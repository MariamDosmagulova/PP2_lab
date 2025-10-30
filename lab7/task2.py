import pygame
pygame.init()
pygame.mixer.init()

s = pygame.display.set_mode((600,600))
i1 = pygame.image.load('labs/lab7/images/1.png')
i2 = pygame.image.load('labs/lab7/images/2.png')
i3 = pygame.image.load('labs/lab7/images/3.png')
i4 = pygame.image.load('labs/lab7/images/4.png')


x=(600-91)//2
y=(600-87)//2

songs = [
    'labs/lab7/music/t.mp3',
    'labs/lab7/music/m.mp3',
    'labs/lab7/music/p.mp3',
    'labs/lab7/music/k.mp3'
]
current = 0

def play_song():
    pygame.mixer.music.load(songs[current])
    pygame.mixer.music.play()

is_playing = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                if is_playing:
                    pygame.mixer.music.pause()
                    is_playing = False
                else:
                    pygame.mixer.music.unpause()
                    if not pygame.mixer.music.get_busy():
                        play_song()
                    is_playing=True
            elif event.key == pygame.K_RIGHT:
                current = (current+1)%len(songs)
                play_song()
                is_playing=True
            elif event.key == pygame.K_LEFT:
                current = (current -1)%len(songs)
                play_song()
                is_playing=True
    s.fill((255,255,255))
    
    s.blit(i2, (x-125,y))
    s.blit(i3, (x+125,y))
    
    if is_playing:
        s.blit(i4,(x,y))
    else:
        s.blit(i1, (x,y))
    

        
    
    pygame.display.flip()
    
pygame.quit()   