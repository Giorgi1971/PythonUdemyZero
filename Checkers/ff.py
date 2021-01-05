from enum import Enum, auto


class Color(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()


list(Color)


print(list(Color))

print(Color(1))

print(Color.RED.name)
# [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]