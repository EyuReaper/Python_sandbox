#Strings in python are are surrounded by either single or double quotation marks. 

name = 'Eyuel'
age = 28

#concatenation
print ('Hello my name is ' + name + ' and I am ' + str(age))
#string formatting

#arguments by position
print ('My name is {name} and I am {age}'.format(name=name,age=age))

#f-strings
print (f'My name is {name} and I am {age}')

#String Methods
s = 'hello world'

#capitalize string
print (s.capitalize()) 

#make all uppercase
print (s.upper())

#make all lowercase
print (s.lower())

#swap case
print (s.swapcase())

#get length
print (len(s))

#replace
print (s.replace('world','everyone'))

#split into a list
print (s.split())

#check startswith
print (s.startswith('hello'))

#check endswith
print (s.endswith('d'))

#check if contains
print ('hello' in s)

#count
print (s.count('o'))

#find
print (s.find('o')) 

#rfind
print (s.rfind('o'))

#format
print (s.format(name=name, age=age))

#join
print ('.'.join(['hello','world']))

