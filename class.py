# A class is like a blueprint for creating objects. An oject has properties and methods(functions) associated with it. Almost everything in python is an object

#Create class
class User:

    # Extend class
class Customer(User):

    #Constructor is an object that run when instantiating an object from a class
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balace(self, balance):
        self.balance = balance
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1 

#Init user object
eyu = User('eyuel','1Xs2X@example.com', 28)

#Init customer object
blen = Customer('blen','1Xs2X@example.com', 28)

janet.set_balance(500)

eyu.has_birthday()
print(eyu.greeting()) 