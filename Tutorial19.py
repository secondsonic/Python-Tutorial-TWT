#Global vs Local

x = 0   #Global
x0 = 1  #Global
x1 = 2  #Global
x2 = 50 #Although it is Global but the 'global' in local scope messed it up 

print(x2)   #once it hits the 'global x2' in the local ,the first x2 is useless

def func():

    x0 = [1,2,3,4,5,6,7,8,9]
    
    x1 = 999            #Local
    global x2           #DO NOT EVER USE THIS GLOBAL THIS WAY
    x2 = 10             #UNLESS THERE IS NO OTHER WAY!
    print(x1)
    for x in x0:

        if x % 3 == 0:
            print (x)   #Local
            print (x0)  #Local
        else:
            print (' ')

func()
print()
print(x,x0,x1,x2)       #Only the x2 in local will be showed
x2 = 100
print(x2)   #IKR?! WHAT??? 3 x2s with three values, and all are global?
            #do not confsue yourself and other, vars matters!
