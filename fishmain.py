import pygame
import math
from nyvektor import *
from fish import *

pygame.init()
Fish.screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

fish= Fish(Vector(300,400),Vector(2,2),())


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Fish.upd()

    Fish.draw()

    Fish.screen.blit(Fish.img,(Fish.position.x,Fish.position.y))


    pygame.display.flip()
    clock.tick(60)
pygame.quit()
