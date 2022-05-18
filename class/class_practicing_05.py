class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("point index out of range")
p1 = point(3, 4)
p2 = point(3, 4)
print("p1 is p2: ", p1 is p2)
print("p1 == p2: ", p1 == p2)
p3 = p1
print("p3 is p1: ", p3 is p1)
