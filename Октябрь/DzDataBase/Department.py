class Department:
    department_id = 0

    @classmethod
    def autoincrement(cls):
        cls.department_id += 1
        return cls.department_id

    def __init__(self, name):
        self.__id = Department.autoincrement()
        self.name = name

    def get_id(self):
        return self.__id

technical_sc = Department(name="Technical sciences")
natural_sc = Department(name="Natural sciences")