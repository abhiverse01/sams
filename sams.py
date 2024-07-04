import os
import csv
from datetime import datetime

class Student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade
        self.subjects = {}

    def add_grade(self, subject, grade):
        self.subjects[subject] = grade

    def get_average(self):
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)

class GradeManagementSystem:
    def __init__(self):
        self.students = {}
        self.load_data()

    def add_student(self, id, name, grade):
        if id not in self.students:
            self.students[id] = Student(id, name, grade)
            print(f"Student {name} added successfully.")
        else:
            print("Student ID already exists.")

    def add_grade(self, student_id, subject, grade):
        if student_id in self.students:
            self.students[student_id].add_grade(subject, grade)
            print(f"Grade added for {self.students[student_id].name} in {subject}.")
        else:
            print("Student not found.")

    def get_student_average(self, student_id):
        if student_id in self.students:
            avg = self.students[student_id].get_average()
            print(f"Average grade for {self.students[student_id].name}: {avg:.2f}")
        else:
            print("Student not found.")

    def generate_report(self):
        report = []
        for student in self.students.values():
            report.append({
                'ID': student.id,
                'Name': student.name,
                'Grade': student.grade,
                'Average': student.get_average()
            })
        return report

    def save_data(self):
        with open('students.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Grade', 'Subjects'])
            for student in self.students.values():
                writer.writerow([student.id, student.name, student.grade, 
                                 ','.join(f"{k}:{v}" for k, v in student.subjects.items())])
        print("Data saved successfully.")

    def load_data(self):
        if os.path.exists('students.csv'):
            with open('students.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    id, name, grade, subjects = row
                    self.students[id] = Student(id, name, grade)
                    if subjects:
                        for subject in subjects.split(','):
                            subj, grade = subject.split(':')
                            self.students[id].add_grade(subj, float(grade))
            print("Data loaded successfully.")
        else:
            print("No existing data found.")

    def export_report(self):
        report = self.generate_report()
        filename = f"student_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ID', 'Name', 'Grade', 'Average'])
            writer.writeheader()
            writer.writerows(report)
        print(f"Report exported to {filename}")

def main():
    gms = GradeManagementSystem()

    while True:
        print("\n--- Student Grade Management System ---")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Get Student Average")
        print("4. Generate Report")
        print("5. Export Report")