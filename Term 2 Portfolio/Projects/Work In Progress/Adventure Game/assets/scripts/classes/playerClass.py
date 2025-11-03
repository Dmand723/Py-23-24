from assets.scripts.settings import *
from os import walk

class Player(pg.sprite.Sprite):
    def __init__(self,pos,imgPath,game,name):
        super(Player,self).__init__()
        self.importAssets(imgPath)
        self.name = name
        self.game = game
        self.frameIndex = 0
        self.status = "down_idle"
        self.image = self.animaions[self.status][self.frameIndex]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.devMode = False

        #movement
        self.pos = vec(self.rect.center)
        self.dir = vec()
        self.speed =  500

        
        # collisons
        self.hitbox = self.rect.inflate(0,-self.rect.height/2)

        # attack
        self.attacking =False

    def importAssets(self,path):
        self.animaions = {}
        for i,folder in enumerate(walk(path)):
            if i == 0:
                for name in folder[1]:
                    self.animaions[name] = []
            else:
                for filename in sorted(folder[2],key = lambda string: int(string.split(".")[0])):
                    path = folder[0].replace("\\","/")+"/"+filename
                    surf =pg.image.load(path).convert_alpha()
                    key = path.split("/")[-2]
                    self.animaions[key].append(surf)
    
    def animate(self,dt):
        print("???")
        curAnitmation = self.animaions[self.status]
        self.frameIndex += 15*dt
        print(self.frameIndex)
        if self.frameIndex >= len(curAnitmation):
            self.frameIndex = 0
        self.image = curAnitmation[int(self.frameIndex)]

    def getStatus(self):
        if self.dir.x == 0 and self.dir.y == 0:
            self.status = self.status.split("_")[0]+"_idle"
        
        if self.attacking:
            self.status = self.status.split("_")[0]+"_attack"
            if self.frameIndex >= len(self.animaions[self.status])-1:
                self.attacking = False
                


    
    def getInputs(self):
        keys = pg.key.get_pressed()

        #movement===========================================
        if keys[pg.K_LEFT] or keys[pg.K_a]:#left
           self.dir.x = -1
           self.status = "left"
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:#right
            self.dir.x = 1
            self.status = "right"
        else:
            self.dir.x = 0
            
        if keys[pg.K_UP] or keys[pg.K_w]:#up
            self.dir.y = -1
            self.status = "up"
        elif keys[pg.K_DOWN] or keys[pg.K_s]:#down
           self.dir.y = 1
           self.status = "down"
        else:
            self.dir.y = 0
            
        #====================================================

        #Shooting============================================
        if keys[pg.K_SPACE] or pg.mouse.get_pressed()[0]:
            print("shoot")
            self.attacking = True
            self.dir = vec(0,0)
            self.frameIndex = 0
        #====================================================

    def resetMove(self):
        self.dir = vec(0,0)

    def update(self,dt):
        self.getInputs()
        self.getStatus()
        self.move(dt)
        self.animate(dt)
        
        
    def move(self,dt):
        #normalize direction===========================
        if self.dir.magnitude() != 0:
            self.dir.normalize()
        #==============================================

        #Horizontal Movement============================
        self.pos.x += self.dir.x * self.speed *dt
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx
        #===============================================

        #Horizontal Collisions==========================

        #===============================================

        #Vertical Movement============================
        self.pos.y += self.dir.y * self.speed *dt
        self.hitbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        #===============================================

        #Vertical Collisions==========================


# class Player(Game_Object):
#     def __init__(self, x, y, width, height, image_path,playername,speed,screen):
#         fixedX = x - width/2
#         fixedY = y - width/2
        
#         super().__init__(fixedX, fixedY, width, height, image_path)
#         self.curSpeed = speed
#         self.gamewindow = screen
#         self.name = playername
#         self.HP = 100
#         self.items = []
#         self.itemsAmount = []
#         self.moveDirX = 0
#         self.moveDiry = 0
#         self.sprintSpeed = speed*2
#         self.normalSpeed = speed
#         self.screenwriter = ScreenText(10,color=white)
#         self.devMode = False


#         print("hi", playername)
    
#     def changeDirX(self,x=0):
#         self.moveDirX = x
#     def changeDirY(self,y=0):
#         self.moveDiry = y
#     def resetMove(self): 
#         self.moveDiry = 0
#         self.moveDirX = 0

#     def update(self):
#         self.move()
#         self.displayName()

#     def displayName(self):
#         self.screenwriter.x = self.curX+2
#         self.screenwriter.y = self.curY+2
#         self.screenwriter.printToScreen(self.gamewindow,self.name)
        

#     def move(self):
#         if self.curX < 0:
#             self.curX = 0
#             return

#         if self.curX > WIDTH - TILE_SIZE[0]:
#             self.curX = WIDTH - TILE_SIZE[0]
#             return
#         if self.curY < 0:
#             self.curY = 0
#             return

#         if self.curY > HEIGHT - TILE_SIZE[0]:
#             self.curY = HEIGHT - TILE_SIZE[0]
#             return
#         self.curX += self.moveDirX *self.curSpeed

        
#         self.curY += self.moveDiry *self.curSpeed

#     def addHP(self,ammout):
#         self.HP += ammout

#     def removeHP(self,ammount):
#         self.HP -= ammount
    
#     def setHP(self,ammount):
#         self.HP = ammount
    
#     def giveItem(self,item):
#         if item not in self.items:
#             self.items.append(item)
#             self.itemsAmount.append(1)
#         else:
#             itemIndex = self.items.index(item)
#             self.itemsAmount[itemIndex] = self.itemsAmount[itemIndex]+1
    
#     def removeItem(self,item):
#         if item not in self.items:
#             pass
#         else:
#             itemIndex = self.items.index(item)
#             self.itemsAmount[itemIndex] = self.itemsAmount[itemIndex] -1
#             if self.itemsAmount[itemIndex] <= 0:
#                 self.items.remove(item)
#                 self.itemsAmount.remove(itemIndex)
    
    






#     def say(self,message):
#         print("{} says {}".format(self.name,message))



