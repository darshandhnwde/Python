# *args :

# *args are the parameter that will pack all the argument in tuple and
#  useful so that function can accept varing amount of arguments 

def add(*args): # no need to pass argument in add function cause of args 
    sum = 0
    args = list(args)
    args[0] = 3     # we can change the value by converting it in to list cause tuple can't change
    for i in args:
        sum += i 
    return sum 

print(add(2,3,5,7,12,43))

# we can give as much as arguments in it