# A dictionary is a collection which is unorderd, changable and indexed. No duplicate members.

#create a dict
person = {
    'firstname' : 'john',
    'lastname' : 'doe',
    'age' : 30
}
#use constructor
#person2 = dict(first_name= 'sara', last_name= 'williams')

#get value
print(person['firstname'])
print (person['lastname'])

#add key/value
person['phone']= '0911361231'



#get dict keys
print(person.keys())

#get dict items
print(person.items())

#copy dict
person2 = person.copy()
person2['city'] = 'addisababa'

#remove item
del(person['age' ])
person.pop('phone')

#clear
person.clear()

#get length
print(len(person2))

#list of dict
people = [
    {'name': 'martha', 'age': 39},
    {'name': 'kevin', 'age': 25}
]

print(people[1] ['name'])