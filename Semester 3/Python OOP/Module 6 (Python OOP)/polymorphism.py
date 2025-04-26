#Polymorphism means many forms
#here area() method work as polymorphism since it has different structure but same name
from math import pi
class Shape:
    def __init__(self, name) -> None:
        self.name = name
    
class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, name, radius) -> None:
        self.radius = radius
        super().__init__(name)

    def area(self):
        return pi * self.radius*self.radius
    
rectangle = Rectangle('Rect',50,15)
print(rectangle.area())
circle = Circle('Circle',2)
print(circle.area())