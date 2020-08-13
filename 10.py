# Take two lists, say for example these two:
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
#  Make sure your program works on two lists of different sizes. Write this using at least one list comprehension.
#  (Hint: Remember list comprehensions from Exercise 7).
c = []
# Extra:

# Randomly generate two lists to test this
if len(a) >= len(b):
    for elem in a:
        if elem in b:
            c.append(elem)
else:
    for elem in b:
        if elem in a:
            c.append(elem)

print(c)

#Extra solution

a = random.sample(range(100), random.randint(1, 10))
b = random.sample(range(100), random.randint(1, 10))
c = []

if len(a) >= len(b):
    for elem in a:
        if elem in b:
            c.append(elem)
else:
    for elem in b:
        if elem in a:
            c.append(elem)
print(a)
print(b)

print(f'Common list: {c}')