class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Adam(Human):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

class Eve(Adam, Human):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)


a = Eve('ali',12, 14)
print(a.name)
print(a.color)
print(a.age)
