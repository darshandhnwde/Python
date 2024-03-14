# **kwargs are the parameter that will pack all the argument in dictionary and
#  useful so that function can accept varing amount of keyword arguments 


def Intro(**kwargs):  # here it is taking keyword argument
    print("hello",end=" ")
    for key,value in kwargs.items():
        print(value , end=" ")

Intro(title= "Mr",firstname="Darshan",middlename="Kashinath",lastname="Dhanwade")

# you can add more keyword argument
