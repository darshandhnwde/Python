mydict = {"name":"Darshan","city":"beed","Age":"20"}
print(mydict)

x = dict(name ="Akash",city ="Parbhani",Age = 20)  # we can write dictonaries using dict() as well
print(x)

value= mydict["name"]
print(value)

mydict["emial"] = "darshan@xyz.com"  # for adding an item
print(mydict) 

mydict.pop("Age") # for deleting any item
print(mydict)

if "name" in mydict:
    print("yes ")
else:
    print("no")

try:
    print(mydict["Lastname"])
except:
    print("error")

for key in mydict:
    print(key)

mydict.update(x) # update() for update and merge the dict
print(mydict)