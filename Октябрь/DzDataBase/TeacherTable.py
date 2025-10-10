from Student import nastya_stu
from Department import natural_sc
from Group import it_1


class TeacherTable:
    def __init__(self, name):
        self.name = name
        self.teachers = list()

    def add_teacher(self, teacher):
        if teacher in self.teachers:
            raise ValueError("Такой преподаватель уже есть")
        else:
            self.teachers.append(teacher)
        return self.teachers

    def update_teacher_surname(self, teacher, new_surname):
        for teacher in self.teachers:
            teacher.surname = new_surname
        return teacher.surname

    def update_teacher_phone(self, teacher, new_phone):
        for teacher in self.teachers:
            teacher.phone = new_phone
        return teacher.surname

    # def update_teacher_academic_degree(self, teacher, new_phone):
    #     for teacher in self.teachers:
    #         teacher.phone = new_phone
    #     return teacher.surname

    # def update_teacher_department(self, teacher, new_group):
    #     for teacher in self.teachers:
    #         teacher.group = new_group
    #     return teacher.group

    def update_teacher_number(self, teacher, new_number):
        for teacher in self.teachers:
            teacher.number_student = new_number
        return teacher.number_student

    def add_subject(self, teacher , new_subject):

        # for student in self.students:
        #     student.number_student = new_number
        # return student.number_student

        return


    def del_teacher(self, teacher):
        self.teachers.remove(teacher)
        return self.teachers

"""
приватность 
абдейт вызвает сет нейм
"""




# student_table1 = StudentTable(name="first course")
#
# print(nastya_stu.surname)
# print(nastya_stu.phone)
# print(nastya_stu.group)
#
# student_table1.add_student(nastya_stu)
# student_table1.update_student_surname(student=nastya_stu,
#                                       new_surname="Mur")
# student_table1.update_student_phone(student=nastya_stu,
#                                       new_phone="000000000000")
# student_table1.update_student_group(student=nastya_stu,
#                                     new_group=it_1)
#
# print(nastya_stu.surname)
# print(nastya_stu.phone)
# print(nastya_stu.group)











# добавление, обновление, удаление?