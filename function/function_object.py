__author__ = 'pavang'
__Date___ = ''

def echo(message):               # Name echo assigned to function object
    print(message)


def indirect(func, arg):
    func(arg)                   # Call the passed-in object by adding ()



if __name__ == '__main__':
    echo('Direct call')
    x = echo                           # Now x references the function too
    x('Indirect call!')                # Call object through name by adding ()

    # indirect(echo, 'Argument call!')   # Pass the function to another function


    # schedule = [(echo, 'Spam!'), (echo, 'Ham!')]
    # for (func, arg) in schedule :
    #     func(arg)                     # Call functions embedded in containers

    print(echo.__code__.co_varnames)

