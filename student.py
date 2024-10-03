from .person import Person
from .role import Role

class Student(Person, Role):
    def __init__(self, name="No Name", surname="No Surname", email="No Email", phone_number="No Phone", registration_date="No Date"):
        Person.__init__(self, name, surname)
        Role.__init__(self)
        self._email = email
        self._phone_number = phone_number
        self._registration_date = registration_date
        self.add_student(self)

    @property
    def email(self):
        return self._email

    @staticmethod
    def school_info():
        return "This is an online tutoring school."

    def set_data(self, name, surname, email, phone_number, registration_date):
        self.name = name
        self._surname = surname
        self._email = email
        self._phone_number = phone_number
        self._registration_date = registration_date

    def __str__(self):
        return f"Student: {self.name} {self._surname}, Email: {self.email}, Phone: {self._phone_number}, Registered: {self._registration_date}"