class A:
    def __new__(cls, a, b):
        print('creating instance 1')
        self = super().__new__(cls)
        self.properties = {a, b}
        self.name = 'amir hossein'
        return self

    def __init__(self, a, b):
        print('creating instance 2')
        self.a = a
        self.b = b

a = A(12, 3)
print(a.a)
print(a.name)
print(a.properties)