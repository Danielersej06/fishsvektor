from fish import *
import random
from nyvektor import *

class Flock:
    def __init__(self,screen, num_fish):
        self.fish_list = []  
        
        for _ in range(num_fish):
            fish = Fish(Vector(random.randint(0,800),random.randint(0,700)),Vector(random.randint(1,-1)),screen)  
            self.fish_list.append(fish) 
        
    def f_upd(self):
            for fish in self.fish_list:
                Fish.upd()

    def f_draw(self):
          for fish in self.fish_list:
               Fish.draw()

