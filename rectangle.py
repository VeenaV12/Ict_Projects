#problem 10 /Base class
class Rectangle:
    def __init__(self, length, width):
        self.l = length
        self.b = width
        
    def perimeter(self):
        perimeter = 2*(self.l + self.b)
        return perimeter
        
    def area(self):
        area = self.l * self.b
        return area
        
    def display(self):
        print("Length and Width of rectangle:", self.l, self.b)
        print("Perimeter =", self.perimeter())
        print("Area =", self.area())
    
        
