from oop.student import Student
from oop.tutor import Tutor
from oop.lesson import Lesson
from oop.feedback import Feedback
from oop.online_student import OnlineStudent
from oop.part_time_tutor import PartTimeTutor

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
    part_time_tutor1.set_data("Jane", "Doe", "jane_new@example.com", "444444444", "2022-01-01", "Physics", 25)

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