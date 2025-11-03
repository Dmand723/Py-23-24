import pygame as pg


class Game_Object(object):
    def __init__(self,x,y,width,height,image_path):
        self.ogImage = pg.image.load(image_path)
        self.width = width
        self.height = height
        self.image = pg.transform.scale(self.ogImage,(self.width,self.height))
        self.startX = x
        self.startY = y
        self.curX = x
        self.curY =  y 
    
    def draw(self,window):
        window.blit(self.image,(self.curX,self.curY))

    def reset(self):
        self.curX, self.curY = self.startY,self.curY