import math
import pygame
from flock import *

class Fish:
    def __init__ (self,position,velocity,screen):
        self.position = position
        self.velocity = velocity
        self.screen = screen
        self.img = pygame.image.load('fish.png')
        self.img = pygame.transform.scale(self.img, (100,100))
    
    def upd(self):
        self.position += self.velocity
        Fish.screenconfinement(self)
        
    
    def draw (self):
            self.screen.fill((0,0,0))
            self.screen.blit(self.img, (self.position.x,self.position.y))

    def screenconfinement(self):
        velocity = self.velocity
        if self.position.x <= 0 or self.position.x >= 700:
             velocity.x = -velocity.x


        if self.position.y <= 0 or self.position.y >= 600:
            velocity.y = -velocity.y

