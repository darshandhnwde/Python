# sort() method = used with lists
# sort() function  = used with iterables

student = ["Darshan","Akash","Saurab","Bhavesh","Ganesh"]
student.sort()
student.sort(reverse=True)  # this reverse parameter arrenge it in reverse alphabetical order
for i in student:
    print(i)

student = ("Darshan","Akash","Saurab","Bhavesh","Ganesh")
sorted_student = sorted(student)                        # for tuple use sorted()
for i in sorted_student:
    print(i)

Info = [("Darshan","A",29),
        ("Akash","B",21),
        ("Saurab","C",22),
        ("Bhavesh","D",23),
        ("Ganesh","F",24)]
grade = lambda grade : grade[1] # for arrenge this based on the second column 
Info.sort(key=grade)            # pass key grade and give index of the column
for i in Info:
    print(i)

age = lambda age : age[2]  # similar for the column 3
#def age(age):
#   return age[2]
Info.sort(key=age)
for i in Info:
    print(i)

