class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
p1 = point(2, 3)
p2 = point(2, 3)
print("p1 is p2: ", p1 is p2)
print("p1 == p2: ", p1 == p2)