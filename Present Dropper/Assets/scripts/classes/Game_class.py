from Assets.scripts.settings import *
from Assets.scripts.classes.controller_class import Controller
from Assets.scripts.classes.spriteObj import SpriteObj
from Assets.scripts.classes.gameObjectClass import Game_Object
from Assets.scripts.classes.bomb import Bomb

class Game(object):

    def __init__(self):
        print(WIDTH,HEIGHT)
        pg.init()
        pg.mixer.init()
        self.initMusic()
        pg.joystick.init()
        self.clock = pg.time.Clock()
        self.window = pg.display.set_mode((SWIDTH, SHEIGHT))
        pg.mouse.set_visible(False)

        self.players = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.allSnow = pg.sprite.Group()
        self.allBomb = pg.sprite.Group()
        self.allGoldPres = pg.sprite.Group()

        self.controllers = []
        self.joy_count = pg.joystick.get_count()
        if self.joy_count > 0:
            for i in range(self.joy_count):
                self.controllers.append(Controller(i))

        self.player = SpriteObj("Player","player",spriteAmount=1,horizontalMovement=True,speed=15,boundType="wrap",moveType=["mouse"])
        
        self.map = Game_Object(0,0,WIDTH,HEIGHT,os.path.join(spritesDir,"bg.jpg"))
        self.startMap = Game_Object(0,0,SWIDTH,SHEIGHT,os.path.join(spritesDir,"startbg.jpg"))

        self.players.add(self.player)
        self.all_sprites.add(self.player)
        
        self.is_playing = False
        self.paused = False
        
        self.lives = 3
        self.score = 0
        self.level = 1
        self.dead = False
        self.presColected = 0
        self.nextLevelScore = 5

        self.enemySpeed = 10
        self.spawnRate = 1500
        self.spawnCooldown = self.spawnRate

        self.presSpawner = SpriteObj("","presSpawner",spriteAmount=0,animatedSptrite=False,horizontalMovement=True)
        self.all_sprites.add(self.presSpawner)
        self.presSpawner.boundType = 'bounce'
        self.presSpawner.moveType = 'auto'
        self.presSpawner.verticalMovement = False
        self.presSpawner.speed = 15
        self.presSpawner.rect.center = (WIDTH/2, 0)
        self.resart = False
        self.pointerLocation = (SWIDTH/2,SHEIGHT/2)

    def start_screen(self):
        
        if not self.resart:
            waiting = True
        while waiting:
            self.clock.tick(FPS)
            self.startDraw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                    if event.key == pg.K_SPACE:
                        pg.mixer.music.play(-1)
                        self.window = pg.display.set_mode((WIDTH, HEIGHT),pg.FULLSCREEN)
                        waiting = False
                        self.is_playing = True

    def startDraw(self):
        dt = self.clock.tick(FPS)
        self.window.fill(darkRed)
        self.startMap.draw(self.window)
        pointer = SpriteObj('pointer','pointer',moveType=['mouse'],boundType='none',verticalMovement=True,horizontalMovement=True)
        pointer.update(dt)
        draw_text(self.window, TITLE, 70, SWIDTH / 2, SHEIGHT / 4,red, "Impact")
        draw_text(self.window, "Play", 60, (SWIDTH / 2), (SHEIGHT / 4)+130, blue, "Impact")
        draw_text(self.window, "Settings", 30, (SWIDTH / 2), (SHEIGHT / 4)+190, violet, "Impact")
        draw_text(self.window,"How To Play?", 30, (SWIDTH / 2), (SHEIGHT / 4)+220, violet, "Impact")
        pg.display.flip()

    def update(self):
        dt = self.clock.tick(FPS)
        self.all_sprites.update(dt)
        self.allSnow.update(dt)
        
        if self.spawnCooldown <= 0:
            rng = random.randint(0,15)
            if rng == 15 or rng ==14 or rng ==13:
                self.spawnBomb()
                self.spawnCooldown = self.spawnRate - 5
            elif rng == 12:
                self.spawnGoldPresent()
                self.spawnCooldown = self.spawnRate-5
            else:
                self.spawnPresent()
                #self.spawnSnow()
                self.spawnCooldown = self.spawnRate
        else:
            self.spawnCooldown -=dt 
        
        hit =pg.sprite.groupcollide(self.players,self.enemies,False,True)
        if hit:
            self.collectSfx.play()
            self.presColected += 1
            self.score += 1
        
        Ghit =pg.sprite.groupcollide(self.players,self.allGoldPres,False,True)
        if Ghit:
            self.goldCollectSfx.play()
            self.presColected +=1
            self.score += 5
        
        for bombs in self.allBomb:
            bombHit= pg.sprite.collide_rect(self.player,bombs)
            if bombHit and not self.dead:
                self.bombSfx.play()
                
                bombs.imgsize = (TILE_SIZE[0]*2,TILE_SIZE[1]*2)
                bombs.rect.center = self.player.rect.center
                self.player.kill()
                bombs.canExplode = True
                self.dead = True
        if self.presColected == self.nextLevelScore:
            self.LevelUpSfx.play()
            self.level +=1
            self.nextLevelScore +=5
            self.enemySpeed +=2
            self.player.speed +=1
            if self.spawnCooldown > 650:
                self.spawnCooldown -=50
                
            


        for pres in self.enemies:
            if pres.rect.top > self.player.rect.bottom:
                self.missSfx.play()
                self.lives -= 1
                pres.kill()
        for bomb in self.allBomb:
            if bomb.rect.top > self.player.rect.bottom:
                bomb.kill()
        for GPres in  self.allGoldPres:
            if GPres.rect.top > self.player.rect.bottom:
                GPres.kill()
        if self.lives <= 0:
            self.gameOverSfx.play()
            self.is_playing = False

    def draw(self):
        self.map.draw(self.window)
        
        self.allSnow.draw(self.window)
        self.all_sprites.draw(self.window)
        
        
        draw_text(self.window,str.format("Score: {}",self.score),50,(WIDTH - 100),(30),green)
        draw_text(self.window,str.format("Lives: {}",self.lives),50,(WIDTH - 100),(70),green)
        draw_text(self.window,str.format("Level: {}",self.level),50,(WIDTH - 100),(110),green)
        draw_text(self.window,"Press Escape To Pause",30,150,(30),red)
        pg.display.flip()

    def get_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT :
                self.is_playing = False
            elif event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.pauseSfx.play()
                    self.paused = True
                    pg.mixer.music.pause()
                    
            

    def mainLoop(self):
        pg.mixer.music.play(-1)
        self.window = pg.display.set_mode((WIDTH, HEIGHT),pg.FULLSCREEN)
        self.is_playing = True
        while self.is_playing and not self.paused:
            self.clock.tick(FPS)
            self.get_events()
            self.update()
            self.draw()
        
        while self.paused:
            self.pause()

        print("ran")

    

    def end_screen(self):
        self.window.fill(mint)
        pg.mixer.music.pause()
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
                        self.resart = True
                    elif event.key == pg.K_n:
                        return "END"
    
    def spawnPresent(self):
        pres = SpriteObj("Present1","pres",speed=self.enemySpeed,spriteAmount=4)
        pres.verticalMovement = True
        pres.horizontalMovement = False
        pres.rect.center = ((random.randint(100,WIDTH-50)),(0))
        imgsize = ((TILE_SIZE[0]-50),(TILE_SIZE[1]))
        pres.image = pg.transform.scale(pres.image,imgsize)
        pres.moveType = 'auto'
        pres.boundType = 'none'
        self.all_sprites.add(pres)
        self.enemies.add(pres)

    def spawnGoldPresent(self):
        pres = SpriteObj("Present2","GoldPres",speed=self.enemySpeed+7,spriteAmount=1)
        pres.verticalMovement = True
        pres.horizontalMovement = False
        pres.rect.center = ((random.randint(100,WIDTH-50)),(0))
        imgsize = ((TILE_SIZE[0]-50),(TILE_SIZE[1]))
        pres.image = pg.transform.scale(pres.image,imgsize)
        pres.moveType = 'auto'
        pres.boundType = 'none'
        self.all_sprites.add(pres)
        self.allGoldPres.add(pres)

    def spawnBomb(self):
        bomb = Bomb(self,imageSize=(TILE_SIZE[0],TILE_SIZE[1]*2))
        bomb.rect.center = ((random.randint(100,WIDTH-50)),(0))
        self.all_sprites.add(bomb)
        self.allBomb.add(bomb)

    # def spawnSnow(self):
    #     snow = SpriteObj("Snow","Snow",animatedSptrite=True,speed=20,spriteAmount=15,imageSize=((TILE_SIZE[0]-50),(TILE_SIZE[1])))
    #     snow.verticalMovement = True 
    #     snow.horizontalMovement = False
    #     snow.rect.center = ((random.randint(100,WIDTH-50)),(0))
    #     imgsize = ((TILE_SIZE[0]-50),(TILE_SIZE[1]))
    #     snow.image = pg.transform.scale(snow.image,imgsize)
    #     snow.moveType = 'auto'
    #     snow.boundType = 'none'
    #     self.allSnow.add(snow)

    def initMusic(self):
        pg.mixer.init()
        pg.mixer.music.load(os.path.join(soundsDir,"bg.mp3"))
        pg.mixer.music.set_volume(.3)
        self.pauseSfx = pg.mixer.Sound(os.path.join(soundsDir,"pause.mp3"))
        self.pauseSfx.set_volume(.3)
        self.collectSfx = pg.mixer.Sound(os.path.join(soundsDir,"collect.wav"))
        self.collectSfx.set_volume(.3)
        self.goldCollectSfx = pg.mixer.Sound(os.path.join(soundsDir,"goldCollect.wav"))
        self.goldCollectSfx.set_volume(.3)
        self.bombSfx = pg.mixer.Sound(os.path.join(soundsDir,"Explosion.wav"))
        self.bombSfx.set_volume(.3)
        self.LevelUpSfx = pg.mixer.Sound(os.path.join(soundsDir,"nextLevel.wav"))
        self.LevelUpSfx.set_volume(.3)
        self.missSfx = pg.mixer.Sound(os.path.join(soundsDir,"miss.wav"))
        self.missSfx.set_volume(.3)
        self.gameOverSfx = pg.mixer.Sound(os.path.join(soundsDir,"gameOver.wav"))
        self.gameOverSfx.set_volume(.3)
        

    def pause(self):
        draw_text(self.window,"Press Space To Continue",100,WIDTH/2,HEIGHT/2,blue)
        draw_text(self.window,"Press Escape To Quit",100,WIDTH/2,HEIGHT/2 + 100,darkRed)
        pg.display.flip()
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                return "END"
                pg.quit()
            elif event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                if event.key == pg.K_SPACE:
                    self.paused = False
                    pg.mixer.music.unpause()
                    self.mainLoop()
