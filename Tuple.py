# Creating a Tuple

tuple = (1,2,3,4,5)
print(tuple)

#First and last element of the tuple

print(tuple[0])
print(tuple[-1])

#slicing the tuple
print(tuple[1:4])

#Concatenating two tuples
tuple1 = (6,7,8)
tuple2 = tuple + tuple1
print(tuple2)

#Repeting a tuple
tuple3 = tuple * 2
print(tuple3)

#length of a tuple
print(len(tuple1))

#finding the index of an element in a tuple
print(tuple.index(3))

#counting the number of occurrences of an element in a tuple
print(tuple.count(2))

#finding the maximum and minimum element in a tuple
print(max(tuple))
print(min(tuple))

#converting a list to a tuple
list = [9,80,36,13]
tuple = tuple(list)
print(tuple)
