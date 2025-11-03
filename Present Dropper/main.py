from Assets.scripts.settings import *
from Assets.scripts.classes.Game_class import Game
from Assets.scripts.classes.startScreen import startScreen
def main():
    while True:
        game = Game()
        game.start_screen()
        game .mainLoop()
        end = game.end_screen()
        if end == "END":
            break
    pg.quit()
    quit()

if __name__ == '__main__':
    main()