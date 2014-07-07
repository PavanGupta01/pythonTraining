__author__ = 'pavang'
__Date___ = ''

import dir1.dir2.mod

print('*' * 30 + "\tAfter Reload\t" + '*' * 30)
from imp import reload
reload(dir1)