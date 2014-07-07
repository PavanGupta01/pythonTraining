__author__ = 'pavang'
__Date___ = ''
import sys
import os


def sort_by_extension():
    source_file = r'/Users/pavang/Documents/tools/performance/lsf'

    lines = [line for line in open(source_file)]
    # print(lines)

    lines.sort(key=lambda lines: os.path.splitext(lines)[1])

    for ln in lines:
        print(ln)

if __name__ == '__main__':
    sort_by_extension()







    # a = [3,4,6]
    # b = [3,4,6]
    #
    # print(a == b)
    # print( a is b)
    # print(isinstance(a,list))



# X = 'Spam'
# def func():
#     X = 'NI'
#     def nested():
#         print(X)
#     nested()
#
# func()
# print(X)
# print(sys.argv[1])