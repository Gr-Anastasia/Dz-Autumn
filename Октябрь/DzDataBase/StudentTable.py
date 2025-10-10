from Student import nastya_stu
from Group import it_1


class StudentTable:
    def __init__(self, name):
        self.name = name
        self.students = list()

    def add_student(self, student):
        if student in self.students:
            raise ValueError("Такой студент уже есть")
        else:
            self.students.append(student)
        return self.students

    def update_student_surname(self, student, new_surname):
        for student in self.students:
            student.surname = new_surname
        return student.surname

    def update_student_phone(self, student, new_phone):
        for student in self.students:
            student.phone = new_phone
        return student.surname

    def update_student_group(self, student, new_group):
        for student in self.students:
            student.group = new_group
        return student.group

    def update_student_number(self, student, new_number):
        for student in self.students:
            student.number_student = new_number
        return student.number_student

    def add_subject(self, student , new_subject):

        # for student in self.students:
        #     student.number_student = new_number
        # return student.number_student

        return


    def del_student(self, student):
        self.students.remove(student)
        return self.students

"""
приватность 
абдейт вызвает сет нейм
"""




student_table1 = StudentTable(name="first course")

print(nastya_stu.surname)
print(nastya_stu.phone)
print(nastya_stu.group)

student_table1.add_student(nastya_stu)
student_table1.update_student_surname(student=nastya_stu,
                                      new_surname="Mur")
student_table1.update_student_phone(student=nastya_stu,
                                      new_phone="000000000000")
student_table1.update_student_group(student=nastya_stu,
                                    new_group=it_1)

print(nastya_stu.surname)
print(nastya_stu.phone)
print(nastya_stu.group)











# добавление, обновление, удаление?