# -*- encoding: utf-8 -*-


class ElementManager(object):
    def __init__(self, elements_list=False):
        self.elements = elements_list or []


class Element(object):

    def __init__(self, init_name, init_rotation, eng_state, max_limit):
        '''
            rotation point: Integer from 0 to max -> allows to know
            in what position is engine rotation
            enggine_state: Integer value from -1 to 1 where ->
                -1: engine ons left rotation
                +-0: engine off
                +1: engine on right rotation
            max: max value to avoid supra rotation and a future disaster
        '''
        self.name = init_name
        self.rotation_point = init_rotation or 0
        self.engine_state = eng_state or 0
        self.max = max_limit or 0

