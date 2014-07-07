__author__ = 'pavang'
__Date___ = ''

from mutable import x, y              # Copy two names out
x = 42
y[0] = 42

import mutable
print(mutable.x)
print(mutable.y)


print('*' * 100)

mutable.x = 42                        # Changes x in other module
import mutable
print(mutable.x)
print(mutable.y)

# print(mutable.__dict__)
