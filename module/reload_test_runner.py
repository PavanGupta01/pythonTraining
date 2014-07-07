__author__ = 'pavang'
__Date___ = ''

import reload_test
import imp

reload_test.printer()

reload_test.message = "message before reload"
reload_test.message2 = "additional attribute"
print(reload_test.message)
print(reload_test.message2)

# del reload_test
imp.reload(reload_test)

# reload_test.printer()
print(reload_test.message)



# reload won't delete already created attributes
print(reload_test.message2)