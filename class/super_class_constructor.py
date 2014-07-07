__author__ = 'pavang'
__Date___ = ''


class Super:
    def __init__(self, x):
     #...default code...
        self.x = x
        print(self.x)


class Sub(Super):
    def __init__(self, x, y):
        Super.__init__(self, x)                 # Run superclass __init__
        #...custom code...                      # Do my init actions
        self.y = y
        print(self.y)


if __name__ == '__main__':
    I = Sub(1, 2)

    
