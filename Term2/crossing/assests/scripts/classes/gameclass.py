from assests.scripts.settings import *
from assests.scripts.classes.screenTextClass import ScreenText



from assests.scripts.settings import *
from assests.scripts.classes.screenTextClass import ScreenText
class Game():
    def __init__(self):
        pg.init() 
        pg.mixer.init()
        pg.joystick.init()
        self.controllerList = []
        self.gameWindow = pg.display.set_mode((WIDTH,HEIGHT))
      
        self.isPlaying = True
        self.clock = pg.time.Clock()
        self.screenWriter = ScreenText(25,color=purple)
        self.joyStickCount = pg.joystick.get_count()   
      
        if self.joyStickCount > 0:
            self.controllerConected = True
        else:
            self.controllerConected = False
        if self.controllerConected:
            if self.joyStickCount > 0:
                for i in range(self.joyStickCount):
                    x = pg.joystick.Joystick(i)
                    x.init()
                    self.controllerList.append(x)
            try:
                self.controllerId = self.controllerList[0].get_instance_id()
            except AttributeError:
                self.controllerId = self.controllerList[0].get_id()
      
      
        self.play()
    def play(self):
        """Main Game Loop"""
        while self.isPlaying:
            # tick clock
            self.clock.tick(FPS)
            #get inputs
            self.getInputs()
            #update
            self.update()
            #draw
            self.draw()
    def update(self):
        temp = pg.joystick.get_count()
        if temp != self.joyStickCount:
            if temp > 0:
                for i in range(self.joyStickCount):
                    x = pg.joystick.Joystick(i)
                    x.init()
                    self.controllerList[i] = x
                try:
                    self.controllerId = self.controllerList[0].get_instance_id()
                except AttributeError:
                    self.controllerId = self.controllerList[0].get_id()
            else:
                self.controllerConected = False
                self.isPlaying = False
        self.joyStickCount = temp
  
    def getInputs(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.is_playing = False
            elif event.type == pg.JOYBUTTONDOWN:
                print("pressed a button")
            elif event.type == pg.JOYBUTTONUP:
                print("released a button")
            elif event.type == pg.JOYAXISMOTION:
                print("moved a joystick")
            elif event.type == pg.JOYHATMOTION:
                print("used the dpad")
        # getting the Axes
        self.controller_name = self.controllerList[0].get_name()
        self.axes = self.controllerList[0].get_numaxes()
        self.axis_values = []
        for i in range(self.axes):
            self.axis_values.append(self.controllerList[0].get_axis(i))
        # get the buttons
        self.buttons =self.controllerList[0].get_numbuttons()
        self.button_values =[]
        for i in range(self.buttons):
            self.button_values.append(self.controllerList[0].get_button(i))
        # get the dpad
        self.hats_values = []
        self.num_hats = self.controllerList[0].get_numhats()
        for i in range(self.num_hats):
            self.hats_values.append(self.controllerList[0].get_hat(i))
      
          
          
    def draw(self):
        self.gameWindow.fill(gray)
        self.drawToScreen()
      
        pg.display.update()
    def drawToScreen(self):
        self.screenWriter.reset()
        self.screenWriter.printToScreen(self.gameWindow, "Xbox Controller Values")
        self.screenWriter.indent()
        self.screenWriter.printToScreen(self.gameWindow, "number of Controllers {}".format(self.joyStickCount))
        self.screenWriter.printToScreen(self.gameWindow, "Controller id {}".format(self.controllerId))
        self.screenWriter.printToScreen(self.gameWindow, "Controller name {}".format(self.controller_name))
        self.screenWriter.printToScreen(self.gameWindow, "Controller number of Axes {}".format(self.axes))
        self.screenWriter.unIndent()
        self.screenWriter.printToScreen(self.gameWindow, "Controller Axes values")
        self.screenWriter.indent()
        self.screenWriter.indent()
        i = 0
        nameList = ["left stick X","left stick Y","right stick X","right stick Y","left trigger","right trigger"]
        for axis in self.axis_values:
            self.screenWriter.printToScreen(self.gameWindow, " axis {0} {2} = {1:>6.3f}".format(i, axis,nameList[i]))
            i+=1
        self.screenWriter.unIndent()
        self.screenWriter.unIndent()
        self.screenWriter.printToScreen(self.gameWindow, "Controller Button values")
        self.screenWriter.indent()
        self.screenWriter.indent()
        i=0
        nameList = ["A", "B", "X", "Y", "left Bumper","right Bumper","select","start","left joy","right joy","na","na","na","na","na","na"]
        for bttn in self.button_values:
            self.screenWriter.printToScreen(self.gameWindow," button {0} {2} = {1}".format(i, bttn,nameList[i]))
            i += 1
        self.screenWriter.unIndent()
        self.screenWriter.unIndent()
        self.screenWriter.printToScreen(self.gameWindow, "Dpad values")
        self.screenWriter.indent()
        self.screenWriter.indent()
        self.screenWriter.printToScreen(self.gameWindow,"number of hats {}".format(self.num_hats))
        for i in range(len(self.hats_values)):
            self.screenWriter.printToScreen(self.gameWindow, "Dpad = {}".format(self.hats_values[i]))
       