class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx**2 + dy**2) ** 0.5
p = Point(2, 6)
q = Point(-1, 4)
print(p.distance(q))