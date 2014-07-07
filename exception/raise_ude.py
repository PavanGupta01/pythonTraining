__author__ = 'pavang'
__Date___ = ''

# ude(User Defined Exception)

class AlreadyGotOne(Exception):     # Inherited by builtin Exception class
    pass                            # User-defined exception

def grail():
    raise AlreadyGotOne()           # Raise an instance


if __name__ == '__main__':
    try:
        grail()
    except AlreadyGotOne:           # Catch class name
        print('got exception')