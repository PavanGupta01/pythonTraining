__author__ = 'pavang'
__Date___ = ''


x = 10
class dummy:
    x = 20
    y = 90
    def method(self):
        print(x)

        # print(y)
        print(self.y)




if __name__ == '__main__':
    obj = dummy()
    obj.method()

    # print(obj.y)
