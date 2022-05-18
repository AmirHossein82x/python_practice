page = "hello students"
print(f"{page=}")
print("--------------------")

result = (a:=11 *2) + (b:=27/9)
print(f"{result = }")
print(f"{a = }, {b = }")
print("--------------------")

def hello(a, b):
    return a * b , a + b
zarb, jam = hello(10, 2)
print(f"{zarb=}, {jam=}")
print("--------------------")

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%d, %d)" %(self.x, self.y)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Dot(x, y)
z1 = Dot(1, 2)
z2 = Dot(3, 4)
print(z1 + z2)
print("--------------------")
