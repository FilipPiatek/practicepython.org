import datetime  #datetime module to get current year

#Getting the name of the user:
name = input("What is your name?  ")

#Getting user age [converting to int]:
age = int(input("How old are you  "))

#Getting current year:
current_date = datetime.date.today()
current_year = int(current_date.year)
#Calculating 100th birthday year:
hundred_birthday = current_year - age + 100
anwser = f"Hi {name}, your 100th birthday will be on the year {hundred_birthday}\n"

print(anwser)

#Getting the number of reps for the message:
reps = int(input("How many times do you want to see this message?"))

print(anwser * reps)