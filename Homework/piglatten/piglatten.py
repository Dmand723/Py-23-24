# # initialize size variable
# size = 0

# # get and validate user size input

# # get input string we want to transform
# sentence = input("Please enter a word, phrase or sentence: ")

# # break string into list of individual words
# words = sentence.split()

# # initialize empty pig latin version of the input sentence
# piglatin = ""

# # for each word, convert and build piglatin output
# for word in words:
#     # convert word to lower case
#     word = word.lower()
    
#     # get first character to examine
#     first_char = word[0]
    
#     # If the first letter is a vowel
#     if first_char in 'aeiou':
#         # add the letters "\way" to the end of the word.
#         word += "way"
#     else:
#         # else the first letter is a consonant
#         # find the first vowel
#         for i in range(len(word)):
#             if word[i] in 'aeiou':
#                 size = i
#                 break

#         # break the word into 2 pieces at the "size" index
#         # build new word by starting with the last part, adding a backslash,
#         # then the first part, then the characters "ay" at the end
#         word = word[size:] + "\\" + word[:size] + "ay"
    
#     # add the new word to the end of the pig latin string, plus a space
#     piglatin += word + " "

# # print the original and final results!
# print("Original: ", sentence)
# print("Pig Latin: ", piglatin)
food = "PIZZA"
print(food[:2])