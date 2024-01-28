# If-else Statment :

is_male = False
is_tall = False
if is_male and  is_tall:
    print("you are a male and tall")
elif is_male and not(is_tall) :
    print("you are male but not tall")
elif not(is_male) and is_tall :
    print("you are not male but tall")
else :
    print("you are neither male nor tall") 


# If-else Statment and comparison
    
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3 :
        return num1
    elif num2 >= num1 and num2 >= num3 :
        return num2
    else:
        print("num3 is greater")
    
print(max_num(12,3,4)) 
   
# Building a calculator using if else

num1 =eval(input("Enter first number: "))
op = input ("Enter operator: ")
num2 =eval(input("Enter second number: "))

if op == "+" :
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*" :
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print(" invalid operator")
