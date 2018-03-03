# -*- encoding: utf-8 -*-


class ElementManager(object):
    def __init__(self, elements_list=False):
        self.elements = elements_list or []

    @property
    def element_type(self):
        return self.elements[0].e_type if self.elements else False


class Element(object):

    def __init__(self, id, init_name, init_rotation=0, eng_state=0, max_limit=0, obj_type=False):
        '''
            name: str
            rotation point: Integer from 0 to max -> allows to know
            in what position is engine rotation
            enggine_state: Integer value from -1 to 1 where ->
                -1: engine ons left rotation
                +-0: engine off
                +1: engine on right rotation
            max: Integer max value to avoid supra rotation and a future disaster
            type: str type of object
        '''
        if not isinstance(id, (int, long)) or id == 0:
            raise ValueError('ERROR:', 'id should be a number > 0')
        else:
            self._id = id
            self.name = init_name
            self.rotation_point = init_rotation
            self.engine_state = eng_state
            self.max = max_limit
            self.e_type = obj_type



# class Blind(Element):
#
# class Awning(Element):
#
# class Curtains(Element)