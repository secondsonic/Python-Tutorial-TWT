# Iteration by item

fruits = ['apples', 'pears', 'straberries']

for fruit in fruits:
    print(fruit)
print()

#or
for x in range(0,3):
    print(fruits[x])
print()

numbers = [0,1,2,3,4,5,6,7,8,9]

print('What numbers are divisible by 3 in range of 0-9')
for number in numbers:
    if number % 3 == 0:
        print([number]) #you do not need [] tho I did it cuz i like it
    else:
        print(number, " is not divisible by 3")
print()

#or

for x in range(10):
    if numbers[x] % 3 == 0:
        print(numbers[x])
    else:
        print(numbers[x], " is not divisible by 3")
print()

#or

for x in range(len(numbers)):
    if numbers[x] % 3 == 0:
        print(numbers[x])
    else:
        print(numbers[x], " is not divisible by 3")
