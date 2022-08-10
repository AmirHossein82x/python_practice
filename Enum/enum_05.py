from enum import Enum, auto

class Direction(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    RIGHT =  auto()
    LEFT = auto()
    UP = auto()
    DOWN = auto()

for name, item in Direction.__members__.items():
    print(f'name: {name}, item.name: {item.name}, item.value: {item.value}')