# # Student: [Your Student Name]

# import datetime
# import math
# import random

# # Provided tuples
# options = ("Sightseeing", "Shopping", "Dining", "Outdoor Activities", "Entertainment")
# prices = (50.00, 100.00, 75.00, 120.00, 80.00)

# # Prompt user for starting date
# startDateString = input("Enter the starting date of your vacation (MM/DD/YYYY): ")

# # Convert start date string to datetime object
# startDate = datetime.datetime.strptime(startDateString, "%m/%d/%Y")

# # Prompt user for stop date
# stopDateString = input("Enter the stop date of your vacation (MM/DD/YYYY): ")

# # Convert stop date string to datetime object
# stopDate = datetime.datetime.strptime(stopDateString, "%m/%d/%Y")

# # Calculate vacation length
# delta = stopDate - startDate

# # Print the length of the vacation
# print("Your vacation is {} days long".format(delta.days))

# # Find the most expensive day
# most_expensive_day_cost = max(prices)
# print("The most expensive day cost ${:.2f}".format(most_expensive_day_cost))

# # Find the least expensive day
# least_expensive_day_cost = min(prices)
# print("The least expensive day cost ${:.2f}".format(least_expensive_day_cost))

# # Calculate the total cost
# total = sum(prices)
# print("Your total trip cost is ${:.2f}".format(total))

# # Calculate the average cost per day
# average = total / delta.days
# print("Your average cost per day is ${:.2f}".format(average))



# Student: [Your Student Name]

import datetime
import math
import random

# Provided tuples
options = ("Sightseeing", "Shopping", "Dining", "Outdoor Activities", "Entertainment")
prices = (50.00, 100.00, 75.00, 120.00, 80.00)

# Prompt user for starting date
startDateString = input("Enter the starting date of your vacation (MM/DD/YYYY): ")

# Convert start date string to datetime object
startDate = datetime.datetime.strptime(startDateString, "%m/%d/%Y")

# Prompt user for stop date
stopDateString = input("Enter the stop date of your vacation (MM/DD/YYYY): ")

# Convert stop date string to datetime object
stopDate = datetime.datetime.strptime(stopDateString, "%m/%d/%Y")

# Calculate vacation length
delta = stopDate - startDate

# Print the length of the vacation
print("Your vacation is {} days long".format(delta.days))

# Initialize costs list
costs = []

# Loop through each day of the vacation
for day in range(delta.days + 1):
    # Pick a random activity index
    activity_index = random.randint(0, len(options) - 1)

    # Read the activity description and cost
    activity = options[activity_index]
    cost = prices[activity_index]

    # Calculate current date and display string for that date
    this_date = startDate + datetime.timedelta(days=day)
    thisDateString = this_date.strftime("%m/%d/%Y")

    # Print daily details and append cost to the end of costs list
    print(str.format("On {}, {} costs ${:.2f}", thisDateString, activity, cost))
    costs.append(cost)

# Find the most expensive day
most_expensive_day_cost = max(costs)
print("The most expensive day cost ${:.2f}".format(most_expensive_day_cost))

# Find the least expensive day
least_expensive_day_cost = min(costs)
print("The least expensive day cost ${:.2f}".format(least_expensive_day_cost))

# Calculate the total cost
total = sum(costs)
print("Your total trip cost is ${:.2f}".format(total))

# Calculate the average cost per day
average = total / delta.days
print("Your average cost per day is ${:.2f}".format(average))
