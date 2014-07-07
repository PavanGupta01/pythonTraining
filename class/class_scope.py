__author__ = 'pavang'
__Date___ = ''

# X defined 5 times throughout the program


X = 11                      # Global (module) name/attribute (X, or manynames.X)

def f():
    print(X)                # Access global X (11)

def g():
    X = 22                  # Local (function) variable (X, hides module X)
    print(X)

class C:
    X = 33                          # Class attribute (C.X)
    def m(self):
        X = 44                      # Local variable in method (X)
        self.X = 55                 # Instance attribute (instance.X)


if __name__ == '__main__':
    obj = C()
    obj.m()

    print(C.X)
    print(obj.X)

    print("Dictionary")

    print(obj.__dict__)
    # print(C.__dict__)
    print([{item:C.__dict__[item]} for item in C.__dict__.keys() if not item\
        .startswith(
            '__')])