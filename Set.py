odd = {1,3,5,7,9,11}
even = {2,4,6,8,10,12}
prime = {1,2,3,5,7,11}

x = odd.union(even)
print(x)

y = even.intersection(prime)
print(y)

set1 = {1,2,3,4,5,12,14,15}
set2 = {12,13,13,14,15}

diff = set1.difference(set2)
print(diff)

set1.symmetric_difference_update(set2)
print(set1)