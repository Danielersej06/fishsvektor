from fish import *
import random


class Flock:
     def __init__(self, img, num_fish):
        self.fish_list = []  

        for _ in range(num_fish):
 
            x = random.randint(0, 800)
            y = random.randint(0, 600)
            fish = Fish(img, x, y)  
            self.fish_list.append(fish) 
        
     def f_upd(self):
            for fish in self.fish_list:
                Fish.upd()

     def f_draw(self):
          for fish in self.fish_list:
               Fish.draw()

