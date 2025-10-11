from MixinTable import MixinTable
from Student import nastya_stu
from Group import it_1

class StudentTable(MixinTable):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.students = self.elems

    def add_student(self, student):
        return self.add_elem(student)

    def update_student_surname(self, student, new_surname):
        for std in self.students:
            if std == student:
                student._surname = new_surname
                return student._surname

    def update_student_phone(self, student, new_phone):
        for std in self.students:
            if std == student:
                student._phone = new_phone
                return student._phone

    def update_student_group(self, student, new_group):
        for std in self.students:
            if std == student:
                student.group = new_group
                return student.group

    def update_student_number(self, student, new_number):
        for std in self.students:
            if std == student:
                student.number_student = new_number
                return student.number_student

    def del_student(self, student):
        return self.del_elem(student)

student_table1 = StudentTable(name="first course")

print(nastya_stu.get_surname())
print(nastya_stu.get_phone())
print(nastya_stu.group)

student_table1.add_student(nastya_stu)
student_table1.update_student_surname(student=nastya_stu,
                                      new_surname="Mur")
student_table1.update_student_phone(student=nastya_stu,
                                      new_phone="000000000000")
student_table1.update_student_group(student=nastya_stu,
                                    new_group=it_1)

print("Новая", nastya_stu.get_surname())
print("Новая", nastya_stu.get_phone())
print("Новая", nastya_stu.group)

