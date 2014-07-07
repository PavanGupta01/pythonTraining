__author__ = 'pavang'
__Date___ = ''

import module1
# from module1 import printer
# from module1 import *


# print(module1.var)
module1.printer("Only Import")

print(module1.var)
# printer("From statement")

print('=' * 30 + '   module1 dir   ' + '=' * 40)

#print(dir(module1))

#includes inherited names for classes
# print(module1.__dict__)


# Another way of modifying attributes
module1.__dict__['var'] = 50
print(module1.var)