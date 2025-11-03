from Assets.scripts.settings import *
from os import walk
from Assets.scripts.classes.spriteObj import SpriteObj

class Player(pg.sprite.Sprite):
    def __init__(self,pos,groups,imgPath,game):
        super(Player,self).__init__(groups)
        self.importAssets(imgPath)
        self.frameIndex = 0
        self.status = "down_idle"
        self.image = self.animaions[self.status][self.frameIndex]
        self.rect = self.image.get_rect()
        self.rect.center = pos

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