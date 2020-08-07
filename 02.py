#Getting a number form the user:
number = input("What's the number?")
number = int(number)

#Checking if number is odd or even and if its even is it multiple of 4:

if number % 2 == 0:
    if number % 4 == 0:
        print('Your number is even and is a multiple of 4')
    else:
        print("Your number is even but it's not a multiple of 4")
else:
    print("Your number is odd")

#Checking if users 2 numbers are divisible by eachother:
num = int(input("Enter first number: "))
check = int(input("Enter second number: "))

if num % check == 0:
    print(
        f"Your first number {num} devides by your second number {check} evenly"
    )
else:
    print("Your numbers don't devide evenly")