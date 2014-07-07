__author__ = 'pavang'
__Date___ = ''


# Only In 3.X
def func_annotation(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c


if __name__ == '__main__':
    total = func_annotation(1,3,5)
    print(total)

    print(func_annotation.__annotations__)