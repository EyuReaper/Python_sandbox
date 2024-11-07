# A list is  a collection which is ordered and changeble. Allows duplicate memebers.

#create list
numbers = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']

#use a constructor
#numbers2 = list((1,2,3,4,5))

print (fruits[1]) 

#get length
print (len(fruits))

#append to list
fruits.append('grapes')

#remove from list
fruits.remove('oranges')

#insert into position
fruits.insert(2,'strawberries')

#change value
fruits[0] = 'kiwi'

#remove with pop
fruits.pop(2)

#reverse list
fruits.reverse()

#sort list
fruits.sort()

#reverse sort
fruits.sort(reverse=True)

print (fruits)