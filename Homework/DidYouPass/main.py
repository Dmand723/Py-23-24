# You can add an input statement to get the numeric grade from the user
# myGrade = int(input("Enter your numeric grade: "))

# For testing purposes, I'll set a default value here
myGrade = 0
def start():
    global myGrade
    try:
        myGrade = int(input("What is your grade score? : "))
        main()
    except:
        print("please enter a number 0-100")
        start()
def main():

    myLetterGrade = "Not Assigned"

    if myGrade >= 90:
        myLetterGrade = "A"
    elif myGrade >= 80:
        myLetterGrade = "B"
    elif myGrade >= 70:
        myLetterGrade = "C"
    elif myGrade >= 60:
        myLetterGrade = "D"
    else:
        myLetterGrade = "F"

    # Print out the grade
    print("Your grade is:", myLetterGrade)

start()