from Assets.scripts.settings import *

class ScreenText():
    def __init__(self,fontsize,fontname=None,color=black):
        self.fontsize = fontsize # fix the font name
        self.fontname = fontname
        self.color = color
        self.x = ""
        self.y = ""
        self.line_height = ""
        self.font = pg.font.Font(self.fontname,fontsize)
        self.reset()

    def printToScreen(self,screen,text):
        textBitmap = self.font.render(text,True,self.color)
        screen.blit(textBitmap,(self.x,self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 25
        self.y = 25
        self.line_height = self.fontsize -3

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

    def newLine(self):
        self.y += self.line_height