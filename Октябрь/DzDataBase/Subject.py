class Subject:
    subject_id = 0

    @classmethod
    def autoincrement(cls):
        cls.subject_id += 1
        return cls.subject_id

    def __init__(self, name):
        self.__id = Subject.autoincrement()
        self.name = name

    def get_id(self):
        return self.__id

biology = Subject(name="Biology")
math = Subject(name="Math")