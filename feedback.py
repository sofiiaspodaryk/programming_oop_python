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