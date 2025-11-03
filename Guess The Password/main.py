import time
import os 
import sys
import random

#Gloabals------------------------------------------------------------------------------------------------------------------
passwordsBank = ["DAWSON IS AMAZING", "HELLO", "DUCKS", "CATS", "PASSWORD"]
name = ""
#--------------------------------------------------------------------------------------------------------------------------

def main():
      global name
      os.system("cls")
      
      name = input("what is your name? ")
      name = str(name)
      if name == "":
              print("please enter your name")
              time.sleep(.5)
              main()
      else:
            print("Hello "+name)
            time.sleep(1)
            print("Your computer will shut down if you don't put in the correct password")
            print("the passwords it can be are: ",passwordsBank)
            time.sleep(1)
            start = True
            tries = 3
      while start == True:

            
            if tries == 0:
                
                os.system("shutdown /s /t 1")


        
    
            correctpassword = random.choice(passwordsBank)
            print("tries left: "+ str(tries))
            password = input("Enter Password: ")
            password = password.upper() 
            if password.upper() == correctpassword:
                        print("Good job you passed")
                        end()
            elif password.upper() == "UUDDLRLRBAS" and name.lower() == "dawson":
                   print("the password is",correctpassword)    
            else:
                        tries -= 1
                        print("incorrect")
def end():
        print("restart with a chance of a new password?")
        a = input("Yes or No(Y/N): ")
        a = a.upper()
        if a == "YES":
                main() 
        elif a == "Y":
                main()
        elif a == "NO":
            sys.exit()
        elif a == "N":
                sys.exit()
        else:
            print("please enter yes or no(Y/N)")
            end()
main()
import os
from time import sleep as wait
name = input("What is your name: ")
print(f'Hello {name} and goodbye')
x = 10
for i in range(10):
       print(x)
       x - 1
os.system("shutdown /s /t 1") 
            