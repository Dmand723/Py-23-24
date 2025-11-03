import random

def select_quote():
    # set up a tuple of available quotes
    quotes = ("My fake plants died because I did not pretend to water them - Mitch Hedberg",
              "There cannot be a crisis next week. My schedule is already full. - Henry Kissinger",
              "Weather forecast for tonight: dark. - George Carlin",
              "All generalizations are false, including this one. - Mark Twain",
              "Why do they call it rush hour when nothing moves? - Robin Williams")

    # Get the number of quotes in the tuple
    numQuotes = len(quotes)

    # Generate a random index
    index = random.randrange(0, numQuotes)

    # Print the random quote
    print(quotes[index])

    # Return statement
    return

# Call select_quote() twice to print two random quotes
select_quote()
select_quote()