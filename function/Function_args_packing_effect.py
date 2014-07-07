__author__ = 'pavang'
__Date___ = ''


def echo(*pargs, **kargs):

    # pargs.append(98)
    # kargs["new"] = "Added"
    # kargs["new2"] = "Added"

    print(pargs)


def without_keyword(*pargs):
    print(pargs)

if __name__ == '__  main__':
    pargs = (1, 2)
    pargs_list = [41, 42, 43, 44]
    kargs = {'a' : 3, 'b' : 4}

  # Unpacking
    echo(*(1, 2),  **{'c':42, 'd': 98})

    # packing
    # echo(pargs,kargs)


    # without_keyword(2,3,4, d = 90)
