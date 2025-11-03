from Assets.scripts.classes.gameObjectClass import Game_Object
from Assets.scripts.settings import *


class Present(Game_Object):
    def __init__(self, x, y):
        image_path = pg.image.load(os.path.join(spritesDir,"present1.png")).convert()
        width = TITLE[0]
        height = TITLE[1]
        super().__init__(x, y, width, height, image_path)