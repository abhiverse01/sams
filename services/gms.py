from models.student import Student
from utils.file_handler import load_students_from_file, save_students_to_file

class GradeManagementSystem:
    def __init__(self):
        self.students = load_students_from_file()

    def student_exists(self, student_id):
        return student_id in self.students

    def add_student(self, id, name, grade):
        if id in self.students:
            return "Student ID already exists."
        self.students[id] = Student(id, name, grade)
        save_students_to_file(self.students)
        return f"Student {name} added successfully."

    def remove_student(self, id):
        if id not in self.students:
            return "Student not found."
        del self.students[id]
        save_students_to_file(self.students)
        return f"Student ID {id} removed successfully."

    def update_student(self, id, name=None, grade=None):
        if id not in self.students:
            return "Student not found."
        student = self.students[id]
        if name:
            student.name = name
        if grade:
            student.grade = grade
        save_students_to_file(self.students)
        return f"Student ID {id} updated successfully."

    def add_grade(self, student_id, subject, grade):
        if student_id not in self.students:
            return "Student not found."
        try:
            self.students[student_id].add_grade(subject, float(grade))
            save_students_to_file(self.students)
            return f"Grade added for {self.students[student_id].name} in {subject}."
        except ValueError:
            return "Invalid grade value. Please enter a numeric grade."

    def get_student_average(self, student_id):
        if student_id not in self.students:
            return "Student not found."
        avg = self.students[student_id].get_average()
        return f"Average grade for {self.students[student_id].name}: {avg:.2f}"

    def display_all_students(self):
        if not self.students:
            return ["No students found."]
        return [
            f"ID: {s.id}, Name: {s.name}, Grade: {s.grade}, Subjects: {s.subjects}"
            for s in self.students.values()
        ]
