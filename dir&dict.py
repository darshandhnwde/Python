# dir , __dict__ and help :

x = [1,3,5,6]
print(dir(x)) # for knowing the different methods
print(x.__add__)

# __dict__

from Constructor import Bank

bank = Bank("SBI","State Bank Of India","Government")
print(bank.__dict__)  # __dict__ represent a dictionary or any mapping object 
# that is used to store the atttribute of the object


print(help(Bank))  # help fun is used to get help documentation for an object , including description
#of its attribute and methods
