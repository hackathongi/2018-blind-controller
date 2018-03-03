# -*- encoding: utf-8 -*-
from elements import ElementManager

class Zona(object):

    def __init__(self, id, z_name=False, elems=False):
        if not id or not  isinstance(id, (int, long)):
            raise ValueError('ERROR:', 'id should be a number > 0')
        self._id = id
        self.name = z_name
        self.element_managers = elems or {}

    def get_all_elements_from_type(self, element_type=False):
        manager = self.element_managers.get(element_type, [])
        return manager.elements if manager else manager


    def get_specific_elements_from_ids(self, element_type=False, ids=list()):
        if isinstance(ids, (int, long)):
            ids = [ids]
        elements_list = self.element_managers.get(element_type)
        if elements_list:
            return filter(lambda x: x._id in ids, elements_list.elements)
            #return [element for element in elements_list.elements if element._id in ids]
        return []


    def insert_element(self, elem_list=list()):
        for elem in elem_list:
            elem_type = elem.e_type
            self.element_managers[elem_type].elements.append(elem) if self.element_managers[elem_type] else self.element_managers[elem_type] = ElementManager([elem])


    def write_values(self, element=None):
        if element:
            elem_type = element.e_type
            elem_id = element._id
            # Fix for only one element (Quick solution)
            self.element_managers[elem_type] = ElementManager([element])

            # TODO
            # In a future can be used thes code to works with list with more than one elements
            # manager = self.element_managers.get(elem_type)
            # if manager:
                # element_found = next((x for x in manager if x._id == elem_id), None)
                # elem_found = next(filter(lambda x: x._id == elem_id, manager))

            # else:
            #     self.element_managers[elem_type] = ElementManager([element])



