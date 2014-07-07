__author__ = 'pavang'
__Date___ = ''

def multiple(x, y):
    x = 2                   # Changes local names only
    y = [3, 4]
    return x, y             # Return multiple new values in a tuple

if __name__ == '__main__':
    X = 1
    L = [1, 2]

    new_X , new_L = multiple(X, L)       # Assign results to caller's names

    print(new_X)
    print(new_L)

