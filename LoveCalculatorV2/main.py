from assests.scripts.settings import *


#gloabals
results = []
precents = []
root = ""

def newMain():
    root_setup()
    createWidgets()


    root.mainloop()


def root_setup():#Setup and Create root window
    global root
    root = Tk()
    root.title(TITLE)
    root.resizable(False,False)
    root.config(bg= BG_COLOR)
    root.iconbitmap(ICON_PATH)
    root.attributes('-fullscreen',True)


def createWidgets():#Create widgets on root window 
    createTextBox()
    createExitBtn()

def createExitBtn():
    exit = Button(root,text="Exit Game",command=exitFtn)
    exit.grid(row=0,column=0,padx=5,pady=5)

def exitFtn():
    answer = messagebox.askyesno("Exit","Are You Sure You Want To Exit?")
    if answer:
        sys.exit()
    else:
        pass

def createTextBox():
    textBox = Label(root,text="Hello you are amazing", font="consolas 40 bold",justify=CENTER,background=TEXT_BG_COLOR)
    textBox.grid(row=5,column=2,sticky=S)

















def main():
    #root_setup()
    loadData()
    game()
    end()
       
def game():
    global results
    global precents
    
    calculating = False
    print("Hello welcome to my love calculator")
    time.sleep(1)
    name1 = input("Name 1: ")
    name2 = input("Name 2: ")
    print("Calculating")
    calculating = True
    secconds = 0
    while calculating == True:
        secconds += 1
        print(str(secconds) + "%")
        time.sleep(.01)
        if secconds == 100:
            calculating = False
            result(name1, name2, results, precents)
            

def result(n1,n2,r1,p1):
    global results
    global precents
    results = r1
    precents = p1
    compatibilty = str(random.randrange(0, 100))
    check = (n1+n2).lower()
    if check in results:
       resultprecent = results.index(check)
       compatibilty = precents[resultprecent]
    print(n1 + " + " + n2 + " Compatiblity " +str(compatibilty)+"%")
    tempR = check+";"+n2+n1
    tempP = compatibilty+";"+compatibilty
    saveData(check,compatibilty,tempR,tempP)
    

    
def end():
    a = input("again?(Y/N): ")
    a = a.upper()
    if a == "YES":
        os.system("cls")
        main()
    elif a == "Y":
        os.system("cls")
        main()
    elif a == "NO":
        sys.exit()
    elif a == "N":
        sys.exit()
    else:
        print("Please enter yes or no")
        end()


def saveData(check, comp,tempR,tempP):
    global results
    global precents
    
    if not check in results:
        results.append(tempR)
        precents.append(tempP)
        results,precents = compressList()
        fileP = open("assests/text/precentsLC.txt","w")
        fileP.write(precents)
        fileP.close()
        fileR = open("assests/text/resultsLC.txt","w")
        fileR.write(results)
        fileR.close()

def compressList():
    tempR = ";".join(results)
    tempP = ";".join(precents)
    return tempR,tempP


def loadData():
    global results
    global precents
    try:
        fileP = open("assests/text/precentsLC.txt","r")
    except:
        fileP = open("assests/text/precentsLC.txt","w")
        fileP.write("100;100")
        fileP.close()
        fileP = open("assests/text/precentsLC.txt","r")
    try:
        fileR = open("assests/text/resultsLC.txt","r")
    except:
        fileR = open("assests/text/resultsLC.txt","w+")
        fileR.write("dawsonsam;samdawson")
        fileR.close()
        fileR = open("assests/text/resultsLC.txt","r")
    precents = fileP.read()
    fileP.close()
    results = fileR.read()
    fileR.close()
    precents =precents.split(";")
    results = results.split(";")



newMain()