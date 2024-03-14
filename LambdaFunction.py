# lambda function = function written in oe line using lambda keyword
#                   accept any number of argument but has only expression
#                   (think of it as shortcut)
#                   (useful if needed for short period of time ,throw away)

# sytntax  : lambda arguments :expression

def double(x):
    return x*2

print(double(3))

# above code uing lambda function

double = lambda x : x * 2
print(double(3))

addition = lambda x,y,z: x+y+z
print(addition(1,2,3))         # we can pass many parameter

full_name = lambda first_name,last_name : first_name+" "+last_name
print(full_name("Darshan","Dhanwade"))

eligible_for_vote = lambda age: True if age>=18 else False
print(eligible_for_vote(20))
