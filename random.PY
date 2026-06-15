#random

import random

secret = random.randint(1, 10)

guess = int(input("Guess Number (1-10): "))

if guess == secret:
    print("You Win!")
else:
    print("Correct Number:", secret)