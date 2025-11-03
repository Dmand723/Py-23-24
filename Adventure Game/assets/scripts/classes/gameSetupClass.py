from assets.scripts.settings import *
from assets.scripts.classes.playerClass import Player
from assets.scripts.classes.screenTextClass import ScreenText
import pygame as pg

class Setup():
    def __init__(self) -> None:
        pg.init()
        print(PATHS["player"])
        self.isPlaying = True
        self.playerCount = 0
        self.players = []
        self.playerNames = []
        self.playersDict = {}
        self.textTyped = []
        self.curentText = ""
        self.nextText = ""
        self.numList = ['1','2','3','4','5','6','7','8','9','0',1,2,3,4,5,6,7,8,9,0]
        self.curPlayerInt = 0

    def checkNum(self):
        events = pg.event.get()
        self.maxPlayerNumList = ['1','2','3','4',1,2,3,4]
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
            if event.type == pg.KEYDOWN:
                self.gameWindow.fill(black)
                typed = event.unicode
                print(typed)
                if event.key == pg.K_BACKSPACE:
                    
                    if not len(self.textTyped) <= 0:
                        print(self.textTyped)
                        self.textTyped.pop()
                        print(self.textTyped)
                        self.text = "".join(self.textTyped)
                        self.screenWriter.reset()
                        self.screenWriter.printToScreen(self.gameWindow,"{} : {}".format(self.curentText,self.text))
                        pg.display.update()
                if typed in self.maxPlayerNumList:
                    print("?")
                    self.textTyped.append(typed)
                    self.text = "".join(self.textTyped)
                    self.screenWriter.reset()
                    self.screenWriter.printToScreen(self.gameWindow,"{} : {}".format(self.curentText,self.text))
                    pg.display.update()
                    print(self.text)
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.start1 = False
                    print("t", self.text)
                    tInt = int(self.text)
                    self.playerCount = tInt
                    self.screenWriter.reset()
                    self.gameWindow.fill(black)
                    self.textTyped.clear()
                    self.text = ''
                    
                    


    def checkTyping(self): #Checks for typig of players name and creates players
        self.gameWindow.fill(black)
        events = pg.event.get()
        self.charList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                self.gameWindow.fill(black)
                typed = event.unicode
                print(typed)
                if event.key == pg.K_BACKSPACE:
                    
                    print("?")
                    if not len(self.textTyped) <= 0:
                        print(self.textTyped)
                        self.textTyped.pop()
                        print(self.textTyped)
                        self.text = "".join(self.textTyped)
                        self.screenWriter.reset()
                        self.screenWriter.printToScreen(self.gameWindow,"{}{}".format(self.curentText,self.text))
                        pg.display.update()
                if (typed.lower() in self.charList or typed in self.numList):
                    print("?")
                    self.textTyped.append(typed)
                    self.text = "".join(self.textTyped)
                    self.screenWriter.reset()
                    self.screenWriter.printToScreen(self.gameWindow,"{}{}".format(self.curentText,self.text))
                    pg.display.update()
                if event.key == pg.K_RETURN:
                    
                    playerName = self.text
                    self.playerNames.append(playerName)
                    
                    self.textTyped.clear()
                    self.text = ''
                    self.start2 = False
                    
    def setup(self):
        # setup pg window
        self.gameWindow = pg.display.set_mode((WIDTH,HEIGHT))
        
        #setup clock
        self.gameClock = pg.time.Clock()

        #setup screen writer
        self.screenWriter = ScreenText(fontsize=25,color=green)

        self.playerSetup()
            
                    

    def playerSetup(self):
        
        self.curentText = "How Many Players? (2-4)"
        self.start1 = True
        self.screenWriter.reset()
        self.screenWriter.printToScreen(self.gameWindow,"{} : {}".format(self.curentText,""))
        pg.display.update()
        while self.start1 == True:
            self.checkNum()
        
        for i in range(self.playerCount):
            self.screenWriter.reset()
            self.curentText = "Player {} : ".format(i+1)
            self.screenWriter.printToScreen(self.gameWindow,"{}{}".format(self.curentText,""))
            pg.display.update()
            self.start2 = True
            while self.start2:
                self.checkTyping()

    def drawToScreen(self):
        self.screenWriter.reset()
        self.screenWriter.printToScreen(self.gameWindow,"{} : {}".format(self.curentText, self.text))

    def getPlayers(self):
        return  self.playerNames