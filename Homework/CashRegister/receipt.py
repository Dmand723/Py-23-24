 Dawson Simmons  
 Cash Register Assiment 

 Declare vars
numItems = 4
costPerItem = 10.00
taxRate = 0.08

def calculate():
    subTotal = costPerItem*numItems
    taxAmount = subTotal*taxRate
    totalPrice = subTotal+taxAmount

    strTotal = str(totalPrice)
    strtax = str(taxAmount)

    return strtax, strTotal

def main():
    taxAmount, totalPrice = calculate()
    print("SALES RECEIPT")
    print("Number of items  : "+str(numItems))
    print("Cost per item    : $"+str(costPerItem))
    print("Tax rate         : "+str(taxRate))
    print("Tax amount       : $"+taxAmount)
    print("TOTAL SALE PRICE : $"+totalPrice)

main()