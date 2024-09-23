import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def sub(self,other):
        return Vector(self.x-other.x,self.y-other.y)

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def dot(self,other):
        return self.x*other.x+self.y*other.y
    
    def length(self):
        return math.sqrt(self.x*self.x+self.y*self.y)

    def scale(self,k):
        return Vector(self.x*k,self.y*k)
    
    def eq(selv,other):
        if v1==v2:
            return True
        else:
            return False


        


v1 = Vector(3,4)
v2 = Vector(3,4)
k = 5


print("add", (v1.add(v2)))
print("sub", (v1.sub(v2)))
print("dot", (v1.dot(v2)))
print("length",v1.length())
print("scale",(v1.scale(k)))
print("equal",(v1.eq(v2)))

