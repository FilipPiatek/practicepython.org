#Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for element in a:
    if element <= 5:
        print(element)

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
b = []
for element in a:
    if element <= 5:
        b.append(element)

print(b)

c = []

num = input("GIB NUMBER!!  ")
num = int(num)

for element in a:
    if element <= num:
        c.append(element)

print(c)