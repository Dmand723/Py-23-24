#I think them given a formula is a little too easy but i would give them a time limit like 2 minutes to come up with the 6 numbers like so 
#Have someone else not playing or the teacher time them



print("to win all of these following conditions must be met: \n 1. number 1 must be greater then number 6 \n 2. number 2 times number 3 must be greater than 20 \n 3. number 4 minus (number 5 times number 1) must be less than 0")
number1 = int(input("Number 1?: "))
number2 = int(input("Number 2?: "))
number3 = int(input("Number 3?: "))
number4 = int(input("Number 4?: "))
number5 = int(input("Number 5?: "))
number6 = int(input("Number 6?: "))

# Check the conditions for a winning ticket
if number1 > number6 and number2 * number3 > 20 and number4 - (number5 * number1) < 0:
    print("Winner!")
else:
    print("Thanks for your contribution to the math club")
