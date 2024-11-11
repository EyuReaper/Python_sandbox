# a module is a file containing a set of functions you want to include in your application.
# there are core python modules, modules you can install using the pip package manager (including django) as well as custom modules

import datetime
from datetime import date
import time
from time import time

#pip module
#from camelcase import CamelCase

#import custom module
import validator
from validator import validate_email

#today = datetime.date.today()
#today = date.today()
#timestamp = time()

#print( timestamp)

#c = CamelCase()

email = 'test@.com'
if validate_email(email):
    print('email is valid')
else:
    print('email is not valid')
 