import math
class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = 2*radius
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter/2
        else:
            raise ValueError('Please provide either radius or diameter')

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

        # Example usage:
circ1 = Circle(radius=3)
circ2 = Circle(diameter=6)

print(circ1.area)  # Output: 28.274333882308138
print(circ2.radius)  # Output: 3.0
print(circ1 + circ2)  # Output: Circle(radius=6.0, diameter=12.0)
print(circ1 > circ2)  # Output: False
print(circ1 == circ2)  # Output: True
print(circ1 <= circ2)  # Output: True
print(circ1 >= circ2)  # Output: True

