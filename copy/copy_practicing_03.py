import copy
class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)
class rectangle:
    def __init__(self, corner, w, h):
        self.corner = corner
        self.width = w
        self.height = h
    def __str__(self):
        return "(%s, %d, %d)" %(self.corner, self.width, self.height)
    def __eq__(self, other):
        return (self.corner == other.corner and self.width == other.width and self.height == other.height)
p1 = rectangle(point(2, 4), 5, 6)
p2 = copy.copy(p1)
p1.corner.x = 100
print("p1: ", p1)
print("p2: ", p2)
print("p1 is p2: ", p1 is p2)
print("p1 == p2: ", p1 == p2)
print("----------------------")
p2 = copy.deepcopy(p1)
p1.height = 89
print("p1: ", p1)
print("p2: ", p2)
print("p1 is p2: ", p1 is p2)
print("p1 == p2: ", p1 == p2)
