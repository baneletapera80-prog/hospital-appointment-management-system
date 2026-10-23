class Patient:
    def __init__(self, id, name, phone, email, age):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "age": self.age
        }

class Doctor:
    def __init__(self, id, name, specialization, available_days):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.available_days = available_days

    def to_dict(self):
        return {
            "name": self.name,
            "specialization": self.specialization,
            "available_days": self.available_days
        }

class Appointment:
    def __init__(self, id, patient_name, doctor_name, date, time, status="Pending"):
        self.id = id
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date
        self.time = time
        self.status = status

    def to_dict(self):
        return {
            "patient_name": self.patient_name,
            "doctor_name": self.doctor_name,
            "date": self.date,
            "time": self.time,
            "status": self.status
        }