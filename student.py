
from .person import Person

class Student(Person):
    student_count = 0

    def __init__(self, name="No Name", surname="No Surname", email="No Email", phone_number="No Phone", registration_date="No Date"):
        super().__init__(name, surname)
        self._email = email
        self._phone_number = phone_number
        self._registration_date = registration_date
        Student.student_count += 1

    @property
    def email(self):
        return self._email

    @staticmethod
    def school_info():
        return "This is an online tutoring school."

    @classmethod
    def student_count_info(cls):
        print(f"Total students: {cls.student_count}")

    def set_data(self, name, surname, email, phone_number, registration_date):
        self.name = name
        self._surname = surname
        self._email = email
        self._phone_number = phone_number
        self._registration_date = registration_date

    def __str__(self):
        return f"Student: {self.name} {self._surname}, Email: {self.email}, Phone: {self._phone_number}, Registered: {self._registration_date}"