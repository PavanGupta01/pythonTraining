__author__ = 'pavang'
__Date___ = ''

def func(x, y, z):
    return x + y + z

f = lambda x, y, z: x + y + z

# Defaults work on lambda arguments, just like in a def:
x = (lambda a="Hello ", b="Mr ", c=" ": a + b + c)

# Nested lambda function
action = (lambda x: (lambda y: x + y))

if __name__ == '__main__':

    print(func(1,5,9))
    print(f(1,5,9))
    # print(x(1,5,9))
    print(action(1)(3))             # Calling Nested lambda function
