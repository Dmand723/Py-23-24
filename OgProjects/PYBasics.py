import time
import os 
import sys
hi = bool
hi = True

list1 = []
x = 1
y = "2"
list1.append(x)
list1.append(y)
print(list1)

def second(seconds):
    print(seconds)
    while True:
        if seconds == 0:
           hi = False
           os.system("shutdown /s /t 1")

        else:
            seconds -= 1
            time.sleep(1)
            print(seconds)



def howoldareyou():
    question = input("how old are you ") 
    question = int(question)
    if question <= 15 and not 12:
    
        print("Little young baby") 
    elif question == 12:
        print("Self Destruct in")
        second(3)
        hi = False
    else:
        print("good job you aren't stupid")


def whatIsYourName():
    name = input("what is your name? ")
    name = str(name)
    print("Hello "+name)
    howoldareyou()
while hi == True:
    
    whatIsYourName()

    
