from assets.scripts.settings import *
from assets.scripts.classes.playerClass import Player
from assets.scripts.classes.screenTextClass import ScreenText
from assets.scripts.classes.stories.story1 import Story1
from assets.scripts.classes.gameObjectClass import Game_Object
from assets.scripts.classes.spriteGroups import AllSprites



class Game():
    def __init__(self,playenames):

        self.isPlaying = True
        
        self.playerNames = playenames
        self.players = pg.sprite.Group()
        self.allsprties = AllSprites()
        self.playerList = []
        self.playersDict = {}
        x = 0
        for i in range(len(playenames)):
            player = Player(spawnPos[0],"assets/sprites/player",self,playenames[i-1])
            self.players.add(player)
            self.allsprties.add(player)
            self.playerList.append(player)
            self.playersDict[player.name] = player
            x +=1 
        self.playerCount = len(self.players)
        self.textTyped = []
        self.curentText = ""
        self.nextText = ""
        self.curPlayerInt = 0
        self.curPlayer = self.playerList[self.curPlayerInt]
        pg.init()
        pg.mixer.init()

    def gameSetup(self):
        # setup pg window
        self.gameWindow = pg.display.set_mode((WIDTH,HEIGHT))
        
        #setup clock
        self.gameClock = pg.time.Clock()

        #setup screen writer
        self.screenWriter = ScreenText(fontsize=25,color=green)

        #start background music
        pg.mixer.music.load('assets/sounds/bg.mp3')
        pg.mixer.music.play(-1)       

         

    def mainloop(self):

        while self.isPlaying:
            #tick clock
            self.gameClock.tick(FPS)
            #Check for events 
            self.getGameEvents()
            #update frame
            self.update()
            #draw frame
            self.draw()
    
    def getGameEvents(self):
        
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.isPlaying = False
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:
                    self.isPlaying = False
            if event.type == pg.KEYUP:
                if event.key == pg.K_p:
                    print("?")
                    self.switchPlayer()

        # keysDown =pg.key.get_pressed()
        # if keysDown[pg.K_w]:#moves player up
        #     self.curPlayer.changeDirY(-1)
        # elif keysDown[pg.K_s]:#moves player down
        #     self.curPlayer.changeDirY(1)
        # else: #resets players move y
        #     self.curPlayer.changeDirY(0)

        # if keysDown[pg.K_a]:#moves player left
        #     self.curPlayer.changeDirX(-1)
        # elif keysDown[pg.K_d]:#moves player right
        #     self.curPlayer.changeDirX(1)
        # else: #resets players move x
        #     self.curPlayer.changeDirX(0)
        
        # if self.curPlayer.name.lower() == "devdman" and keysDown[pg.K_7] :
        #     if keysDown[pg.K_2]:
        #         if keysDown[pg.K_3]:
        #             #this is useless
        #             self.curPlayer.devMode = True

    def switchPlayer(self,id = None):#Switches curent player 
        self.curPlayer.resetMove()
        if id == None:#if no id was passed in it will just go to the next player
            if self.curPlayerInt == self.playerCount -1:
                self.curPlayerInt = 0
            else:
                self.curPlayerInt += 1
        else:
            self.curentText = id
        self.curPlayer = self.playerList[self.curPlayerInt]
        print(self.curPlayer.name,self.playerCount)

    def update(self):
        self.dt = self.gameClock.tick(FPS)/1000
        self.curPlayer.update(self.dt)

    def draw(self):
        self.gameWindow.fill(pink)
        self.drawToScreen()
        
        #Draw players and have curent player draw on top 
        self.allsprties.customDraw(self.curPlayer)
        # for i in range(len(self.players)):
        #     if i == self.curPlayerInt:
        #         pass
        #     else:
        #         self.players[i].draw(self.gameWindow)



        # update display last
        pg.display.update()
    

    def setNewText(self,text):
        self.curentText = ''
        self.text = ''
        self.textTyped.clear()
        for char in text:
            self.curentText = self.curentText + char
        
            
    
    def drawToScreen(self):
        pass



    def endScreen(self):
        return "END"