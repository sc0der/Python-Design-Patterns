from enum import Enum

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