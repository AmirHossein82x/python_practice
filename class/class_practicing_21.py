class Part:
    new = 0
    def __init__(self):
        self.house = [1, 2, 3, 4]
        Part.new += 1
    @classmethod
    def add(cls):
        print(cls.new)


a = Part()
b = Part()
a.add()