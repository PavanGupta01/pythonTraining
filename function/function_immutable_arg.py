__author__ = 'pavang'
__Date___ = ''

def f(a):           # a is assigned to (references) the passed object
    a = 99          # Changes local variable a only

    # print(a is b)

if __name__ =='__main__':
    b = 80
    f(b)
