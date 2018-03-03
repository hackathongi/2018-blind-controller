# -*- encoding: utf-8 -*-


class Zona(object):

    def __init__(self, id, z_name=False, elems=False):
        if not id or not  isinstance(id, (int, long)):
            raise ValueError('ERROR:', 'id should be a number > 0')
        self._id = id
        self.name = z_name
        self.element_managers = elems or {}

    def get_all_elements_from_type(self, element_type=False):
        return self.element_managers.get(element_type, [])


    def get_specific_elements_from_ids(self, element_type=False, ids=list()):
        if isinstance(ids, (int, long)):
            ids = [ids]
        elements_list = self.element_managers.get(element_type)
        if elements_list:
            return [element for element in elements_list.elements if element._id in ids]
        return []


    def insert_element(self, elem_list=list()):
        for elem in elem_list:
            elem_type = elem.e_type
            self.element_managers[elem_type].append(elem) if self.element_managers[elem_type] else self.element_managers[elem_type] = [elem]


    #def write_values(self, ids, element_type=False, values=False):

