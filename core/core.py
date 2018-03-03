# -*- encoding: utf-8 -*-
from elements import ElementManager

class Core(object):

    MIN_LUX = 400
    MIN_TMP = 20

    MAX_LUX = 200
    MAX_TMP = 30

    def __init__(self):
        self.temperature_lvl = 0
        self.light_lvl = 0
        #self.manager = ElementManager()



    def action_selector(self):
        '''call determinate function depending of environement status'''
        current_temp = self.temperature_lvl
        current_light = self.light_lvl

        # Check Extream vals
        if current_light in range(self.MIN_LUX, self.MAX_LUX):


    def write(self):
