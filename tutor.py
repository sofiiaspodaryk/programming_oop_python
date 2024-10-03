from .person import Person

class Tutor(Person):
    tutor_count = 0

    def __init__(self, name="No Name", surname="No Surname", email="No Email", phone_number="No Phone", hire_date="No Date", subject="No Subject"):
        super().__init__(name, surname)
        self._email = email
        self._phone_number = phone_number
        self._hire_date = hire_date
        self._subject = subject
        Tutor.tutor_count += 1

    @property
    def subject(self):
        return self._subject

    @staticmethod
    def school_info():
        return "This is an online tutoring school."

    @classmethod
    def tutor_count_info(cls):
        print(f"Total tutors: {cls.tutor_count}")

    def set_data(self, name, surname, email, phone_number, hire_date, subject):
        self.name = name
        self._surname = surname
        self._email = email
        self._phone_number = phone_number
        self._hire_date = hire_date
        self._subject = subject

    def __str__(self):
        return f"Tutor: {self.name} {self._surname}, Email: {self._email}, Phone: {self._phone_number}, Hired: {self._hire_date}, Subject: {self._subject}"