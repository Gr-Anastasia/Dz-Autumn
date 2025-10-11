from MixinTable import MixinTable
from Teacher import juli_tch
from Department import technical_sc


class TeacherTable(MixinTable):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.teachers = self.elems

    def add_teacher(self, teacher):
        return self.add_elem(teacher)

    def update_teacher_surname(self, teacher, new_surname):
        for teach in self.teachers:
            if teach == teacher:
                teacher._surname = new_surname
            return teacher._surname

    def update_teacher_phone(self, teacher, new_phone):
        for teach in self.teachers:
            if teach == teacher:
                teacher._phone = new_phone
            return teacher._phone

    def update_teacher_academic_degree(self, teacher, new_academic_degree):
        for teach in self.teachers:
            if teach == teacher:
                teacher.academic_degree = new_academic_degree
            return teacher.academic_degree

    def update_teacher_department(self, teacher, new_department):
        for teach in self.teachers:
            if teach == teacher:
                teacher.department = new_department
            return teacher.department

    def del_teacher(self, teacher):
        return self.del_elem(teacher)

teacher_table1 = TeacherTable(name="Biologi")

print(juli_tch.get_surname())
print(juli_tch.get_phone())
print(juli_tch.academic_degree)
print(juli_tch.department)

teacher_table1.add_teacher(juli_tch)
teacher_table1.update_teacher_surname(teacher=juli_tch,
                                      new_surname="Ivanova")
teacher_table1.update_teacher_phone(teacher=juli_tch,
                                      new_phone="000000000000")
teacher_table1.update_teacher_department(teacher=juli_tch,
                                         new_department=technical_sc)
teacher_table1.update_teacher_academic_degree(teacher=juli_tch,
                                              new_academic_degree="Professor")

print("Новая", juli_tch.get_surname())
print("Новая", juli_tch.get_phone())
print("Новая", juli_tch.academic_degree)
print("Новая", juli_tch.department)

