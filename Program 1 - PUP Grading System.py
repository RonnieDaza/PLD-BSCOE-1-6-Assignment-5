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
        else:
            # 5. If the input didn't match the first 3 special conditions, then convert the grade percentage to float.
            gradePercentage = float(gradePercentage)

            # 6. Round off the grade percentage.
            roundoffGrade = round(gradePercentage)

            # 7. Test if the grade percentage is 1.00 and excellent.
            if roundoffGrade >=97 and roundoffGrade <=100:
                print("Your Grade/Mark is: 1.0") # True Block
                print("Your Description is: Excellent") # True Block
            
            # 8. Test if the grade percentage is 1.25 and excellent.
            elif roundoffGrade >=94 and roundoffGrade <=96:
                print("Your Grade/Mark is: 1.25") # True Block
                print("Your Description is: Excellent") # True Block
            
            # 9. Test if the grade percentage is 1.5 and very good.
            elif roundoffGrade >=91 and roundoffGrade <=93:
                print("Your Grade/Mark is: 1.5") # True Block
                print("Your Description is: Very Good") # True Block
            
            # 10. Test if the grade percentage is 1.75 and very good.
            elif roundoffGrade >=88 and roundoffGrade <=90:
                print("Your Grade/Mark is: 1.75") # True Block
                print("Your Description is: Very Good") # True Block
            
            # 11. Test if the grade percentage is 2.0 and good.
            elif roundoffGrade >=85 and roundoffGrade <=87:
                print("Your Grade/Mark is: 2.0") # True Block
                print("Your Description is: Good") # True Block
            
            # 12. Test if the grade percentage is 2.25 and good.
            elif roundoffGrade >=82 and roundoffGrade <=84:
                print("Your Grade/Mark is: 2.25") # True Block
                print("Your Description is: Good") # True Block
            
            # 13. Test if the grade percentage is 2.5 and satisfactory.
            elif roundoffGrade >=79 and roundoffGrade <=81:
                print("Your Grade/Mark is: 2.5") # True Block
                print("Your Description is: Satisfactory") # True Block
            
            # 14. Test if the grade percentage is 2.75 and satisfactory.
            elif roundoffGrade >=76 and roundoffGrade <=78:
                print("Your Grade/Mark is: 2.75") # True Block
                print("Your Description is: Satisfactory") # True Block
            
            # 15. Test if the grade percentage is 3.0 and passing.
            elif roundoffGrade ==75:
                print("Your Grade/Mark is: 3.0") # True Block
                print("Your Description is: Passing") # True Block