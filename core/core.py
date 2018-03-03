# -*- encoding: utf-8 -*-
from elements import ElementManager
from hw_controller.hw_controller import *
from multiprocessing import Pool


class Core(object):
    MIN_LUX = 400
    MIN_TMP = 20

    MAX_LUX = 200
    MAX_TMP = 30

    def __init__(self):
        self.manager = ElementManager()
        self.pool = Pool(processes=1)

    def blind_up(self, t=0):
        self.pool.close()
        self.pool.terminate()
        self.pool = Pool(processes=1)
        self.pool.apply_async(blind_open, (t,))

    def blind_down(self, t=0):
        self.pool.close()
        self.pool.terminate()
        self.pool = Pool(processes=1)
        self.pool.apply_async(blind_close, (t,))

    def blind_stop(self):
        self.pool.close()
        self.pool.terminate()
        self.pool = Pool(processes=1)

    def update_sensors(self, **kwargs):
        '''call determinate function depending of environement status'''
        self.light_lvl = kwargs['light_lvl']

        # Check Extream vals
        if self.light_lvl >= self.MIN_LUX:
            self.blind_up()
        else:
            self.blind_down()
        # TODO what to do with temperature?


