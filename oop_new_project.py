class Person:
    def __init__(self, name="No Name", surname="No Surname"):
        self._name = name
        self._surname = surname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    def __str__(self):
        return f"Person: {self._name} {self._surname}"


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


class Lesson:
    def __init__(self, time="No Time", tutor=None, student=None, price=0, office="No Location"):
        self._time = time
        self._tutor = tutor
        self._student = student
        self._price = price
        self._office = office

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if not value:
            raise ValueError("Time cannot be empty")
        self._time = value

    def set_data(self, time, tutor, student, price, office):
        self.time = time
        self._tutor = tutor
        self._student = student
        self._price = price
        self._office = office

    def __str__(self):
        return f"Lesson: {self._time}, Tutor: {self._tutor}, Student: {self._student}, Price: {self._price}, Office: {self._office}"


class Feedback:
    def __init__(self, date="No Date", text="No Text", student=None, tutor=None):
        self._date = date
        self._text = text
        self._student = student
        self._tutor = tutor

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not value:
            raise ValueError("Date cannot be empty")
        self._date = value

    def set_data(self, date, text, student, tutor):
        self.date = date
        self._text = text
        self._student = student
        self._tutor = tutor

    def __str__(self):
        return f"Feedback: {self._date}, Text: {self._text}, Student: {self._student}, Tutor: {self._tutor}"


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


if __name__ == "__main__":
    student1 = Student("Alice", "Smith", "alice@example.com", "123456789", "2023-01-01")
    tutor1 = Tutor("John", "Doe", "john@example.com", "987654321", "2022-01-01", "Math")
    lesson1 = Lesson("10:00 AM", tutor1, student1, 50, "Room 101")
    feedback1 = Feedback("2023-01-02", "Great lesson!", student1, tutor1)
    online_student1 = OnlineStudent("Bob", "Brown", "bob@example.com", "555555555", "2023-02-01", "Zoom")
    part_time_tutor1 = PartTimeTutor("Jane", "Doe", "jane@example.com", "444444444", "2022-02-01", "Physics", 20)


    student1.set_data("Alice", "Smith", "alice_new@example.com", "123456789", "2023-01-01")
    tutor1.set_data("John", "Doe", "john_new@example.com", "987654321", "2022-01-01", "Math")
    lesson1.set_data("11:00 AM", tutor1, student1, 60, "Room 102")
    feedback1.set_data("2023-01-03", "Excellent lesson!", student1, tutor1)
    online_student1.set_data("Bob", "Brown", "bob_new@example.com", "555555555", "2023-02-01", "Teams")
    part_time_tutor1.set_data("Jane", "Doe", "jane_new@example.com", "444444444", "2022-02-01", "Physics", 25)

    print(student1)
    print(tutor1)
    print(lesson1)
    print(feedback1)
    print(online_student1)
    print(part_time_tutor1)

    print(Student.school_info())
    print(Tutor.school_info())

    Student.student_count_info()
    Tutor.tutor_count_info()