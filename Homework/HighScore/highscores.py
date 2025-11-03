 set names to names value
names = ["Dawson", "Paps", "AAA"]
 set score to scores value
scores = ["1000000", "500", "400"]

 combine names and scores
s = 0
print("High Scores")
print("--------------")
for name in names:
    highScore = str.format("{} = {}", name, scores[s])
    s+=1
    print(highScore)