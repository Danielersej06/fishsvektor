import math
import pygame

class Fish:
    def __init__ (self,position,velocity,screen):
        self.position = position
        self.velocity = velocity
        self.screen = screen
        self.img = pygame.image.load('fish.png')
        self.img = pygame.transform.scale(self.img, (200,200))
    
    def upd(self):
        self.screenconfinement
        self.position += self.position + self.velocity
    
    def draw (self):
        self.screen.blit(self.img, (self.position.x,self.position.y))
    
    def screenconfinement(self):
        velocity = self.velocity
        if self.position.x <= 0 or self.position.x >= 800 - 200:
            velocity.x = -velocity.x
        
        if self.position.y <= 0 or self.position.y >= 600- 200:
            velocity.y = -velocity.y
        print(self.velocity)
        return (velocity)

