__author__ = 'pavang'
__Date___ = ''


x = 'spam'

def fetcher(obj, index):
    return obj[index]

def catcher():
    try:
        fetcher(x, 4)
    except IndexError:
        print('got exception')
        print('continuing')



if __name__ == '__main__':

    # print(fetcher(x,3))
    # print(fetcher(x,4))
                # OR
    # try:
    #     print(fetcher(x,4))
    # except IndexError:
    #     print("got Index Error")

                # OR
    # catcher()