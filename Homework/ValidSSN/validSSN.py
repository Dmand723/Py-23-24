# # Limit the number of attempts to 3
# for attempt in range(3):
#     ssn = input("Please enter your 9-digit Social Security Number: ")

#     # Ensure the input string has a length of 9
#     if len(ssn) != 9:
#         print("Error: Social Security Number must have 9 digits.")
#         continue

#     # Ensure that the input string is a valid integer
#     try:
#         ssn_int = int(ssn)
#     except ValueError:
#         print("Error: Social Security Number must be a valid integer.")
#         continue

#     # Ensure that the input number is within the valid range
#     if ssn_int < 0 or ssn_int > 999999999:
#         print("Error: Social Security Number must be between 000000000 and 999999999.")
#         continue

#     # If all checks pass, break out of the loop
#     break
# else:
#     # If the loop completes without a valid input, print an error message and quit
#     print("You have exceeded the maximum number of attempts. Please try again later.")
#     exit()

# print("You have entered a valid Social Security Number:", ssn)
print(int("dad"))