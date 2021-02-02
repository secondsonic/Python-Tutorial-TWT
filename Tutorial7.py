#While Loops
"""
while condition == True:
    do this

Goes on till condition == False or we can use 'break'
"""
x = 0

while x < 10:
    x = x + 1
    print(x)

loop = True

while loop:
    name = input('Enter some words1: ')
    if name == 'stop':
        loop = False
#OR
y = True

while y:
    name = input('Enter some words2: ')
    if name == 'stop':
        break
