# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
#  You can (and should!) use your answer to Exercise 4 to help you.
prime = ""

num = int(input("Give me a number "))

for number in range(1, (num - 1)):
    if num % number == 0:
        prime = number

if prime == 1:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")