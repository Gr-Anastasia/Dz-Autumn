class Specialty:
    specialty_id = 0

    @classmethod
    def autoincrement(cls):
        cls.specialty_id += 1
        return cls.specialty_id

    def __init__(self, name):
        self.__id = Specialty.autoincrement()
        self.name = name

    def get_id(self):
        return self.__id

it = Specialty(name="information security")
chemistry = Specialty(name="laboratory assistant")