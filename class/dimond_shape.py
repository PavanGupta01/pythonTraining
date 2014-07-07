__author__ = 'pavang'
__Date___ = ''


class first:
    def working(self):
        print("working first")

    def dummy(self):
        print("dummy first")

class second:
    def working(self):
        print("working second")

    def dummy(self):
        print("dummy second")

class third(first, second):
    def working(self):
        second.working(self)


if __name__ == '__main__':
    t = third()
    t.working()
    t.dummy()

    print(issubclass(second, first))
