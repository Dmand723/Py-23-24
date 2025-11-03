import datetime

# Define the get_verified_integer function
def get_verified_integer(prompt, min_value, max_value):
    while True:
        try:
            # Get input from the user
            user_input = input(prompt)
            # Convert the input to an integer
            user_input = int(user_input)
            # Check if the input is within the specified range
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print("Try again - ", end="")
        except ValueError:
            # Handle the case when a non-integer value is entered
            print("Try again - ", end="")

# main program starts here
month = get_verified_integer("Please enter today's month (1-12): ", 1, 12)
day   = get_verified_integer("Please enter today's day (1-31): ", 1, 31)
year  = get_verified_integer("Please enter today's year (2000 - 2030): ", 2000, 2030)

# build date object and print out the day of the week
today = datetime.date(year, month, day)
print("Today is a " + today.strftime("%A"))