# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

text = input("Give me a word to check if its a palindrome or not.")
palindrome = []
for c in text:
    palindrome.insert(0, c)

palindrome = ''.join(map(str, palindrome))
if palindrome == text:
    print("Your word is a palindrome")
else:
    print("Your word is not a palindrome")