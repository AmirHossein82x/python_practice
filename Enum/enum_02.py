from enum import Enum

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    RIGHT_ALIAS = 1

for name in Direction:
    print(name)

"""
out put: Direction.RIGHT, Direction.LEFT, Direction.UP, Direction.DOWN
"""
for name, item in Direction.__members__.items():
    print(name)

"""
out put: RIGHT, LEFT, UP, DOWN, RIGHT_ALIAS 
"""

for name, item in Direction.__members__.items():
    print(item)

"""
out put: Direction.RIGHT, Direction.LEFT, Direction.UP, Direction.DOWN
"""
