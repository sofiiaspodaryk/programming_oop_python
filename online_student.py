from .student import Student

class OnlineStudent(Student):
    def __init__(self, name="No Name", surname="No Surname", email="No Email", phone_number="No Phone", registration_date="No Date", platform="No Platform"):
        super().__init__(name, surname, email, phone_number, registration_date)
        self._platform = platform

    @property
    def platform(self):
        return self._platform

    def set_data(self, name, surname, email, phone_number, registration_date, platform):
        super().set_data(name, surname, email, phone_number, registration_date)
        self._platform = platform

    def __str__(self):
        return f"OnlineStudent: {self.name} {self._surname}, Email: {self.email}, Phone: {self._phone_number}, Registered: {self._registration_date}, Platform: {self._platform}"