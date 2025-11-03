# import datetime

# def get_day_of_week(date_str):
#     try:
#         # Attempt to parse the date string
#         date_object = datetime.datetime.strptime(date_str, "%Y-%m-%d")
#         # Get the day of the week as an integer (0 = Monday, 6 = Sunday)
#         day_of_week = date_object.weekday()
#         # Define a list of days of the week
#         days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#         # Return the day of the week
#         return days[day_of_week]
#     except ValueError:
#         # If the date format is invalid, return an error message
#         return "Invalid date format"

# # main code starts here
# print(get_day_of_week("1776-07-04")) # US Declaration of Independence adopted
# print(get_day_of_week("1918-11-11")) # World War I Armistice Day
# print(get_day_of_week("3-16-2001"))   # Test invalid date format
a = "alpha"
 
def mystery(letter):
    print(letter)
    letter = "omega"
    print(letter)
    return letter
 
print(a)
a = mystery(a)
print(a)