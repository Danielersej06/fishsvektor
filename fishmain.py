import pygame
import math
from nyvektor import *
from fish import *
from flock import *

pygame.init()
screen = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()
running = True
flock = Flock(Fish.draw,10)

fish = Fish(Vector(200,300),Vector(1,1),screen)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Flock.f_upd()

    Flock.f_draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
