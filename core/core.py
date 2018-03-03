# -*- encoding: utf-8 -*-
from elements import ElementManager
from hw_controller.hw_controller import *
from multiprocessing import Pool


class Core(object):

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



