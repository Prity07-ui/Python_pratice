#   Dictionary
''' 
A Dictionary is a collection which is unordered, changable and indexed. In Python, dictionaries are witten with curly brackets, 
 and they have keys and values.  '''

# Creating a dictionary 
my_dict = {"name": "Riti", "age": 19, "City": "Delhi"}
print(my_dict)

#Acessing items in a dictionary
print(my_dict["name"])
print(my_dict.get("age"))

#Changing value in a dictionary
my_dict["age"]=20
print(my_dict)

#Adding items in a dictionary
my_dict["country"]="India"
print(my_dict)

#Deleting items in a dictonary
del my_dict["City"]
print(my_dict)
my_dict.pop("age")
print(my_dict)
my_dict.clear()
print(my_dict)

