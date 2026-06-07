import pygame
pygame.init()
screen=pygame.display.set_mode((500,400))
running=False
while not running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=True
    pygame.draw.rect(screen,(0,125,255),pygame.Rect(175,175,100,80))
    pygame.display.flip()