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
    else:
        # 4. Test if the user is a debutante.
        if age == 18:
            print("You're a debutante.") # True Block
        else:
            #5. If nothing matches the age description, then the user is an adult.
            print("You're an adult.") # True Block

# 6. Print the concluding message.
print("The program is done.")