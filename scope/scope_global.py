__author__ = 'pavang'
__Date___ = ''


glob_var = 5

def print_globvar():
    print(glob_var)       # No need for global declaration to read value of globvar


def set_globvar_to_one():
    global glob_var                 # Needed to modify global copy of globvar
    glob_var = 1
    print(glob_var)

def local():
    glob_var = 10                                # local glob in dummy function
    print(glob_var)

def add_global():
    global x
    x = "Global var added"


if __name__ == '__main__':
    print_globvar()
    set_globvar_to_one()
    local()


    # add_global()
    # print(x)

