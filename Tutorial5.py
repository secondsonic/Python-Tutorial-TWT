#Chained Conditionals and Nested Statements

"""
Key words:
and , or , not
"""

x = 2
y = 3

if x == y and x + y == 5: #you can chain as many as you want
    print("HI")
else:
    print("Bye")

if x == y or x + y == 5:
    print("HI")
else:
    print("Bye")

if not(x == y or x + y == 5):
    print("HI")
else:
    print("Bye")

if not(x == 3 or x + y == 6):
    print("HI")
else:
    print("Bye")

#Nested
a = int(input())
b = int(input())
if a == 2:
    if b == 3:
        print('a == 2, b == 3')
    else:
        print('b != 3')
else:
    print('a != 2')
