#Function to Check Even or Odd

from tokenize import Number


def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd(7)

#Function to Find Maximum Number

def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print(maximum(10, 20))