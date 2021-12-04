from enum import Enum

class CoordinateSystem(Enum):
    CARTESTIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y