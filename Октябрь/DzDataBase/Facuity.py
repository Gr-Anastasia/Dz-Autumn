class Faculty:
    faculty_id = 0

    @classmethod
    def autoincrement(cls):
        cls.faculty_id += 1
        return cls. faculty_id

    def __init__(self, name):
        self.__id = Faculty.autoincrement()
        self.name = name

    def get_id(self):
        return self.__id

him_bio = Faculty(name="him_bio")
