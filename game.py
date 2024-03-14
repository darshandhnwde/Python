# making rock ,paper , scissors game :

import random
while True:
   choice = ["rock","paper","scissors"]
   computer = random.choice(choice)
   player = None
   while player not in choice:
      player = input("rock,paper or scissors : ").lower()

      if computer == player:
       print("computer : ",computer)
       print("player : ",player)
       print("TiE")
      elif computer=="paper":
        if player=="rock":
           print("computer : ",computer)
           print("player : ",player)
           print("You lose the game")

        if player=="scissors":
          print("computer : ",computer)
          print("player : ",player)
          print("You win the game")
      elif computer=="rock":
        if player=="paper":
         print("computer : ",computer)
         print("player : ",player)
         print("You win the game")
    
        if player=="scissors":
          print("computer : ",computer)
          print("player : ",player)
          print("You lose the game")
      elif computer=="scissors":
        if player=="rock":
          print("computer : ",computer)
          print("player : ",player)
          print("You win the game")

        if player=="paper":
          print("computer : ",computer)
          print("player : ",player)
          print("You lose the game")


   play_again = input("play again ?,(yes/no)").lower()
   if play_again!="yes":
     break
print("By")


      
