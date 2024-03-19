import pygame 
import time
import datetime
import math

pygame.init()
SIZE = WIDTH ,HEIGHT = 1000,1000
midle = WIDTH//2 , HEIGHT//2
RADIUS = 1000

screen = pygame.display.set_mode((SIZE))
clock = pygame.time.Clock()


sec = pygame.image.load("images/leftarm.png").convert_alpha()
minute = pygame.image.load("images/rightarm.png").convert_alpha()
rectsec = sec.get_rect()
rectmin = minute.get_rect()
rectmin.center = rectsec.center = midle

background = pygame.image.load("images/mainclock.png")
run =True

angle1 = 0
angle2 = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #system time
    time = datetime.datetime.now()
    minuteTime = time.minute
    secondTime = time.second

    #minute
    angle1 = -minuteTime*6 #6 is degree
    leg1 = pygame.transform.rotate(minute, angle1)
    rect1 = leg1.get_rect()
    rect1.center = rectmin.center

    #second
    angle2 = -secondTime*6 #6 is degree
    leg2 = pygame.transform.rotate(sec, angle2)
    rect2 = leg2.get_rect()
    rect2.center = rectsec.center

    #output
    screen.blit(background, (-200, -20))
    screen.blit(leg1, rect1)
    screen.blit(leg2, rect2)
    

    #screen.blit(background, (0, 0))
    #pg.draw.circle(screen, (0, 0, 0), (500, 500), 490, 5)
    pygame.display.flip()
    clock.tick(60)