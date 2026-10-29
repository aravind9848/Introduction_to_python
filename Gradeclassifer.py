grade = float(input("grade/20: "))

if grade < 0 or grade > 20:
    print("Invalid grade. Please enter a grade between 0 and 20.")
else:
    if grade >= 16:
        print("Grade: A")
    elif grade >= 14:
        print("Grade: B")
    elif grade >= 12:
        print("Grade: C")
    elif grade >= 10:
        print("Pass")
    else:
        print("Fail")