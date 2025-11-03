from assests.scripts.settings import *


class ScreenText():
    def __init__(self,fontsize,fontName=None,color=black):
        self.fontsize = fontsize
        self.fontname = fontName
        self.color = color
        self.x = ""
        self.y = ""
        self.lineHeight = ""
        self.font = pg.font.Font(self.fontname,self.fontsize)
        self.reset()

    def printToScreen(self,screen,text):
        textBitMap = self.font.render(text,True,self.color)
        screen.blit(textBitMap,(self.x,self.y))
        self.y += self.lineHeight
    
    def reset(self):
        self.x = 25
        self.y = 25
        self.lineHeight = self.fontsize - 3

    def indent(self):
        self.x += 10


    def unIndent(self):
        self.c -= 10

    def newLine(self):
        self.y +=self.lineHeight
