from enum import Enum
from math import *

class CoordinateSystem(Enum):
    CARTESTIAN = 1
    POLAR = 2


class Point:
    def __init__(self, a, b, system=CoordinateSystem.CARTESTIAN):
        if system == CoordinateSystem.CARTESTIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * cos(b)
            self.y = a * sin(b)

    @staticmethod
    def new_cartesian_point(self, x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(self, rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))