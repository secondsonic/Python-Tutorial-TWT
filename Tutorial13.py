#How to read a text file

file = open('text.txt', 'r')
f = file.readlines()
print(f)

#now to read properly

newList = []

for line in f:
    if line[-1] == '\n':    #to remove only if there is an \n new line escape char
        newList.append(line[:-1]) #to remove last char for \n 
    else:
        newList.append(line) #to have the last statement in file
print(newList)

#or

newList0 = []

for line in f:
    newList0.append(line.strip())
    
print(newList0)

file.close()