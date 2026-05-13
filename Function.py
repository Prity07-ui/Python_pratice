# Function 
def greet():
     print("Welcome to Python Programming!")
print("Hello, World!")
greet()

#Default Parameter
def student(name="Unknown"):
    print(name)
    student()
    student("Monika")

#function with parameter
def add(a,b):
    print(a+b)
    add(10,20)

#function using multiple arguments
def details(name,age):
    print("Name:" + name)
    print("Age:" + str(age))
    details("Sneha", 21)

 #Function with Return Value
def square(n):          
    return n*n
result = square(5)
print(result)

