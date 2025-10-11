class MixinTable:
    def __init__(self, name):
        self.name = name
        self.elems = list()

    def add_elem(self, elem):
        if elem in self.elems:
            raise ValueError("Такой элемент уже есть")
        else:
            self.elems.append(elem)
        return self.elems

    # def update_elem_surname(self, elem, new_surname):
    #     for elements in self.elems:
    #         if elements == elem:
    #            elem._surname = new_surname
    #         return elem._surname
    #
    # def update_elem_phone(self, elem, new_phone):
    #     for elements in self.elems:
    #         if elements == elem:
    #             elem._phone = new_phone
    #         return elem._phone

    def del_elem(self, elem):
        self.elems.remove(elem)
        return self.elems