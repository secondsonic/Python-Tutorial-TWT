#IF/ ELIF/ ELSE

"""
if condition == true:
    do this

also 
>= greater than or equal to
<= less than or equal to
"""
"""
age = int(input('Your Age: '))

if age < 18:
    print("You are younger than 18.")
#OR

age = input('Your Age: ')

if int(age) > 18:
    print("You are older than 18.")

age = input('Your Age: ')

if int(age) == 18:
    print("You are 18.")

age = input('Your Age: ')

if int(age) != 18:
    print("You are not 18.")
"""
age = input("Enter your age: ")
if int(age) == 18:
    print("You are 18.")
elif int(age) < 18: #you can have as many as elif you want
    print('You are younger than 18.')
else:   #but only one else since it is a default
    print("You are older than 18.")
