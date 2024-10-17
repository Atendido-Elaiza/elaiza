name = str(input("Enter your name: "))
section = str(input("Enter your section: "))

prelim = float(input("Enter prelim grade: "))
if prelim < 40 or prelim > 100  or prelim == " ":
    print("Input grades is invalid, please try again.")
else:
    midterm = float(input("Enter midterm grade: "))
    if(midterm < 40 or midterm > 100 or midterm == " "):
       print("Input grade is invalid, please try again.")
    else:
        final = float(input("Enter final grade: "))
        if(final < 40 or final > 100 or final == " "):
            print("Input grade is invalid, please try again.")

        else:
            final_grade = round(prelim * 0.3333 + midterm * 0.3333 + final * 0.3333)
            if(final_grade <= 100 and final_grade>= 99):
                grade = 1.00
                description = "Excellent"
            elif(final_grade <= 98 and final_grade >= 96):
                grade = 1.25
                description = "Outstanding"
            elif(final_grade <= 95 and final_grade >= 93):
                grade = 1.50
                description = "Superior"
            elif(final_grade <= 92 and final_grade >= 90):
                grade = 1.75
                description = "Very Good"
            elif(final_grade <= 89 and final_grade >= 87):
                grade = 2.00
                description = "Good"
            elif(final_grade <= 86 and final_grade >= 84):
                grade = 2.25
                description = "Satisfactory"
            elif(final_grade <= 83 and final_grade >= 81):
                grade = 2.50
                description = "Fairly Satisfactory"
            elif(final_grade <= 80 and final_grade >= 78):
                grade = 2.75
                description = "Fair"
            elif(final_grade <= 77 and final_grade >= 75):
                grade = 3.00
                description = "Passed"
            else:
                grade = 5.0
                description = "Failed"
                
        print(f"Final Grade:  {final_grade:.2f}")
        print(f"GPA: {grade}")
        print("Description: " + description)