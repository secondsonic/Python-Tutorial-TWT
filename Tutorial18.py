#Error handling, Try and except same as try and catch

text = input('Username: ')
try:
    number = int(text)
    print(number)
except:
    print('Invalid username!')
