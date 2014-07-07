__author__ = 'pavang'
__Date___ = ''

x = 'spam'

def fetcher(obj, index):
    return obj[index]

def after() :
    try :
        fetcher(x, 3)
    finally :
        print('after fetch')
    print('after try?')

if __name__ == '__main__':
    after()