__author__ = 'pavang'
__Date___ = ''

def f1():
    X = 88
    def f2():
        print(X)                    # Remembers X in enclosing def scope
    return f2                       # Return f2 but don't call it

if __name__ == '__main__':
    # Most importantly, f2 remembers the enclosing scope’s X in f1,
    # even though f1 is no longer active—

    action = f1()                       # Make, return function
    action()                            # Call it now: prints 88


