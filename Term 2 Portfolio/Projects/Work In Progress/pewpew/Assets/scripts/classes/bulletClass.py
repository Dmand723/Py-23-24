from Assets.scripts.settings import *
from Assets.scripts.classes.spriteObj import SpriteObj
from Assets.scripts.settings import TILE_SIZE, transparent

class bullet(SpriteObj):
    def __init__(self,spriteFolderName='',tag="Object",spriteAmount = 1,animatedSptrite = False,
                 spriteColor = transparent,boundType = "solid",moveType = ["keyboard"],
                 verticalMovement = False,horizontalMovement = False, speed = 10,
                 imageSize = ((TILE_SIZE[0])*2,(TILE_SIZE[1])*2)):
        super().__init__(spriteFolderName, tag, spriteAmount, animatedSptrite, spriteColor, boundType, moveType, verticalMovement, horizontalMovement, speed, imageSize)

        