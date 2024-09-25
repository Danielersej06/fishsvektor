import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __dot__(self,other):
        return self.x*other.x+self.y*other.y
    
    def __length__(self):
        return math.sqrt(self.x*self.x+self.y*self.y)

    def __scale__(self,k):
        return Vector(self.x*k,self.y*k)
    
    def __eq__(self,other):
        if v1==v2:
            return True
        else:
            return False


v1 = Vector(3,4)
v2 = Vector(3,4)

