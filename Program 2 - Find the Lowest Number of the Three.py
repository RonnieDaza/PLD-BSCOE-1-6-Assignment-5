# Program 2 - Find the Lowest Number of the Three
# Find the lowest number.
# Create a program that asks 3 numbers.
# Find the lowest number using only if-else statement.
# Display the lowest number.

# Steps
# 1. Ask the user for the first number.
firstNumber = float(input("Enter the first number: "))
# 2. Ask the user for the second number.
secondNumber = float(input("Enter the second number: "))
# 3. Ask the user for the third number.
thirdNumber = float(input("Enter the third number: "))

# 4. Test if the first number is the lowest of all the three numbers.
if firstNumber < secondNumber and firstNumber < thirdNumber:
    lowestOfall = firstNumber