from enum import Enum

class PolarDiraction(Enum):
    SOUTH = 'south'
    NORTH = 'north'
    WEST = 'west'
    EAST = 'east'
    A = 'south'

print(PolarDiraction)
print(PolarDiraction.EAST)  # --> PolarDiraction.EAST
print(PolarDiraction.EAST.name) # --> EAST
print(PolarDiraction.EAST.value) # --> east
print(PolarDiraction.EAST == PolarDiraction.NORTH) # --> False
print(PolarDiraction.SOUTH.name == PolarDiraction.A.name) # --> True
print(PolarDiraction.SOUTH == PolarDiraction.A) # --> True
print(PolarDiraction.SOUTH.value == PolarDiraction.A.value) # --> True
