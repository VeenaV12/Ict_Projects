#problem 10 /Child class
from rectangle import *
   
class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.h = height
        
    def volume(self):
        volume = self.l*self.b*self.h
        print("Volume =", volume)
    

r = Rectangle(5, 6)
r.display()

r1 = Parallelepiped(2, 3, 4)
r1.display()
r1.volume()
