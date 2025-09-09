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
    id_doc = 0
    queues = dict()

    def __init__(self, doctor):
        self.doctor = doctor
        self.patients = list()
        Queue.id_doc += 1
        self.id_doc = Queue.id_doc
        self.notes = dict()
        Queue.queues[self.id_doc] = self.patients

    def add_patients(self, patient):
        self.patients.append(patient)
        self.notes[self.id_doc] = self.patients
        return self.notes

    def get_patients(self):
        return [patient.name for patient in  self.patients]

    def get_queue(self):
        return [f"{self.id_doc} | {self.get_patients()}" for id_doc, patients in self.notes.items()]


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

queue_doc1 = Queue(doc_1)
queue_doc2 = Queue(doc_2)
queue_doc1.add_patients(patient_1)
queue_doc1.add_patients(patient_3)
queue_doc1.add_patients(patient_5)
queue_doc2.add_patients(patient_2)
queue_doc2.add_patients(patient_4)

print("Очередь 1 доктора: ", queue_doc1.get_queue())
print("Очередь 2 доктора: ", queue_doc2.get_queue())

