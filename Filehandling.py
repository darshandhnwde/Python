# catching errors
# Try Except block



try:
    answer =10/0
    number = int(input("Enter a number: "))
    print(number)
    
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input") 

# Reading Files
    
employee_file = open("employee.text","r")
print(employee_file.readlines()[1])

for employee in employee_file.readlines() :
    print(employee)

print(employee_file.read())
print(employee_file.readable())

employee_file.close() 

# Writing to Files

employee_file = open("employee.text","a") # appending means "a" for adding at the end
employee_file = open("employee.text","w")
employee_file = open("employee1.text","a")  # this will creat a new file "employee1.text"
employee_file.write("oscar - Human Resources")
employee_file.write("\nRam - Customer Service")
employee_file.close()



