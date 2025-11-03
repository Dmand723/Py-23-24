from assets.scripts.settings import *







class Game(object):
    def __init__(self):
        print("The game was created")
        self.root = Tk()
        self.root_setup()
        self.loadImgs()
        self.loadData()
        self.setupGame()
        self.createWidgits()
        self.updateDisplay()
    
    def setupGame(self):
        self.trys = -1
        diff = self.diffSelector.get()
        print(diff)
        if diff == "Easy":
            x = random.randint(0,len(self.easyWords))
            self.word = self.easyWords[x]
            self.hint = self.easyHints[x]
        elif diff == "Medium":
            x = random.randint(0,len(self.medWords))
            self.word = self.medWords[x]
            self.hint = self.medHints[x]
        else:
            x = random.randint(0,len(self.hardWords))
            self.word = self.hardWords[x]
            self.hint = self.hardHints[x]
        self.guess = ""
        self.wordSoFar = "_"*len(self.word)
        
    def updateDisplay(self):
        self.trys +=1
        self.display.config(image=self.imgList[self.trys])

    def loadImgs(self):
        location = "assets/imgs/"
        names = []
        self.imgList = []
        for i in range(9):
            x = str.format("frame{}.png", i)
            names.append(location+x)
        self.imgList = []
        for name in names:
            self.imgList.append(PhotoImage(file=name))

    def createWidgits(self):
        self.window = Frame(self.root)
        self.window.config(width=1920, height=1080)
        self.createHintLbl()
        self.createDisplay()
        self.createBttnList()
        self.createDiffSelector()
        self.createWordFrame()
        self.createExitBttn()
        self.window.pack()

    def createExitBttn(self):
        self.exitBttnFrame = Frame(self.root, padx=10,pady=10, bg="Light blue")
        self.exitBttnFrame.place(x=0,y=0)
        self.exitBttn = Button(self.exitBttnFrame,text="Exit?",command=self.exitFtn)
        self.exitBttn.grid(row=0,column=0)
    
    def exitFtn(self):
        question = messagebox.askyesno("Exit Game?", "Are You Sure" )
        if question:
            self.root.destroy()
        else:
            self.noFnt()
    def noFnt(self):
        question = messagebox.askyesno("Exit Game?", "You Clicked Exit Now Exit" )
        if question:
            self.root.destroy()
        else:
            self.noFnt()

    def createHintLbl(self):
        self.hintLbl = Label(self.window,text=self.hint)
        self.hintLbl.grid(row=0, column=0,columnspan=2,sticky=W, padx=5, pady=5, ipadx=5, ipady=5)
        
    def updateWord(self):
        for i in range(len(self.wordSoFar)):
            self.lettersList[i].config(text = self.wordSoFar[i])

    def createDiffSelector(self):
        self.diffValues = ["Easy", "Medium", "Hard"]
        self.diffSelector = ttk.Combobox(self.window,values=self.diffValues)
        self.diffSelector.current(0)
        self.diffSelector.grid(row=0, column=2,columnspan=1,sticky=W, padx=5, pady=5, ipadx=5, ipady=5)
        

    def createDisplay(self):
        self.display = Label(self.window,image=self.imgList[0])
        self.display.grid(row=1, column=0,columnspan=3,sticky=NSEW, padx=5, pady=5, ipadx=5, ipady=5)
        
    def guessLetter(self,id):
        self.bttnList[id].config(state=DISABLED)
        self.guees = self.letters[id]
        print(id)
        if self.guees.upper() in self.word.upper():
            print(True)
           
            temp = ""
            for i in range(len(self.word)):
                if self.guees.upper() == self.word[i].upper():
                    temp += self.word[i]
                else:
                    temp+=self.wordSoFar[i]
            self.wordSoFar = temp
            self.updateWord()
        else:
            if self.trys < len(self.imgList-1):
                self.updateDisplay()
            else:
                answer = messagebox.askyesno("Game Over","Would you like to play again")
                if answer:
                    pass
                #call setup game 
                else:
                    self.root.destroy
            print(False)
     
    def createBttnList(self):
        self.bttnList = []
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.bttnFrame = Frame(self.window)
        row = 0
        col = 0
        index = 0
        for letter in self.letters:
            x = Button(self.bttnFrame,text=letter,command=lambda id=index:self.guessLetter(id))
            x.grid(row=row, column=col, padx=3, pady=3, ipadx=3, ipady=3)
            self.bttnList.append(x)
            col+=1
            index +=1
            if col >12:
                row+= 1
                col = 0
        self.bttnFrame.grid(row=3, column=0,columnspan=2,sticky=NSEW, padx=5, pady=5, ipadx=5, ipady=5)

    def createWordFrame(self):
        self.wordFrame = Frame(self.window)
        self.lettersList = []
        for letter in  self.wordSoFar:
            self.lettersList.append(Label(self.wordFrame, text="_", padx=10,pady=10).pack(side=LEFT))
        self.wordFrame.grid(row=2, column=0,columnspan=2,sticky=NSEW, padx=5, ipadx=5, ipady=7)

    def root_setup(self):
        self.root.geometry(geoString)
        self.root.title(TITLE)
        self.root.resizable(False,False)
        self.root.config(bg= "light blue")
        self.root.iconbitmap(ICON_PATH)
        self.root.attributes('-fullscreen',True)

    def loadData(self):
        try:
            file = open("assets/text/words.txt","r")
        except:
            messagebox.showerror("Error","Could Not Load File")

        tempList = file.readlines()
        file.close()
        cleanList = []
        wordList = []
        hintList = []
        for e in tempList:
            e.strip("\n")
            cleanList.append(e.strip("\n"))
        for daddy in cleanList:
            word,hint = daddy.split(";",2)
            wordList.append(word)
            hintList.append(hint)
        self.easyWords = []
        self.easyHints = []
        self.medWords = []
        self.medHints = []
        self.hardWords =[]
        self.hardHints = []
        for mommy in range(len(wordList)):
            if len(wordList[mommy]) <=4:
                self.easyWords.append(wordList[mommy])
                self.easyHints.append(hintList[mommy])
            elif len(wordList[mommy]) <=8:
                self.medWords.append(wordList[mommy])
                self.medHints.append(hintList[mommy])
            else:
                self.hardWords.append(wordList[mommy])
                self.hardHints.append(hintList[mommy])
        
    def play(self):
        self.root.mainloop()