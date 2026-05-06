""" Dictinory 
 Collection - key + Value=pair = data1
 
 left-side  = key 
right-side = Value
{key1:value1, key2:value2}"""

# Create a dictinory
student = {
    'Priti':450,
    'Sneha':400
}

#Accessing the value of a key 
print(student['Priti'])

#Update the value of a key 
student['Priti'] = 460
print(student['Priti'])

# Delete a key value pair
del student['Priti']
print(student)