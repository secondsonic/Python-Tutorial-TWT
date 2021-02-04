#Function

def addTwo(x):  # x is a parameter
    return x + 2

def subtractTwo(x):
    return x -2

def printString(string):    #string is a parameter
    print(string)

def momentum(mass, velocity):
    p = mass * velocity
    return p

def doSomething():
    print('Something')
    
add_result = addTwo(int(input('Enter an integer: ')))
sub_result = subtractTwo(int(input('Enter an integer: ')))

doSomething()

print(add_result, sub_result)
printString("This is a String,") # "This is a String" is an argument
printString("This is a String too,")
printString("This is a String as well.")

print(momentum(2,5))
