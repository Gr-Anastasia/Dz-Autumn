class Doctor:
    def __init__(self, name):
        self.name = name
        self.__jornal = list()

    def visit(self, patient):
        self.__jornal.append(patient)

    def get_patient(self):
        return [patient.name for patient in  self.__jornal]

    def unique_patient(self):
        return list(set(self.get_patient()))


class Patients:
    def __init__(self, name):
        self.name = name


class CommonPatients:
    def __init__(self, *args):
        self.doctor = [doctor for doctor in args]

    def get_doctors(self):
        return [doctor.name for doctor in self.doctor]

    def common_patients(self):
        sets_of_patients = [set(doctor.unique_patient()) for doctor in self.doctor]
        if not sets_of_patients:
            return []
        common_patients = set.intersection(*sets_of_patients)
        return list(common_patients)

class Queue:
    id = 0

    def __init__(self, doctor, patients):
        self.doctor = doctor
        self.patients = patients
        self.id = id + 1
        self.notes = dict()

    # def create_id(self):
    #     if not id in self.notes:
# Создаёт айди доктора

    # def create_dict(self, doctor, patients):
    #     patients = []
    #     [id.doc][patients]
    #




"""
Надо словрь: ключ - айди врача, значение - список очередь 
значение - экземпляр класса 

"""






doc_1 = Doctor("docT")
doc_2 = Doctor("docP")

patient_1 = Patients('Vasya')
patient_2 = Patients('Oleg')
patient_3 = Patients('Nastya')
patient_4 = Patients('Lena')
patient_5 = Patients('Nikita')

doc_1.visit(patient_1)
doc_1.visit(patient_1)
doc_1.visit(patient_2)
doc_1.visit(patient_3)
print("Уникальные пациенты Первого: ", doc_1.unique_patient())
print("Все пациенты Первого: ", doc_1.get_patient())

doc_2.visit(patient_4)
doc_2.visit(patient_5)
doc_2.visit(patient_3)
print("Уникальные пациенты Второго: ", doc_2.unique_patient())
print("Все пациенты Второго: ", doc_2.get_patient())

CD = CommonPatients(doc_1, doc_2)
print("Общие пациенты: ", CD.common_patients())
