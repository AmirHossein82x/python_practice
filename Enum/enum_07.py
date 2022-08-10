from enum import Enum, IntEnum

class Color(IntEnum):
    RED = '1'
    BLUE = '2'
    YELLOW = '3'
    ALIAS_RED = '1'
    # A = 'hello'   ValueError: invalid literal for int() with base 10: 'hello'

class Direction(IntEnum):
    RIGHT = 1
    DOWN = 2
    UP = 3
    ALIAS_RIGHT = 1
    
print(Color.RED.value == 1) # True
print(Color.RED.value == Direction.RIGHT.value) # True
print(Direction.RIGHT.value == 1) # True
print(Direction.RIGHT.value == Direction.ALIAS_RIGHT.value) # True