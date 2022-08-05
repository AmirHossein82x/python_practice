class MetaClass(type):
    def __new__(cls, name, bases, dct):
        bases += (A, B)
        instance = super().__new__(cls, name, bases, dct)
        return instance

class A:
    def walk(self):
        return 'I can walk'

class B:
    def swim(self):
        return 'I can swim'

class Animal(metaclass=MetaClass):
    pass
animal = Animal()
print(animal.walk())
print(animal.swim())