from enum import Enum

class Shape(Enum):
    RECTANGLE = 'rec'
    TRIANGLE = 'tri'
    CIRCLE = 'cir'

print(Shape.RECTANGLE.value == 'rec') # --> True
print(Shape.RECTANGLE.value is 'rec') # --> True
