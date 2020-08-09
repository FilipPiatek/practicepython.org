# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

text = input("Give me a word to check if its a palindrome or not.")
i = 0
for c in text:
    if text[i] == text[i - len(text)]:
        print("Hi")
        continue
    else:
        print(f"{text} is not a palindrome")
