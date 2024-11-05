#single line comment
'''
this is multi line comment
or doc string used to define a function purpose
can be  single or double quotes
'''

"""
VARIABLE RULES:
    - Variable names are case sensitive (name and NAME are different variables)
    - Variable names with underscores are not allowed
    - Variable names can only start with letters or underscores
    -must have numbers but cannot start with one

"""

x = 1 #int
y = 2.5 #float
name = 'John' #str
is_cool = True #bool

#multiple assignment
x,y,name,is_cool = (1,2.5,'John',True)

print (x,y,name,is_cool)  

#basic math

a = x + y

#casting
x = str(x)
y = int(y)
z = float(y)

print (type(z), z)

