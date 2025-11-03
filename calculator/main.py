from assests.scripts.settings import *

answer = ''
root = ""
box = ''
buttonList = []
opList = []
numberList = []
calculated = False
clickSnd = ''
errorSnd = ''

def main():#Main runtime function 
    global root
    root = root_setup()
    createWigets()
    loadSounds()

    root.mainloop()

def createWigets():
    createTxtBox()
    createButtons()
    configBtns()
    

def createTxtBox():#Creates Entrybox
    global box
    box = Entry(root,justify=RIGHT)
    box.config(font="Helvetica 20 bold")
    box.pack(padx=5,pady=5,ipadx=5,ipady=5)
    box.insert(END,'0')
    numberList.insert(0,'0')
    box.config(state=DISABLED)

def createButtons():#Creates all buttons for the calcutor 
    butnFrame = Frame(root,bg = "black")
    butnFrame.pack()
    buttons = [
    '1', '2', '3', '/',   # Row 1
    '4', '5', '6', '*',   # Row 2
    '7', '8', '9', '-',   # Row 3
    '.' , '0', '(-)', '+',  # Row 4
    'ans','C', '='       # Row 5         
    ]
    row =0
    col = 0
    for b in buttons:
        x = Button(butnFrame,text=b ,font="Helvetica 20 bold",width=5,height=2,command=lambda buttonText=b: buttonCommand(buttonText),activebackground='gray')
        x.grid(column=col,row=row,padx=5,pady=5)
        col+=1
        if row != 4:
            if row == 4 and col==1:
                opList.append(x)
            else:
                if col >=4:
                    opList.append(x)
                else:
                    buttonList.append(x)
                if col >3:
                    col=0
                    row+=1
        else:
            opList.append(x)
        
       
def configBtns():#Configures negtive and op buttons
    for b in opList:
        b.config(bg= '#36cac6',activebackground = '#27a19e')
    opList[6].config(command=calculate,bg='#00fa3d',activebackground = '#00d434')
    opList[4].config(command=ansBtnCmd,bg="#ad03d6",activebackground="#7a0396")
    opList[5].config(command=clearCmd, bg="#007ad4",activebackground ="#005899")
    buttonList[11].config(command=negitiveCmd)

def negitiveCmd():#Comand for negitive button
    clickSnd.play()
    box.config(state=NORMAL)
    box.insert(0,'-')
    numberList.insert(0,'-')
    box.config(state=DISABLED)
    print(numberList)
    
def clearCmd():#Clears the enry box
    clickSnd.play()
    for b in buttonList:
            b.config(state=NORMAL)
    box.config(state=NORMAL)
    box.delete(0,END)
    box.insert(END,'0')
    box.config(state=DISABLED)
    numberList.clear()
    print(numberList)

def ansBtnCmd():#Puts prevous anwer in the entry box
    global calculated
    clickSnd.play()
    if answer == '':#Checks if there is a previous answer
        pass
    else:
        for b in buttonList:
            b.config(state=DISABLED)
        box.config(state=NORMAL)
        calculated = False
        box.delete(0,END)
        numberList.clear()
        box.insert(END,answer)
        numberList.append(str(answer))
    
    box.config(state=DISABLED)

def buttonCommand(id):#Add the number of the button you pressed to the eqation 
    global calculated
    global numberList
    clickSnd.play()
    box.config(state=NORMAL)
    opIdList = ['/','*','-','+','ans','=','C']
    if id in opIdList and box.get() == '':#Checks if there is nothing in the entrybox and does not let an oporator in the calculation
        try:
            if id not in numberList[1]:
                print("?????")
                numberList[1] = id
                print(numberList)
                return
            else:
                return
        except:
            return
    for b in buttonList:
            b.config(state=NORMAL)
    print(id)

    if calculated:
        if id not in opIdList:#Checks if the button pressed was an oporator and if so does not display it 
            box.delete(0,END)
            numberList.clear()
        calculated = False
    
    
    if str(id) in opIdList:#Clears the entry box if a oporator is clicked 
        box.delete(0,END)
        tempnslist = ["".join(numberList)]
        numberList = tempnslist
        numberList.append(id)
        
        
        print(numberList)
    else:
        if box.get() == '0':
            box.delete(0,END)
        box.insert(END,id)
        numberList.append(id)
        print(numberList)
    box.config(state=DISABLED)





    #Hi dawson I love you very much 
    #                    -Secret Admirer

def calculate():#Calculates and outputs answer
    global answer
    global calculated
    clickSnd.play()
    for b in buttonList:
            b.config(state=NORMAL)
    try:
        numberList[0] = "".join(numberList)
    except:
        errorCmd()
    box.config(state=NORMAL)
    try:
        answer = str(eval(numberList[0]))
        box.delete(0,END)
        box.insert(END, answer)
        numberList.clear()
        numberList.append(answer)
    except:
        errorCmd()
    print(answer)
    print(numberList)
    calculated = True
    box.config(state=DISABLED)

def root_setup():#Sers up main window
    root =Tk()
    root.geometry(geoString)
    root.config(bg = 'black')
    root.title(TITLE)
    root.iconbitmap(ICON_PATH)
    root.resizable(False,FALSE)
    return root

def errorCmd():#Runs when there is an error
    errorSnd.play()
    print('Error')
    box.config(state=NORMAL)
    box.delete(0,END)
    box.insert(END, "Error")
    box.config(state=DISABLED)

def loadSounds():
    pg.mixer.init()
    global clickSnd
    global errorSnd
    clickSnd = pg.mixer.Sound("assests/sounds/click.mp3")
    errorSnd = pg.mixer.Sound("assests/sounds/error.mp3")
main()