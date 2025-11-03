from assests.scripts.settings import *
from assests.scripts.classes.controllerClass import Controler
from assests.scripts.classes.gameObjectClass import Game_Object
from assests.scripts.classes.playerClass import Player



class SlimeGame():
    def __init__(self):
        self.isplaying = True
        pg.init()
        pg.mixer.init()
        pg.joystick.init()
        #setup the controller
        self.controllerList = []
        self.joyCount = pg.joystick.get_count()
        if self.joyCount > 0:
            for i in range(self.joyCount):
                self.controllerList.append(Controler(i))
        
        #set up window 
        self.gameWindow = pg.display.set_mode((WIDTH,HEIGHT))

        #setup clock
        self.clock = pg.time.Clock()
        #setup objects
        self.map = Game_Object(0,0,WIDTH,HEIGHT,"assests/imgs/maps/background.png")
        
        self.players = []
        for i in range(self.joyCount):
            player = Player(WIDTH/2,HEIGHT/2,TILE_SIZE[0],TILE_SIZE[1],"assests/imgs/player.png",5)
            self.players.append(player)
            
        

    
    def mainLoop(self):
        while self.isplaying:
            #tick Clock
            self.clock.tick(FPS)
            #event frame 
            self.getGameEvents()
            #update frame
            self.update()
            #draw frame
            self.draw()
    
    def getGameEvents(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.isplaying = False

            self.joyValues = []
            self.dpadValues = []
            self.bttnValues = [] 
            for i in range(len(self.players)):
                self.joyValues.append(self.controllerList[i].getAxes())
                self.dpadValues.append(self.controllerList[i].getDpad())
                self.bttnValues.append(self.controllerList[i].getButtons())

            

    def update(self):
        #player movement
        for i in range(len(self.players)):
            if self.joyValues[i].get("LJOY_X") != 0 or self.joyValues[i].get("LJOY_Y") != 0:
                self.players[i].changeDir((self.joyValues[i].get("LJOY_X")),(self.joyValues[i].get("LJOY_Y")))
            self.players[i].update()

    def draw(self):
        self.gameWindow.fill(green) 
        self.map.draw(self.gameWindow)
        for i in range(len(self.players)):
            self.players[i].draw(self.gameWindow)


        # update display last
        pg.display.update()

    def startScreen(self):
        print("start")
        
    def endScreen(self):
        return "END"