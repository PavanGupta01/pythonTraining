__author__ = 'pavang'
__Date___ = ''

def hider():
    open = 'spam'          # Local variable, hides built-in here
    # open('data.txt')       # Error: this no longer opens a file in this scope!

if __name__ == '__main__':
    hider()
