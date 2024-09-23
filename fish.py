import math
import pygame

class Fish:
    def __init__ (self,position,velocity,img,screen):
        self.position = position
        self.velocity = velocity
        self.img = img
        self.screen = screen
    
    def upd (self,position,velocity):
        self.position += self.velocity
    
    def draw (self, position):
        self.screen.blit(self.img, (self.position.x,position.y))
    
    def screenconfinement(self):
        velocity = self.velocity
        if self.position.x <= 0 or self.position.x >= 800 - 200:
            velocity.x = -velocity.x
        if self.position.y <= 0 or self.position.y >= 600- 200:
            velocity.y = -velocity.y
        return velocity

