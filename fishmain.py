import pygame
import math
from nyvektor import *
from fish import *

pygame.init()
screen = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()
running = True

fish = Fish(Vector(200,300),Vector(2,2),screen)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fish.upd()

    fish.draw()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
