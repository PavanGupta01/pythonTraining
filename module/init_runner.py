__author__ = 'pavang'
__Date___ = ''

#import  statements are executed at runtime
#print(initialization.spam)

import initialization

print(initialization.spam)

initialization.spam = 5


# Module Loaded only once
import initialization
print(initialization.spam)

print(initialization)

