import pygame as pg


class Controler():
    def __init__(self,cont_num,deadZone=0.04):
        self.deadZone = deadZone

        try:
            self.controller = pg.joystick.Joystick(cont_num)
            self.controller.init()
            try:
                contId = self.controller.get_instance_id()
            except AttributeError:
                contId = self.controller.get_id()

        except IOError:
            print("no controller conected")
    
    def getDpad(self):
        dpad = self.controller.get_hat(0)
        x = dpad[0]
        y = dpad[1]*-1
        dpadDict = {"D_X":x,"D_Y":y}
        dpadDict["D_C"] = 10
        return dpadDict

    def getButtons(self):
        a = self.controller.get_button(0)
        b = self.controller.get_button(1)
        x = self.controller.get_button(2)
        y = self.controller.get_button(3)
        lb = self.controller.get_button(4)
        rb = self.controller.get_button(5)
        start = self.controller.get_button(6)
        back = self.controller.get_button(7)
        lj = self.controller.get_button(8)
        rj = self.controller.get_button(9)
        buttonsDict = {"A":a,"B":b,"X":x,"Y":y,"LB":lb,"RB":rb,"START":start,"BACK":back,"LJ":lj,"RJ":rj}
        return buttonsDict

    def getAxes(self):
        leftX = self.controller.get_axis(0)
        leftY = self.controller.get_axis(1)
        rightX = self.controller.get_axis(2)
        rightY = self.controller.get_axis(3)
        leftTrig = self.controller.get_axis(4)
        rightTrig = self.controller.get_axis(5)

        if leftX < self.deadZone and leftX > -self.deadZone:
            leftX = 0
        if leftY < self.deadZone and leftY > -self.deadZone:
            leftY = 0
        if rightX < self.deadZone and rightX > -self.deadZone:
            rightX = 0
        if rightY < self.deadZone and rightY > -self.deadZone:
            rightY = 0
        # set up key value pairs
        axisDict = {"LJOY_Y":leftY,
                    "LJOY_X":leftX,
                    "RJOY_X":rightX,
                    "RJOY_Y":rightY,
                    "LTRIG":leftTrig,
                    "RTRIG":rightTrig}
        return axisDict        


    