# Super function = Function used to give access to the method of parent class
#                  return a temperory object of parent class when used 

class Rectangle:
    def __init__(self,X ,Y) -> None:
        self.length = X
        self.width = Y

    def area(self):
        return self.length * self.width
        
class Circle(Rectangle):
    def __init__(self,X,Y) -> None:
        super().__init__(X ,Y)

    def area(self):
        return 3.14 * self.length * self.width
        

rectangle =  Rectangle(24,10)
print(rectangle.area())
circle  = Circle(2,2)
print(circle.area())