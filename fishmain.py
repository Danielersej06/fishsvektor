import pygame
import math
from vektor import *
from fish import *

pygame.init()
Fish.screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

Fish.img = pygame.image.load('fish.png')
Fish.img = pygame.transform.scale(Fish.img, (200,200))
Fish.position = Vector(400,300)

Fish.velocity = Vector(2,2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Fish.upd

    Fish.draw

    Fish.screen.blit(Fish.img,(Fish.position.x,Fish.position.y))

    Fish.position = (Fish.position.add(Fish.velocity))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
