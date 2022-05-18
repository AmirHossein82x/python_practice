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
#p = point(2, 3)
#print(p)
#print(p[1])

class rectangle:
    def __init__(self, corner, w, h):
        self.corner = corner
        self.width = w
        self.height = h
    def __str__(self):
        return "(%s, %d, %d)" %(self.corner, self.width, self.height)
    def grow(self, delta_width, delta_height):
        self.width +=delta_width
        self.height += delta_height
    def move(self, dx, dy):
        self.corner.x +=dx
        self.corner.y += dy
#box = rectangle(point(0, 0), 100, 200)
#bomb = rectangle(point(100, 80), 5, 10)
#print("box: ", box)
#print("bomb: ", bomb)
r = rectangle(point(10, 5), 100, 50)
print(r)
r.grow(25, -10)
print(r)
r.move(-10, 10)
print(r)
