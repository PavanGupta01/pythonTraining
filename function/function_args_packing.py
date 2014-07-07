__author__ = 'pavang'
__Date___ = ''

def f_positional(a, b, c):
    print(a, b, c)

def f_keyword(c=3, b=2, a=1):
    print(a, b, c)

def positional_key(a,b = 2, c =3):
    print(a,b,c)

def f_arbitrary_tuple(*args):
    """
    Headers: Collecting arguments
    :param args:
    :type args:
    :return:
    :rtype:
    """
    print(args)

def f_arbitrary_dict(**args):
    print(args)


def echo(*pargs, **kargs):

    kargs["new"] = "Added"
    print(pargs, kargs)

def f_arbitrary_tuple_dict(a, *pargs, **kargs):
    print(a, pargs, kargs)

def kwonly(a, *b, c):
    """
    available only in 3.X
    """
    print(a, b, c)


if __name__ == '__main__':
    #
    # print("Positional Argument")
    # f_positional(10,20,30)
    #
    # print("\nKeyword Argument")
    # f_keyword()
    # f_keyword(72,9,36)
    #
    # print("\nPositional and Keyword args together")
    # positional_key(40)
    # positional_key(50,60)
    # positional_key(40,50,60)

    # print("\nArbitrary touple")
    # f_arbitrary_tuple()
    # f_arbitrary_tuple(5,6,7,8,13)

    # print("\nArbitrary Dict")
    # f_arbitrary_dict()
    # f_arbitrary_dict(a = 1, b = 2)

    pargs = (1, 2)
    kargs = {'a' : 3, 'b' : 4}

    print("\nTuple   --   Dict ")
    # echo()
    echo(pargs,kargs)
    # echo(1, 2,67,7,667,56,57,57, a = 3, b = 4)
    #
    # print("\nPositional -- Tuple   --   Dict ")
    # f_arbitrary_tuple_dict(2)
    # f_arbitrary_tuple_dict(1, 2, 3, x=1, y=2)
    #
    print("\nKeyword Only, In 3.X ")
    kwonly(1, 2, 10, 58, c = 3)
    kwonly(a = 1, c = 3)
    kwonly(1, 2, 3)                     # TypeError:


    print(kargs)