class Role:
    def __init__(self):
        self._students = []
        self._tutors = []

    def add_student(self, student):
        self._students.append(student)

    def add_tutor(self, tutor):
        self._tutors.append(tutor)

    @property
    def student_count(self):
        return len(self._students)

    @property
    def tutor_count(self):
        return len(self._tutors)