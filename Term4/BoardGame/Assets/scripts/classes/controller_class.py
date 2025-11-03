import pygame as pg

class Controller():
    def __init__(self,cont_num,dead_zone=0.25):
        self.dead_zone = dead_zone
        try:
            self.controller = pg.joystick.Joystick(cont_num)
            self.controller.init()
            try:
                cont_id = self.controller.get_instance_id()
            except AttributeError:
                cont_id = self.controller.get_id()

        except IOError:
            print("no controller connected")

    def get_dpad(self):
        dpad = self.controller.get_hat(0)
        x = dpad[0]
        y = dpad[1]*-1
        dpad_dict = {"D_X":x,"D_Y":y}
        return dpad_dict
    def get_buttons(self):
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
        buttons_dict = {"A":a,"B":b,"X":x,"Y":y,"LB":lb,"RB":rb,
                        "START":start,"BACK":back,"LJ":lj,"RJ":rj}
        return buttons_dict
    def get_axes(self):
        left_x = self.controller.get_axis(0)
        left_y = self.controller.get_axis(1)
        right_x = self.controller.get_axis(2)
        right_y = self.controller.get_axis(3)
        left_trig = self.controller.get_axis(4)
        right_trig = self.controller.get_axis(5)

        if left_x > 0 and not left_x < self.dead_zone:
            left_x=left_x
        elif left_x < 0 and not left_x > -self.dead_zone:
            left_x = left_x
        else:
            left_x = 0
        if left_y > 0 and not left_y < self.dead_zone:
            left_y = left_y
        elif left_y < 0 and not left_y > -self.dead_zone:
            left_y = left_y
        else:
            left_y = 0

        if right_x > 0 and not right_x < self.dead_zone:
            right_x = right_x
        elif right_x < 0 and not right_x > -self.dead_zone:
            right_x = right_x
        else:
            right_x = 0
        if right_y > 0 and not right_y < self.dead_zone:
            right_y = right_x
        elif right_y < 0 and not right_y > -self.dead_zone:
            right_y = right_x
        else:
            right_y = 0

        # set up key value pairs
        axis_dict = {"LJOY_Y": left_y,
                     "LJOY_X": left_x,
                     "RJOY_Y": right_y,
                     "RJOY_X": right_x,
                     "LTRIG": left_trig,
                     "RTRIG": right_trig}
        return axis_dict