#String Methods
'''
For example:
.strip(), .len(), .lower(), .upper(), .split(), ...
len is a function not a method btw
'''
text = input("Enter something: ")
#strip removes spaces after and before a word
print(text)
print(text.strip())
print(len(text))
print(text.lower())
print(text.upper())
print(text.split())
#split is so cool look at these
text0 = input('Input: ')
#input0: Hey What'S uP ?
print(text0.split(' ')) #default slipt is already with space in between words
#input1: hey.what's.up
text1 = input('Input: ')
print(text0.split('.'))

#https://www.tutorialspoint.com/python/python_strings.htm
