__author__ = 'pavang'
__Date___ = ''

class MixedNames:                           # Define class
    data = 'spam'                           # Assign class attr

    def __init__(self, value):              # Assign method name
        self.data = value                   # Assign instance attr

    def display(self):
        print(self.data, MixedNames.data)     # Instance attr, class attr

    def method_with_args(self, text):
        self.text = text
        print(self.text)


if __name__ == '__main__':
    x = MixedNames(1)                   # Make two instance objects
    y = MixedNames(2)                   # Each has its own data

    x.display()
    y.display()             # self.data differs, MixedNames.data is the same


    print('=' * 30 + '   Calling method via class   ' + '=' * 40)
    MixedNames.display(x)
    MixedNames.display(y)

    print('=' * 30 + '   Calling method via class with args   ' + '=' * 40)
    MixedNames.method_with_args(x, "Via x")
    MixedNames.method_with_args(y, "Via y")
