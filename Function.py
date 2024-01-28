# Function :

def IntroduceYourself(name,age):
    print("Hello , my name is "+name)
    print("I am "+age +" years old")

IntroduceYourself("Darshan","20")


# Return statment :

def cube(num):
    return num * num * num

print(cube(24))
print("\n")

def Bankdetails(bankname,accountnum,ifccode,branch):
    print("Bank name is : "+bankname)
    print("The Account Number is : "+accountnum)
    print("IFC Code is : "+ifccode)
    print("Branch of bank is : "+branch)

Bankdetails("SBI","40514637798","SBIN0009066","Talkhed") 

# Building a Translator using  function

def Translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation =translation + letter
    return translation
print(Translate(input("Enter a phrase: ")))



