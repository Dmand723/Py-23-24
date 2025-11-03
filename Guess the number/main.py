from assets.scripts.settings import *
           
            
            
#Globals-----------------------------------------------------------------------------------------------------------------
labelList = []
radioBttnList = []
widgetsList = []
diff = ""
low = 0
high = 100
window =""
logoImage = ""
root =""
rbValueList = ""

#------------------------------------------------------------------------------------------------------------------------

#Funtions----------------------------------------------------------------------------------------------------------------
def root_setup():#Setup The Root
    global root
    # Create an instamce of tkinter window
    root = Tk()
    root.title(TITLE)
    root.iconbitmap(ICON_PATH)
    # root.maxsize(WIDTH, HEIGHT)
    # root.minsize(WIDTH,HEIGHT)
    # root.resizable(False,False)
    
    
    # Define the geomotry of the window 
    root.geometry(geoString)
    # set the backgroud color
    root.configure(background='dark gray',)
    return root

def createMainWindow():
    pass

def createTextOutput():
    pass

def createWidgets(root):#Create widgets on screen 
    global labelList
    global diff
    global radioBttnList
    global widgetsList
    global window
    global logoImage
    
    logoImage = PhotoImage(file=IMAGE_PATH)
    resized = logoImage.subsample(x=5,y=5)
    lblFont = font.Font(family="Courier",size=30,weight="bold")
  
    window = Frame(root, background="gray")
    radio_bttn_frame = Frame(window,width=200)
    textList = ["lives", "<", ">", "Low", "High", "Img"]
    for t in textList:
        labelList.append(Label(window, text=t, font = lblFont,width=9))

    labelList[-1].config(image = logoImage)
    
    rbValueList = ["Easy","Medium", "Hard", "I am a GOD"]
    diff = StringVar(window, rbValueList[0])
    for v in rbValueList:
        radioBttnList.append(Radiobutton(radio_bttn_frame,text=v,variable=diff,value=v, font=lblFont))
    guessBttn = Button(window, text= "GUESS ?",font=lblFont)
    numberSb = Spinbox(window, from_=low, to= high,justify=CENTER, width=5 )
    output = Entry(window)
    
    widgetsList.append(output)
    widgetsList.append(numberSb)
    widgetsList.append(guessBttn)
    widgetsList.append(radioBttnList)
    widgetsList.append(labelList)


    window.pack()
    radio_bttn_frame.grid(row=0,column=0,sticky=NSEW,padx=5,pady=5,ipadx=5,ipady=5)
    x=0
    for rb in widgetsList[3]:
        rb.grid(row=x,column=0,sticky=NW)
        x+=1
    widgetsList[4][5].grid(row=0,column=1,columnspan=3,sticky=NSEW,padx=5,pady=5,ipadx=5,ipady=5)
    widgetsList[4][0].grid(row=0, column=4, sticky=NSEW,padx=5,pady=5,ipadx=5,ipady=5)
    # row 1 setup
    widgetsList[4][3].grid(row=1,column=0,sticky=NSEW,padx=5,pady=5,ipadx=5,ipady=5)
    widgetsList[4][1].grid(row=1, column=1, sticky=NSEW, padx=5, pady=5, ipadx=5, ipady=5)
    widgetsList[1].grid(row=1,column=2,sticky=NSEW,padx=5,pady=5,ipadx=5,ipady=5)
    widgetsList[4][2].grid(row=1, column=3, sticky=NSEW, padx=5, pady=5, ipadx=5, ipady=5)
    widgetsList[4][4].grid(row=1, column=4, sticky=NSEW, padx=5, pady=5, ipadx=5, ipady=5)
    # row 2 setup
    widgetsList[2].grid(row=2, column=2, sticky=NSEW, padx=5, pady=5, ipadx=5, ipady=5)
    # row 3 set up
    widgetsList[0].grid(row=3,column=0,columnspan=5,sticky=NSEW,padx=5,pady=5,ipadx=5,ipady=5)
    
def gameSetup():
    lives = ""
    high = ""
    low = ""
    number = ""
    guess = ""

    if diff.get() == rbValueList[0]:
        lives = 10
        high = 25
        low = 1
    
    if diff.get() == rbValueList[1]:
        lives = 5
        high = 150
        low = 1

    if diff.get() == rbValueList[2]:
        lives = 3
        high = 200
        low = 1
    
    if diff.get() == rbValueList[3]:
        lives = 1
        high = 10000
        low = 1


    number = random.randint(low,high)
    guess = 0


    return lives, high,low,number,guess

def placeWidgets():
    pass

def main():#Main Runtime Function
    root = root_setup()
    createWidgets(root) 
    root.mainloop()
   


   
    



#--------------------------------------------------------------------------------------------------------------------------
main()