class Point:    
    def __init__(self, x, y):  
        self._x = x
        self._y = y
    def __repr__(self):
        return __class__.__name__ + repr((self._x, self._y))
    
class ColorPoint(Point):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self._color = color
    def __repr__(self):
        return __class__.__name__ + repr((self._x, self._y, self._color))
