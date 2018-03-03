# -*- encoding: utf-8 -*-

class Zona(object):

    def __init__(self, elems=False):
        self.element_managers = elems or {}
    
    # inser