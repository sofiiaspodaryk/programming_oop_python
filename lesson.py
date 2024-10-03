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