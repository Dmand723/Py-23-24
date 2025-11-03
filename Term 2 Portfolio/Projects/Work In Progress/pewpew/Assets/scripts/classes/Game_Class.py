from Assets.scripts.settings import *
from Assets.scripts.classes.playerClass import Player
from Assets.scripts.classes.spriteGroups import AllSprites

class Game(object):
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.is_playing = True
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.players = pg.sprite.Group()
        self.all_sprites = AllSprites()
        self.gameSetup()
        

    def get_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.is_playing = False

    def update(self):
        self.dt = self.clock.tick(FPS)/1000
        self.all_sprites.update(self.dt)

    def draw(self):
        self.window.fill(black)
        self.all_sprites.customDraw(self.player)
        pg.display.flip()

    def gameSetup(self):
        self.player = Player((200,200),(self.players,self.all_sprites),os.path.join(spritesDir,"player"),self)  

    def play(self):
        while self.is_playing:
            self.clock.tick(FPS)
            self.get_events()
            self.update()
            self.draw()

    def start_screen(self):
        self.window.fill(black)
        draw_text(self.window, TITLE, 150, WIDTH / 2, HEIGHT / 4,  green, "impact")
        pg.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_SPACE or event.key == pg.K_RETURN:
                        waiting = False

    def end_screen(self):
        self.window.fill(black)
        draw_text(self.window, "GameOver", 150, WIDTH / 2, HEIGHT / 4,red, "impact")
        draw_text(self.window, "yould you like to play again (Y/N)?", 75, WIDTH / 2, HEIGHT / 4+200,green, "impact")
        pg.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    return "quit"
                    pg.quit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_y:
                        waiting = False
                    elif event.key == pg.K_n:
                        return "quit"