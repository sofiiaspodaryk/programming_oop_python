from .person import Person
from .role import Role

class Tutor(Person, Role):
    def __init__(self, name="No Name", surname="No Surname", email="No Email", phone_number="No Phone", hire_date="No Date", subject="No Subject"):
        Person.__init__(self, name, surname)
        Role.__init__(self)
        self._email = email
        self._phone_number = phone_number
        self._hire_date = hire_date
        self._subject = subject
        self.add_tutor(self)

    @property
    def subject(self):
        return self._subject

    @staticmethod
    def school_info():
        return "This is an online tutoring school."

    def set_data(self, name, surname, email, phone_number, hire_date, subject):
        self.name = name
        self._surname = surname
        self._email = email
        self._phone_number = phone_number
        self._hire_date = hire_date
        self._subject = subject

    def __str__(self):
        return f"Tutor: {self.name} {self._surname}, Email: {self._email}, Phone: {self._phone_number}, Hired: {self._hire_date}, Subject: {self._subject}"