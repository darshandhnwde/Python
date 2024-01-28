# working with List

friends = ["Akash","Saurab","Darshan"]
friends[0]="Kadam"
print("Hello ",friends[0])
print("Hello ",friends[1:2]) 


#List Functions :

Fav_nums = [10,24,2410,1024]
friends = ["Akash","Saurab","Darshan","Darshan","Darshan"]
friends.extend(Fav_nums)
friends.append("Shakya")       # it add element at last  
print(friends)
friends.insert(1,"Tom")
print(friends)
friends.remove("Tom")
print(friends)
friends.pop()          # remove last element
print(friends)
print(friends.index("Darshan"))
print(friends.count("Darshan"))
Fav_nums.sort()        # sorting elements in decending order
Fav_nums.reverse()
print(Fav_nums)
friends2 =friends.copy()
print(friends2)
friends.clear()
print(friends)


# Tuple :
# we can't change the tuple 

coordinate = (4,5)
print(coordinate[1])

# 2D List and Nested loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [6,7,8],
    [0]
]

print(number_grid[2][2])
