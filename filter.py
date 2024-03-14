# filter() = creates a collection of element from an iterable for which a function returns
#
# filter(function , iterable)

friends = [("darshan",20),
           ("akash",21),
           ("saurabh",22),
           ("bhavesh",17),
           ("shakya",16)]

age = lambda data : data[1] >= 18
drinking_buddies = list(filter(age ,friends))

for i in drinking_buddies:
    print(i)

