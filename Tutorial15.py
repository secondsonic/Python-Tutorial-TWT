# .count() and .find() methods

string = 'hello'

print(string.find('e'))
print(string.find('h'))
print(string.find('7')) #if the letter is not in the string it give -1

print(string.count('l'))
print(string.count('ll'))

x = input('input with no underscore: ')
if x.count('_') > 0:
    print("Not good")
else:
    print('Good')
