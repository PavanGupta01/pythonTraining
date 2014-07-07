__author__ = 'pavang'
__Date___ = ''

class Parent(object):
    x = 5
    def n(self):
        return self.x + 2

class dummy():
    x = 50

class Child(Parent):
    x = 8
    def m(self):
        return self.x + 4 + Parent.n(dummy)

# p = Parent()
c = Child()

print(issubclass(Child, Parent))

# print p.n()
print(c.m())
#print(c.n())

