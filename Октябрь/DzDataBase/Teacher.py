from Department import natural_sc

class Teacher:
    teacher_id = 0

    @classmethod
    def autoincrement(cls):
        cls.teacher_id += 1
        return cls.teacher_id

    def __init__(self, name, surname, phone, academic_degree, department, patronymic = None):
        self.__id = Teacher.autoincrement()
        self.name = name
        self._surname = surname
        self.patronymic = patronymic
        self._phone = phone
        self.academic_degree =  academic_degree
        self.department = department

    def get_id(self):
        return self.__id

    def get_phone(self):
        return self._phone

    def get_surname(self):
        return self._surname


juli_tch = Teacher(name="Julia",
                   surname="Petrova",
                   phone="89657454287",
                   academic_degree="Professor",
                   department=natural_sc)

juli_tch.get_phone()
juli_tch.get_surname()