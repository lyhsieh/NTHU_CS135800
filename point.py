import math

class Point:
    count = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.serial = Point.count
        Point.count += 1

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def r(self):
        return math.sqrt(self.x**2 + self.y**2)

    @property
    def theta(self):
        return math.atan(self.y / self.x) * 180 / math.pi

    radius = r
    
    @property
    def area_of_circle(self):
        return math.pi * self.r() ** 2

    @property
    def area_of_rectangle(self):
        return self.x * self.y

