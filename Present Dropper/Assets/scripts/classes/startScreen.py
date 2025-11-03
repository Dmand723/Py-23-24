from Assets.scripts.settings import *
from Assets.scripts.classes.gameObjectClass import Game_Object

class startScreen(object):
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.clock = pg.time.Clock()
        self.window = pg.display.set_mode((SWIDTH, SHEIGHT))
        pg.mouse.set_visible(False)
        self.startMap = Game_Object(0,0,SWIDTH,SHEIGHT,os.path.join(spritesDir,"startbg.jpg"))
        self.resart = False
        
    def start_screen(self):
            if not self.resart:
                waiting = True
            while waiting:
                self.update()
                self.clock.tick(FPS)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                    if event.type == pg.KEYUP:
                        if event.key == pg.K_ESCAPE:
                            pg.quit()
                        if event.key == pg.K_SPACE:
                            waiting = False
    
    def update(self):
        self.draw()

    