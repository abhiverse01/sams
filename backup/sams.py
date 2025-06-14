import csv
import os
from datetime import datetime

class Student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade
        self.subjects = {}

    def add_grade(self, subject, grade):
        self.subjects[subject] = float(grade)

    def get_average(self):
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)

class GradeManagementSystem:
    def __init__(self):
        self.students = {}
        self.load_data()

    def add_student(self, id, name, grade):
        if id in self.students:
            return "Student ID already exists."
        self.students[id] = Student(id, name, grade)
        return f"Student {name} added successfully."

    def remove_student(self, id):
        if id not in self.students:
            return "Student not found."
        del self.students[id]
        return f"Student ID {id} removed successfully."

    def update_student(self, id, name=None, grade=None):
        if id not in self.students:
            return "Student not found."
        student = self.students[id]
        if name:
            student.name = name
        if grade:
            student.grade = grade
        return f"Student ID {id} updated successfully."

    def add_grade(self, student_id, subject, grade):
        if student_id not in self.students:
            return "Student not found."
        try:
            self.students[student_id].add_grade(subject, float(grade))
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
        return [f"ID: {s.id}, Name: {s.name}, Grade: {s.grade}, Subjects: {s.subjects}" for s in self.students.values()]

    def save_data(self):
        with open('students.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Grade', 'Subjects'])
            for student in self.students.values():
                writer.writerow([student.id, student.name, student.grade, ','.join(f"{k}:{v}" for k, v in student.subjects.items())])

    def load_data(self):
        if os.path.exists('students.csv'):
            with open('students.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    id, name, grade, subjects = row
                    new_student = Student(id, name, grade)
                    self.students[id] = new_student
                    if subjects:
                        for subject in subjects.split(','):
                            subj, grade = subject.split(':')
                            new_student.add_grade(subj, float(grade))
