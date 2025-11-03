from assests.scripts.classes.gameObjectClass import Game_Object
from assests.scripts.settings import *

class Player(Game_Object):
    def __init__(self, x, y, width, height, image_path,speed):#VS code wrote this for me :)
        fixedX = x - width/2
        fixedY = y - width/2

        super(Player,self).__init__(fixedX, fixedY, width, height, image_path)
        self.lives = 3
        self.speed = speed
        self.score = 0
        self.moveDirX = 0
        self.moveDiry = 0
        self.sprintSpeed = speed*2
        self.normalSpeed = speed
        self.stamana = 100
        self.HP = 100

    def update(self):
        self.move()

    def move(self):
        if self.curX < 0:
            self.curX = 0
            return

        if self.curX > WIDTH - TILE_SIZE[0] - TILE_SIZE[0]:
            self.curX = WIDTH - TILE_SIZE[0]  - TILE_SIZE[0]
            return
        if self.curY < 0:
            self.curY = 0
            return

        if self.curY > HEIGHT - TILE_SIZE[0]:
            self.curY = HEIGHT - TILE_SIZE[0]
            return
        self.curX += self.moveDirX *self.speed

        
        self.curY += self.moveDiry *self.speed

    def changeDir(self,x=0,y=0):
        self.moveDirX = x
        self.moveDiry = y

    def collect(self):
        pass

    def sprint(walk):
        pass

    def die(self):
        pass

    def addScore(self,amount):
        self.score += amount

    def addLife(self, amount = 1):
        self.lives += amount

    def takeLife(self,amount = 1):
        self.lives -=amount
    
    def takeDamage(self,amount):
        self.HP -= amount
    
    def addHP(self,amount):
        self.HP += amount

    def useStamina(self,amount):
        self.stamana -= amount

    def asdStamina(self,amount):
        self.stamana += amount