class rectangle:
    def __init__(self, corner, w, h):
        self.corner = corner
        self.width = w
        self.height = h
    def __eq__(self, other):
        return(self.corner == other.corner and self.width == other.width and self.height == other.height)

p1 = rectangle(20, 2, 4)
p2 = rectangle(20, 2, 4)
print("p1 is p2: ", p1 is p2)
print("p1 == p2: ", p1 == p2)