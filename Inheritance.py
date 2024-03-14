# Inheritance :

class Parents():
   
      
     def Skin_color(self):
        print(f"white skin color")

     def look(self):
         print(f"similar to their parents")

class children(Parents):
    
    def Occupation(self):
        print(f"Business")

parent = Parents()
print(parent.Skin_color())
print(parent.look())
children = children()
print(children.Occupation())
print(children.Skin_color()) 

# Multiple inheritance 

class Employee:
    def __init__(self, name) -> None:
        self.name =  name

    def show(self):
        print(f"name : {self.name}")

class Dance:
    def __init__(self,dance ) -> None:
        self.dance = dance

    def show(self):
        print(f"Dance : {self.dance}")

class EmployeeDance(Dance,Employee): # the class which we give first that class inheritance first
    def __init__(self, name,dance) -> None:
        self.name =  name
        self.dance = dance

ED = EmployeeDance("tom","HIPHOP")
print(ED.show())        
print(EmployeeDance.mro())  # method resolution order which show the methods in the class 
