__author__ = 'pavang'
__Date___ = ''

def changer(a, b):                  # Arguments assigned references to objects
    # b = b[:]                      # Copy input list so we don't impact caller
    a = 2                           # Changes local name's value only
    b[0] = 'spam'                   # Changes shared object in place

if __name__ =='__main__':
    X = 1
    L = [1,2]
    changer(X, L)
    # changer(X, L[:])               # Pass a copy, so our 'L' does not change
    # changer(X, tuple(L))           # Pass a tuple, so changes are errors
    print(X,L)