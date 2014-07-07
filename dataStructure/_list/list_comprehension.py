__author__ = 'pavang'
__Date___ = ''




def demo_list():
    lst = [' Bollywood ',' Hollywood ', 'Tollywood', 'Ro', 'Robinhood  ']
    print([item.strip() for item in lst])


def w_comprehension():
    lst = []
    f = open('/tmp/c2cprop.txt')
    lines = f.readlines()
    for line in lines :
        lst.append(line.rstrip())
    return lst


def con_chars():
    res = []
    for x in 'abc':
        for y in 'lmn':
            res.append(x + y)
    return res

if __name__ == '__main__':
    demo_list()

    # lines = w_comprehension()

    # lines = [line.rstrip() for line in open('/tmp/c2cprop.txt')]
    # lines = [line.rstrip() for line in open('/tmp/c2cprop.txt') if line[0] == 'p']

    # print(lines)


    # concatenation of x + y for every x in one string and every y in another.It
    # effectively collects all the ordered combinations of the characters in two
    # strings:

    # lst = [x + y for x in 'abc' for y in 'lmn']
    # print(lst)

