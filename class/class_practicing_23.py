# class Animal:
#     def __init__(self):
#         pass

#     def walk(self):
#         return 'the bird cant walk'

"""
we can implement a class in one line in dynamic programing
"""
A = type('Animal', (), {"walk": lambda x: 'Animals can walk', 'name': 'animal'})
a = A()
# print(A.walk())  TypeError: <lambda>() missing 1 required positional argument: 'x'
print(a.walk())
print(A.__name__)  # Animal
print(A.__dict__)
print(dir(A))

B = type('bird', (A,), {'fly': "the bird can fly"})

b = B()
print(b.fly)
print(b.walk())
print(a.name)
print(b.name)