# Dawson Simmons

# Start the Conversation
name = input("What is your name?" )
print("Hi " + name + ", nice to meet you.  I am Chatbot-1024.")

# ask about a favorite sport
sport = input("What is your favorite sport? ")
if ((sport == "football") or (sport == "Football")):
  # respond to football with a question
  yards = input("I like football too.  Can you tell me the length of a football field in yards? ")
  # verify and comment on the answer
  if (int(yards) < 100):
     print("No, too short.")
  elif (int(yards) > 100):
     print("No, too long.")
  else:
     print("That's right!")

elif ((sport == "baseball") or (sport == "Baseball")):
  # respond to baseball with a question
  strikes = int(input("I play baseball every summer.  How many 'strikes' does it take to get a batter out? "))
  # verify and comment on the answer
  if (strikes == 3):
     print("Yes, 1, 2, 3 strikes you're out...")
  else:
     print("Actually, 3 strikes will get a batter out.")

elif ((sport == "basketball") or (sport == "Basketball")):
  # respond to basketball with a question
  team = input("The Harlem Globetrotters are the best.  Do you know the name of the team they always beat? ")
  # verify and comment on the answer (check for either version with or without capitals)
  if ((team == "washington generals") or (team == "Washington Generals")):
     print("Yes, those Generals can never catch a break.")
  else:
     print("I think it's the Washington Generals.")

else:
  # user entered a sport we don't recognize, so just display a standard comment
  print("That sounds cool; I've never played " + sport + ".")

print("Great chatting with you.")
