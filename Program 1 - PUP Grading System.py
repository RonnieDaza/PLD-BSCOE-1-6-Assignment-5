# Program 1: PUP Grading System
# Create a program that will ask for grade percentage.
# Display the equivalent Grade/Mark and Description.
# Grade/Mark          Percentage/Equivalent          Description        
# 1.0                 97-100                         Excellent
# 1.25                94-96                          Excellent
# 1.5                 91-93                          Very Good
# 1.75                88-90                          Very Good
# 2.0                 85-87                          Good
# 2.25                82-84                          Good
# 2.5                 79-81                          Satisfactory
# 2.75                76-78                          Satisfactory
# 3.0                 75                             Passing
# 5.0                 65-74                          Failure
# Inc.                                               Incomplete
# W                                                  Withdrawn
# D                                                  Dropped

# Steps
# 1. Ask for the grade percentage of the user.
gradePercentage = input("Enter your grade percentage: ")

# 2. Test if the user input is Incomplete.
if gradePercentage == "Inc.":
    print("Your status is: Incomplete") # True Block
else:
    # 3. Test if the user input is Withdrawn.
    if gradePercentage == "W":
        print("Your status is: Withdrawn") # True Block
    else:
        # 4. Test if the user input is Dropped.
        if gradePercentage == "D":
            print("Your status is: Dropped") # True Block