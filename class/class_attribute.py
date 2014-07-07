__author__ = 'pavang'
__Date___ = ''

class Person:
    name = "Kabala"
    age = 697


class Student(Person):
    rollno = "Modi"

    # def print_att(self):
    #     print("__name__ :    " + str(self.__class__.__name__))


if __name__ == '__main__':
    s = Student()

    print('=' * 30 + '   subclass check   ' + '=' * 40)
    print("issubclass  :" + str(issubclass(Student, Person)))


    print('\n' + '=' * 30 + '  Obj belongs to Class   ' + '=' * 40)
    print("s belongs to :" + str(s.__class__))


    print('\n' + '=' * 30 + '   Attributes of Class   ' + '=' * 40)
    print("__name__ :    " + str(Student.__name__))
    print("__dict__ :    " + str(Student.__dict__))
    print("__bases__ :   " + str(Student.__bases__))

    # s.print_att()


    # print(list(name for name in dir(s) if not name.startswith('__')))