#Classes and Objects

x = 'String' #an object of class str
y = 10       #an object of class int
print(type(x),type(y)) #each object has its own attribiutes

print(x.count('S')) #y doest have a count

class number():
    def __init__(self, num): #the purpose using self is same as this in java
        self.var = num

    def display(self, x):
        print(x)

num = number(23)
print(num)

num.display(num.var)
