# -*- encoding: utf-8 -*-
from elements import ElementManager
from hw_controller.hw_controller import blind_open, blind_close
class Core(object):

    MIN_LUX = 400
    MIN_TMP = 20

    MAX_LUX = 200
    MAX_TMP = 30

    def __init__(self):
        self.temperature_lvl = 0
        self.light_lvl = 0

    def action_selector(self):
        '''call determinate function depending of environement status'''
        current_temp = self.temperature_lvl
        current_light = self.light_lvl

        # Check Extream vals
        if current_light in range(self.MIN_LUX, self.MAX_LUX):
            blind_open()
        elif current_light < self.MIN_LUX:
            blind_close()
        elif current_light > self.MAX_LUX:
            blind_open()
        # TODO what to do with temperature?

    
