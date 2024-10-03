from .tutor import Tutor

class PartTimeTutor(Tutor):
    def __init__(self, name="No Name", surname="No Surname", email="No Email", phone_number="No Phone", hire_date="No Date", subject="No Subject", hours_per_week=0):
        super().__init__(name, surname, email, phone_number, hire_date, subject)
        self._hours_per_week = hours_per_week

    @property
    def hours_per_week(self):
        return self._hours_per_week

    def set_data(self, name, surname, email, phone_number, hire_date, subject, hours_per_week):
        super().set_data(name, surname, email, phone_number, hire_date, subject)
        self._hours_per_week = hours_per_week

    def __str__(self):
        return f"PartTimeTutor: {self.name} {self._surname}, Email: {self._email}, Phone: {self._phone_number}, Hired: {self._hire_date}, Subject: {self._subject}, Hours/Week: {self._hours_per_week}"