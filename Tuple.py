# A Tuple is a collection which is ordered and unchangeable. 
# Tuples are written with round brackets.
# A Tuple can allow duplicate values.

#create tuple
fruits = ('apples','oranges','pears','apricots')
#fruit2 = tuple(('apples','oranges','pears','apricots'))



#single value needs trailing comma
#fruits2 = ('oranges',)

#get value
#print (fruits[1])


#can't change value
#fruits[0] = 'pears'

#delete tuple
#del fruits2

#get lengh
print (len(fruits))

#A set is a collection which is unordered and unindexed. 
#Sets are written with curly brackets.
#no duplicate members

#create set
fruits = {'apples','oranges','pears','apricots'}
#fruits2 = set(('apples','oranges','pears','apricots'))

#check if in set
print ('oranges' in fruits)

#add to set
fruits.add('grapes')

print(fruits)

#remove from set
fruits.remove('apricots')

print(fruits)

#clear set
fruits.clear()

#delete set
del fruits

print(fruits)