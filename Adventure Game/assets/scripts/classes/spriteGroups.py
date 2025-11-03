from typing import Iterable, Union
from pygame.sprite import AbstractGroup
from assets.scripts.settings import *



class AllSprites(pg.sprite.Group):
    
    def __init__(self):
        super(AllSprites,self).__init__()
        self.offset = vec()
        self.displaySuface = pg.display.get_surface()
        pathx = os.path.join(PATHS["other"],"bg.png")
        pathx = pathx.replace("\scripts\assets", "")
        self.bg = pg.image.load("assets//sprites//other//bg.png").convert()
        self.bg = pg.transform.scale(self.bg,(bgWidth,bgHeight))
    def customDraw(self,player):
        self.offset.x = player.rect.centerx - WIDTH/2
        self.offset.y = player.rect.centery - HEIGHT/2

        self.displaySuface.blit(self.bg,-self.offset)
        for sprite in self.sprites():
            offsetRect = sprite.image.get_rect(center = sprite.rect.center)
            offsetRect.center -= self.offset
            self.displaySuface.blit(sprite.image,offsetRect)