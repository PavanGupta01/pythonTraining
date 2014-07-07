__author__ = 'pavang'
__Date___ = ''

def exception():
    try:
        raise IndexError
    except IndexError:
        print("got index error exception")

if __name__ == '__main__':
    exception()

