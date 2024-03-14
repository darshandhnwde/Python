# reduce() = apply a function to an iterable and reduce it to single commulative value
#            performs function on first two value and repeat it until one value is remain
#
# reduce(function , iterable)

import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y : x + y,letters)
print(word)

factorial = [5,4,3,2,1]
answer = functools.reduce(lambda x , y: x * y ,factorial)
print(answer)

# it just basically reduce iterable value in to one 



