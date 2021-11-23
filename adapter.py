class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw_point(self):
        print(".", end="")


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
