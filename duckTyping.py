# duck typing = concept where the class of an object is less important than methods/attributes
#               class type is not  checked if minimum method /attribute are present
#               "If it walks like a duck , and quacks like a duck ,then it must be duck"

class Duck:
    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is quacking")

class Chicken:
    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken is clucking")

class Person:
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("you caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken) # here Chicken class is working even this has not chicken.walk()and talk() method in person class  
#                      because it has same methods as Duck class and that is the duck typing  
        

