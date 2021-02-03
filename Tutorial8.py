#List and Tuples

x = ['apple', "Ball", 3]
#   Index 0 , Index 1, Index 2

print(x)
print(x[2])

for i in range (3):
    print(x[i])

#easiest way to add to the end of the list

x.append('Y')
print(x)

#easiest way to change an element of the list

x[1] = 0
print(x)

#easiest way to revome an element from the list

x.remove(x[0])
print(x)
x.remove(0)
print(x)

#Tuple
y = (2, 3)
