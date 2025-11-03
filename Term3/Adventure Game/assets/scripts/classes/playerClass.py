from assets.scripts.settings import *
from os import walk

class Player(pg.sprite.Sprite):
    def __init__(self,pos,imgPath,game,name):
        super(Player,self).__init__()

        self.goingDown = False
        self.goingUp = False
        self.goingRight = False
        self.goingLeft = False

        self.importAssets(imgPath)
        self.name = name
        self.game = game
        self.frameIndex = 0
        self.status = "down"
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
        
        curAnitmation = self.animaions[self.status]
        self.frameIndex += 15*dt
        if self.frameIndex >= len(curAnitmation):
            self.frameIndex = 0
        self.image = curAnitmation[int(self.frameIndex)]

    def getStatus(self):
        keys = pg.key.get_pressed()
        
        if self.dir.x == 0 and self.dir.y == 0:
            self.frameIndex = 0

        if self.goingLeft and not self.goingDown and not self.goingUp:#1
            self.status = "left"
        elif self.goingLeft  and self.goingDown:#2
            self.status = "left_down"
        elif self.goingDown and not self.goingLeft and not self.goingRight:#3
            self.status = "down"

        if self.goingLeft and not self.goingUp and not self.goingDown:#4
            self.status = "left"
        elif self.goingLeft and self.goingUp:#5
            self.status = "left_up"
        elif self.goingUp and not self.goingLeft and not self.goingRight:#6
            self.status = "up"
        
        if self.goingRight and not self.goingDown and not self.goingUp:#7
            self.status = "right"
        elif self.goingRight and self.goingDown:#8
            self.status = "right_down"
        elif self.goingDown and not self.goingRight and not self.goingLeft:#9
            self.status = "down"

        if self.goingRight and not self.goingUp and not self.goingDown:#10
            self.status = "right"
        elif self.goingRight and self.goingUp:#11
            self.status = "right_up"
        elif self.goingUp and not self.goingRight and not self.goingLeft:#12
            self.status = "up"

        # if self.attacking:
        #     self.status = self.status.split("_")[0]+"_attack"
        #     if self.frameIndex >= len(self.animaions[self.status])-1:
        #         self.attacking = False

    
    def switchStatus(self,status):
        self.status = status
        

    
    
    def getInputs(self):
        keys = pg.key.get_pressed()

        #movement===========================================

        


        if keys[pg.K_LEFT] or keys[pg.K_a]:#left
            self.dir.x = -1
            self.goingLeft = True
            self.goingRight = False
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:#right
            self.dir.x = 1
            self.goingRight = True
            self.goingLeft = False
            
                
        else:
            self.dir.x = 0
            self.goingLeft = False
            self.goingRight = False
            
        if keys[pg.K_UP] or keys[pg.K_w]:#up
            self.dir.y = -1
            self.goingUp = True
            self.goingDown = False
            
                
        elif keys[pg.K_DOWN] or keys[pg.K_s]:#down
            self.dir.y = 1
            self.goingDown = True
            self.goingUp = False
           
           
            
        else:
            self.dir.y = 0
            self.goingDown = False
            self.goingUp = False

        if keys[pg.K_a]!=True and keys[pg.K_LEFT]!=True:
            self.goingLeft = False
        if keys[pg.K_d]!=True and keys[pg.K_RIGHT]!=True:
            self.goingRight = False
        if keys[pg.K_s]!=True and keys[pg.K_DOWN]!=True:
            self.goingDown = False
        if keys[pg.K_w]!=True and keys[pg.K_UP]!=True:
            self.goingUp = False

        

        #====================================================

        #Shooting============================================
        if keys[pg.K_SPACE] or pg.mouse.get_pressed()[0]:
            self.attacking = True
            self.dir = vec(0,0)
            self.frameIndex = 0
        #====================================================

    def resetMove(self):
        self.dir = vec(0,0)

    def update(self,dt):
        self.getStatus()
        
        
        self.animate(dt)

    def curPlayerUpdate(self,dt):
        self.move(dt)
        self.getInputs()
        
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


