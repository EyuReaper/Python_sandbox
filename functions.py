# A function is a block of code which runs only when it is called. In python, we do not use curly brackets, we use indentation with tabs or spaces


# Create function

def sayHello(name):
    print(f'hellow {name}')

sayHello('John Doe')

#Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

num = getSum(3, 4)
print(num)
# a lambda function is small anonymous function
# a lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2: num1 + num2

print(getSum(10, 13))
