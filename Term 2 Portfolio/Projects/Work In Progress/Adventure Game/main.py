from assets.scripts.settings import *
from assets.scripts.classes.gameClass import Game
from assets.scripts.classes.gameSetupClass import Setup

def main():
    setup = Setup()
    setup.setup()
    playerNames = setup.getPlayers()
    game = Game(
        playerNames)
    game.gameSetup()
    game.mainloop()
    end = game.endScreen()
    if end == "END":
        pg.quit()
        quit()
    elif end == "AGAIN":
        if __name__ == "__main__":
            main()

if __name__ == "__main__":
    main()