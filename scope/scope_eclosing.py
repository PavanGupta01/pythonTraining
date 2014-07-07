__author__ = 'pavang'
__Date___ = ''

X = 10                                       # Global scope name: not used
def f1():
    # global X
    # X = 20                                   # Enclosing def local
    def f2():
        nonlocal X
        # global X
        X = 30
        print('f2: ' + str(X))                             # Reference made in
        # nested def
    f2()
    print('f1: ' + str(X))

if __name__ == '__main__':
    f1()                                     # Prints 88: enclosing def local
    print('G : ' + str(X))
