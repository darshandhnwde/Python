# Method chaining = calling multiple method sequentially 
#                   each call perform an action on the same object and return self

class Car:
    def turn_on(self):
        print("You start the car engine")
        return self
        
    def drive(self):
        print("You drive the car")
        return self

    def Break(self):
        print("You step on the break")
        return self

    def turn_off(self):
        print("You turn of the car engine")
        return self

car = Car()
car.turn_on().drive().Break().turn_off() # we can call all the method in one line of code 
#car.turn_on()\
#        .drive()\
#        .Break()\
#        .turn_off() you can write like this for more convinent of understanding using back slash
