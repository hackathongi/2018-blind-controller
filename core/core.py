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

    def update_sensors(self, **kwargs):
        '''call determinate function depending of environement status'''
        self.light_lvl = kwargs['light_lvl']


        # Check Extream vals
        if self.light_lvl in range(self.MIN_LUX, self.MAX_LUX):
            blind_open()
        elif self.light_lvl < self.MIN_LUX:
            blind_close()
        elif self.light_lvl > self.MAX_LUX:
            blind_open()
        # TODO what to do with temperature?

