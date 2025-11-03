from Assets.scripts.settings import *
from Assets.scripts.classes.controller_class import Controller
from Assets.scripts.classes.player_class import Player
from Assets.scripts.classes.presClass import Present

class Game(object):

    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.joystick.init()
        self.clock = pg.time.Clock()
        self.window = pg.display.set_mode((SWIDTH, SHEIGHT))
        pg.mouse.set_visible(False)

        self.players = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()

        self.controllers = []
        self.joy_count = pg.joystick.get_count()
        if self.joy_count > 0:
            for i in range(self.joy_count):
                self.controllers.append(Controller(i))

        self.player = Player("Player","player",1)
        self.player.verticalMovement = False
        self.players.add(self.player)
        self.all_sprites.add(self.player)
        self.is_playing = False
        self.level = 0

        self.enemy = Player("","enemy",4,False,blue)
        self.all_sprites.add(self.enemy)
        self.enemies.add(self.enemy)
        self.enemy.boundType = 'bounce'
        self.enemy.moveType = 'auto'
        self.enemy.verticalMovement = False
        self.enemy.speed = 15
        self.enemy.rect.center = (WIDTH/2, 0)

    def update(self):
        dt = self.clock.tick(FPS)
        self.all_sprites.update(dt)

        #pg.sprite.spritecollide(self.player, self.enemies,True)
        pg.sprite.groupcollide(self.players,self.enemies,True,False)

    def draw(self):
        self.window.fill(darkRed)
        self.all_sprites.draw(self.window)
        pg.display.flip()

    def get_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT :
                self.is_playing = False
            elif event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.is_playing = False
                if event.key == pg.K_p:
                    self.spawnPresent()

    def mainLoop(self):
        while self.is_playing:
            self.clock.tick(FPS)
            self.get_events()
            self.update()
            self.draw()

        print("ran")

    def start_screen(self):
        self.window.fill(blue)
        draw_text(self.window, TITLE, 150, SWIDTH / 2, SHEIGHT / 4,red, "Impact")
        draw_text(self.window, "Press Space To Start", 50, (SWIDTH / 2), (SHEIGHT / 4)+150, green, "Impact")
        pg.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                    if event.key == pg.K_SPACE:
                        self.window = pg.display.set_mode((WIDTH, HEIGHT),pg.FULLSCREEN)
                        waiting = False
                        self.is_playing = True

    def end_screen(self):
        self.window.fill(green)
        draw_text(self.window, "GAME OVER", 150, WIDTH / 2, HEIGHT / 4,red, "Impact")
        draw_text(self.window, "Play Again? (y/n)", 50, (WIDTH / 2), (HEIGHT / 4)+150 , blue, "Impact")

        pg.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT or (event.type == pg.KEYUP and event.key == pg.K_ESCAPE):
                    return "END"
                    pg.quit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_y:
                        waiting = False
                    elif event.key == pg.K_n:
                        return "END"
    
    def spawnPresent(self):
        pres = Present((WIDTH), (HEIGHT)*5)

