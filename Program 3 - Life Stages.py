# Program 3 - Life Stages
# Create a program that asks for an age of a person.
# Display the life stage of the person.
# Rules:
# 0 - 12: Kid
# 13 - 17: Teen
# 18: Debut
# 19 and above: Adult

# Steps
# 1. Ask for age, convert, and store.
age = int(input("Enter your age: "))
# 2. Test if the user is a kid.
if age >-1 and age <=12:
    print("You're a kid.") # True Block
else:
    # 3. Test if the user is a teenager.
    if age >=13 and age <=17:
        print("You're a teenager.") # True Block