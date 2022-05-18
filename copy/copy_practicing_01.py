import copy
class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
p1 = point(3, 4)
# shallow copy
p2 = copy.copy(p1)
print("p1 is p2: ", p1 is p2)
print("p1 == p2: ", p1 == p2)