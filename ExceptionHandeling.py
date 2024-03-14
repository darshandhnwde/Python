# Exception handling


try:
     numerator = int(input("enter the numerator"))
     denominator =int(input("enter the denominator"))
     result = numerator / denominator

     

except ZeroDivisionError as e:
     print(e)
     print("You cant divide by zero")

except ValueError as e:
      print(e)
      print("you can divide only with numbers")

except Exception as e:
      print(e)   
      print("something went wrong")

else:
     print(result)


      
