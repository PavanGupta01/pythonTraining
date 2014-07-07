__author__ = 'pavang'
__Date___ = ''


def func(a, b, c, d):
    print(a, b, c, d)

if __name__ == '__main__':
    print("Args unpacking using tuple")
    # args = (5,10,15,20)
    # args = [2,3,8,5]
    # func(*args)

    print("\nArgs unpacking using dictionary")
    args = {'a' : 1, 'b' : 2, 'c' : 3,  'd' : 4}
    func(**args)

    pargs = (1, 2)
    kargs = {'a' : 3, 'b' : 4}

    func(*(1, 2), **{'d' : 4, 'c' : 3})         # Same as func(1, 2, d=4, c=3)