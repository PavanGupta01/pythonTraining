__author__ = 'pavang'
__Date___ = ''

import module1
module1.printer("Python")



module1.printer = "Hello"
print(module1.printer)

# print(module1.__dict__)

var = "var of init"


# accessing local and module attribute
print(var)
print(module1.var)