__author__ = 'pavang'
__Date___ = ''


if __name__ == '__main__':
    L = [lambda x: x ** 2,            # Inline function definition
         lambda x: x ** 3,
         lambda x: x ** 4,
         lambda x: x ** 5,
         lambda x: x ** 6,]           # A list of three callable functions

    for f in L:
        print(f(2))                   # Prints 4, 8, 16 , 32 , 64

    print(L[0](3)) # Prints 9