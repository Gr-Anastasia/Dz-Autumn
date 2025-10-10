from Subject import biology
from Group import bg_1
from Facuity import him_bio
from Specialty import chemistry
from Teacher import juli_tch


class Student:
    student_id = 0

    @classmethod
    def autoincrement(cls):
        cls.student_id += 1
        return cls.student_id

    def __init__(self, name, surname, phone, number_student,
                 faculty, specialty, group, patronymic = None, subjects = None, budget = True):
        self.__id = Student.autoincrement()
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.phone = phone
        self.number_student = number_student
        self.budget = budget
        self.faculty = faculty
        self.specialty = specialty
        self.group = group
        if subjects is None:
            self.subjects = list()
        else:
            self.subjects = subjects

    def get_id(self):
        return self.__id

    def get_surname(self):
        return self.surname


nastya_stu = Student(name ="Nastya",
                   surname = "Grigorjeva",
                   phone="8937157896587",
                   number_student="2811",
                   faculty=him_bio,
                   specialty=chemistry,
                   group=bg_1,
                    subjects=[{"subject" : biology, "teacher" : juli_tch, "average" :4.7}],
                   patronymic="Andreevna")




# print(nastya_stu.faculty, nastya_stu.specialty, nastya_stu.group, nastya_stu.subjects)