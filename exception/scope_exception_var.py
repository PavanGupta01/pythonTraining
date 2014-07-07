__author__ = 'pavang'
__Date___ = ''


X = 99

try:
    1/0
except Exception as X:                      # Python removes this reference
    print(X)

# print(X)



Y = 20
print([Y for Y in range(10)])
print(Y)