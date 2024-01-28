# while loop

i=1
while i<=24:
    
    print(i)
    i+=1  

# Building guessing game using while loop
    
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
       guess = input("Enter guess: ")
       guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses , You lose")
else:
     print("you win")  

# For loop

Friends = ["Darshan","Akash","Saurab"]
for name in Friends :
    print(name)

for index in range (4,10):
    print(index) 

# Exponent function using for loop
    
def raise_to_power(base_num,pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,4))  

# 2D List and Nested loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [6,7,8],
    [0]
]

for row in number_grid:
    for column in row:
        
        print(column)
    
