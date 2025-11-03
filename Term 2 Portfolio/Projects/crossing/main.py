from assests.scripts.settings import *
from assests.scripts.classes.gameclass import Game
from assests.scripts.classes.slimeGameClass import SlimeGame



def main():
    while True:
        game = SlimeGame()
        game.startScreen()
        game.mainLoop()
        end = game.endScreen()
        if end == "END":
            pg.quit()
            quit()
        elif end == "AGAIN":
            pass
            #play again

if __name__ == '__main__':
    main()