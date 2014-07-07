__author__ = 'pavang'
__Date___ = ''

from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    @abstractmethod
    def abs_method(self):
        print("Super....")
        pass

class Sub(Super):

    def abs_method(self):
        print("Sub....")
        pass

    def action(self):
        print('spam')

if __name__ == '__main__':
    # x = Super()

    y = Sub()
    y.abs_method()
