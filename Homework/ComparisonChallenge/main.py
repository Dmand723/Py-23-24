savings = int(input("How much do you have in savings? : "))
gameCost = int(input("How much does the game cost? : "))
posterCost = int(input("How much does the poster cost? : "))

# Predictions
print("is Cost Equal :", gameCost == posterCost)       #gameCost is not equal to posterCost)
print("is Cost Different :", gameCost != posterCost)    #gameCost is different from posterCost)
print("is Poster More :", gameCost < posterCost)        #gameCost is not less than posterCost)
print("is Game More :", gameCost > posterCost)          #gameCost is greater than posterCost)
print("can Buy Game :", gameCost <= savings)            #gameCost is not less than or equal to savings)
print("can Buy Poster :", savings >= posterCost)        #savings are greater than or equal to posterCost)
print("can Buy Game and Poster:", gameCost+posterCost <= savings ) #game cost and poster cost is less or equal to savings