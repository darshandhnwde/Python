import random

x = random.randint(1,6)
print(x)

y = random.random()
print(y)

myList = ["rock" , "paper" ,"sessior"]
z = random.choice(myList)
print(z)

cards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.shuffle(cards)
print(cards)

