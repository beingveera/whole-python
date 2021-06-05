from enum import Enum
class color(Enum):
	red=1
	blue=2
	green=3
	pink=4
print(color.red)
print(color(2))
print(color['red'])
print([i for i in color])