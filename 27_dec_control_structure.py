__author__ = 'pavang'
__Date___ = ''

# Does python support char data types

st = """ hiii hello \t \n dfklsvkdsnsdnj "ygdfjgsjfg" 'efjjdsdfsnkjn' """


# Change a string and make a new one
def str_demo():
    city = 'Pune'
    city = city + ' Synerzip'
    print(city[3:5])
    print(city.upper())
    print(city)
    city.replace('Pune', 'Mumbai', 1)


def file_print(file_path):
    f = open(file_path, 'r')

    #print(f.readline())

    # print(f.readlines())

    for line in f.readlines():
        print(line)

    # print(f.read())

    print('=' * 45 + 'File Attribute' + '=' * 45)
    print("Name of the file: " + f.name)
    print("Closed or not : " + str(f.closed))
    print("Opening mode : " + f.mode)




    f.close()


def write_file(file_path):
    fo = open(file_path, "w")
    fo.write("Python is a great language.\nYeah its great fun!!\n ")
    fo.close()


# Why strings are immutable in Python

def func(a,b):
    a += 20
    print("insert func  " + str(a),str(b))
    return a + b

if __name__ == '__main__':
    # "c:\new\text.txt"

    # f_path_read = r'/tmp/run03.csv'
    # f_path_write = r'/tmp/aboutPyhon.txt'
    # file_print(f_path_read)
    # write_file(f_path_write)

    a = 10
    b = 40
    print(func(a,b))
    print(a,b)





# ByteArray (Mutable String)

# print as a statement and as function

# equality check(== and is)

# List comprehension