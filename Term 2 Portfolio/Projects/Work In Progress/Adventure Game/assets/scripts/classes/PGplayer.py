from assets.scripts.settings import *
class Player(pg.sprite.Sprite):
    def __init__(self,spritePath):
        super(Player, self).__init__()
        self.speed = 5
        self.image = 
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.wrap_movement = True
        self.move_dir_x = 1
        self.move_dir_y = 0


    def update(self):
        self.move()
        if self.wrap_movement:
            if self.rect.left >= WIDTH:
                self.rect.right = 0
            elif self.rect.right <= 0:
                self.rect.left = WIDTH
            if self.rect.bottom < 0:
                self.rect.top = HEIGHT
            elif self.rect.top > HEIGHT:
                self.rect.bottom = 0

    def animate(self):
        pass

    def move(self):
        self.rect.center = (self.rect.centerx + self.speed * self.move_dir_x, self.rect.centery + self.speed * self.move_dir_y)

