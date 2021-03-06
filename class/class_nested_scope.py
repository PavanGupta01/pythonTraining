__author__ = 'pavang'
__Date___ = ''

X = 1
def nester():
    X = 2                                       # Hides global
    print(X)                                    # Local: 2

    class C:
        X = 3               # Class local hides nester's: C.X or I.X (not scoped)
        print(X)            # Local: 3

        def method1(self):
            print(X)        # In enclosing def (not 3 in class!): 2
            print(self.X)   # Inherited class local: 3

        def method2(self):
            X = 4           # Hides enclosing (nester, not class)
            print(X)        # Local: 4
            self.X = 5      # Hides class
            print(self.X)   # Located in instance: 5

    I = C()
    I.method1()
    I.method2()


if __name__ == '__main__':
    nester()