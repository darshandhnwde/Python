class car:
    color = None

class Motorcycle:
    color = None

def change_color(vehicle,color):
    
    vehicle.color = color

car1 = car()
car2 = car()
car3 = car()
car4 = car()

change_color(car1,"red")
change_color(car2,"blue")
change_color(car3,"green")
change_color(car4,"white")

print(car1.color)
print(car2.color)
print(car3.color)
print(car4.color)

bike1 = Motorcycle()

change_color(bike1,"black")
print(bike1.color)