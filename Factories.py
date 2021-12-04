from enum import Enum
from math import *

class CoordinateSystem(Enum):
    CARTESTIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'
        
    # def __init__(self, a, b, system=CoordinateSystem.CARTESTIAN):
        # if system == CoordinateSystem.CARTESTIAN:
        #     self.x = a
        #     self.y = b
        # elif system == CoordinateSystem.POLAR:
        #     self.x = a * cos(b)
        #     self.y = a * sin(b)

    @staticmethod
    def new_cartesian_point(self, x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(self, rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.new_polar_point(1, 2)
    print(p, p2)