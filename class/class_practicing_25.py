class MetaClass(type):
    def __new__(cls, name, bases, dct):
        cls.name = "bird"
        instance = super().__new__(cls, name, bases, dct)
        return instance

a = MetaClass('Animal', (), {'walk': True})
b = a()
print(a.walk)
print(b.walk)
print(a.name)  # the name was changed in line 3
print(a.__class__.__name__)  # MetaClass
print(b.__class__.__name__)  # Animal
# print(b.name)  # AttributeError: 'Animal' object has no attribute 'name'