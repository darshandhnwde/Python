#Higher Order Function  = a function that either 
#                           1. accept a function as a argument
#                               or
#                           2. return a function
#                               (In python, function are also treated as object)

def Petrol(car):
    print("You bought a petrol or Fuel car")

def EV(car):
    print("You bought a EV car")

def Buy_car(func):
   car = func(None)

Buy_car(Petrol)
Buy_car(EV)

#                           2. return a function
#                               (In python, function are also treated as object)

def divisor(x):
    def dividend(y):
        return y/x 
    return dividend

divide = divisor(2)
print(divide(10))
