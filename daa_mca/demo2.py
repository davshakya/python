from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass  # Abstract method has no implementation here

    @abstractmethod
    def perimeter(self):
        pass


# Derived class implementing abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Another derived class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.1416 * self.radius


# Usage
# shape = Shape()  # This will raise an error: Can't instantiate abstract class

rect = Rectangle(5, 3)
print("Rectangle area:", rect.area())           # Rectangle area: 15
print("Rectangle perimeter:", rect.perimeter()) # Rectangle perimeter: 16

circle = Circle(4)
print("Circle area:", circle.area())             # Circle area: 50.2656
print("Circle perimeter:", circle.perimeter())   # Circle perimeter: 25.1328
