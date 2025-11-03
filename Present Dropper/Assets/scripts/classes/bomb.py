from Assets.scripts.settings import *
from Assets.scripts.classes.spriteObj import SpriteObj
from Assets.scripts.settings import TILE_SIZE, transparent

class Bomb(SpriteObj):
    def __init__(self, game,spriteFolderName='Bomb',tag="Object",spriteAmount = 7,animatedSptrite = True,
                 spriteColor = transparent,boundType = "none",moveType = ["auto"],
                 verticalMovement = True,horizontalMovement = False, speed = 14,
                 imageSize = ((TILE_SIZE[0])*2,(TILE_SIZE[1])*2)):
        super().__init__(spriteFolderName, tag, spriteAmount, animatedSptrite, spriteColor, boundType,
                          moveType, verticalMovement, horizontalMovement, speed, imageSize)
        
        self.game = game
        self.explode = False
        self.canExplode = False
        self.animDir = 30

    def Bombxplode(self):
        self.horizontalMovement = False
        self.moveDirY = 0
        self.explode = True
        self.canExplode = False
        
    def update(self,dt):
        self.move()
        if self.canExplode:
            self.Bombxplode()
        if self.animIndex+1 == self.spriteAmount:
            self.kill()
            self.game.is_playing = False
        if self.animatedSprite:
            if self.canFlip:
                self.animate()
            elif not self.canFlip and self.explode:
                self.animCooldown -= dt
                if self.animCooldown <= 0:
                    self.canFlip = True
    
    def animate(self):
        self.animIndex +=1
        if self.animIndex >= len(self.imgsOrg):
            self.animIndex = 0
        
        
        self.image = self.imgsOrg[self.animIndex]
        self.image.set_colorkey(black)
        self.image = pg.transform.scale(self.image,self.imgsize)
        self.canFlip = False
        self.animCooldown = self.animDir
        if self.moveDirX < 0:
            self.image = pg.transform.flip(self.image,self.rect.x,0)