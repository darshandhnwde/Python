# map()   = applies a function to each object in an iterables (list , tuple etc)
#
# map(function,iterables)

store = [("shirt",150),
         ("pant",350),
         ("jacket",400),
         ("shoe",300)]

to_dollars = lambda data :(data[0],data[1] / 83.05)

store_dollars = list(map(to_dollars,store))

for i in store_dollars:
    print (i)

# map function used for iterating each object in list tuple etc 