# Prompt the user for input
blueMoon = input("Is there a blue moon tonight (Yes / No)? ")
weekDay = input("What is the day of the week (Monday - Sunday)? ")
dayOfMonth = int(input("What is the day of the month (1 - 31)? "))

# Normalize user input to accept both capitalized and lower-case answers
blueMoon = blueMoon.lower()
weekDay = weekDay.capitalize()

# Logic to select and print a song title
if blueMoon == "yes":
    print("Play song 'Once in a Blue Moon'")
elif dayOfMonth <= 7:
    if weekDay == "Monday":
        print("Play song 'Manic Monday'")
    elif weekDay == "Tuesday":
        print("Play song 'Tuesday's Gone'")
    elif weekDay == "Wednesday":
        print("Play song 'Just Wednesday'")
    elif weekDay == "Thursday":
        print("Play song 'Sweet Thursday'")
    elif weekDay == "Friday":
        print("Play song 'Friday I'm in Love'")
    elif weekDay == "Saturday":
        print("Play song 'Saturday in the Park'")
    elif weekDay == "Sunday":
        print("Play song 'Lazing on a Sunday Afternoon'")
    else:
        print("Play song 'Days of the Week'")
else:
    print("Play song 'Day Dream Believer'")