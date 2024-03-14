# methd overriding :

class Animal:
    def eat(self):
        print("this animal is eating")


class Rabbit(Animal):
    def eat(self):
        print("this rabbit is eating a carrot")
 

rabbit = Rabbit()
rabbit.eat()
     
# In methd overriding basically object will use a method which is more closely associated 
# with itself first before relaying on method which inherit form it's parent class 