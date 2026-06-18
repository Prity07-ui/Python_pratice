#ATM Mini Project

balance = 10000

amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    balance -= amount
    print("Withdraw Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")