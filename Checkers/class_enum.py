from enum import Enum


class Koko(Enum):
    RED = 1
    BLUE = 'black'

mem = Koko.BLUE

print(mem.name)

print(mem.value)



# print(Koko.RED)
#
# print(repr(Koko.BLUE))
#
# print(type(Koko.RED))
#
# print(isinstance(Koko.RED, Koko))
#
# print(Koko.RED.name)
#
# print(Koko.BLUE.value)
#
# print(Koko('black'))
#
# Koko(1)
#
# print('---')
#
# print(Koko(1))
# print('---')
#
# print(Koko['RED'])