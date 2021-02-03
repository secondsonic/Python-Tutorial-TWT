#Slice operator

fruits = ['apples', 'pears', 'strawberries']
text = 'Hello I like Python'

print(text[0:5])    #slice[start:stop:step] like for loops range
#or
print(text[:5]) #default start is at index 0 or beginning

print(text[0:]) #default stop is till the end

print(text[::3])    #step example

print(fruits[1:])
'''
.append() was adding things to the end of the list
now what if we want it in the beginning or middle
'''

fruits.append('raspberries')
print(fruits)

#in the beginning for example
x = ['blueberries']
fruits[0:0] = x
print(fruits)

#or

fruits[2:2] = 'peach'.split()
print(fruits)
