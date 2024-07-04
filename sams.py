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
        if id not in self.students:
            self.students[id] = Student(id, name, grade)
            print(f"Student {name} added successfully.")
        else:
            print("Student ID already exists.")

    def add_grade(self, student_id, subject, grade):
        if student_id in self.students:
            try:
                grade = float(grade)
                self.students[student_id].add_grade(subject, grade)
                print(f"Grade added for {self.students[student_id].name} in {subject}.")
            except ValueError:
                print("Invalid grade value. Please enter a numeric grade.")
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
        try:
            with open('students.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'Name', 'Grade', 'Subjects'])
                for student in self.students.values():
                    writer.writerow([student.id, student.name, student.grade, 
                                     ','.join(f"{k}:{v}" for k, v in student.subjects.items())])
            print("Data saved successfully.")
        except IOError as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        if os.path.exists('students.csv'):
            try:
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
            except IOError as e:
                print(f"Error loading data: {e}")
            except ValueError as e:
                print(f"Error parsing data: {e}")
        else:
            print("No existing data found.")

    def export_report(self):
        report = self.generate_report()
        filename = f"student_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['ID', 'Name', 'Grade', 'Average'])
                writer.writeheader()
                writer.writerows(report)
            print(f"Report exported to {filename}")
        except IOError as e:
            print(f"Error exporting report: {e}")

def main():
    gms = GradeManagementSystem()

    while True:
        print("\n--- Student Grade Management System ---")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Get Student Average")
        print("4. Generate Report")
        print("5. Export Report")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            gms.add_student(id, name, grade)
        elif choice == '2':
            student_id = input("Enter student ID: ")
            subject = input("Enter subject: ")
            grade = input("Enter grade: ")
            gms.add_grade(student_id, subject, grade)
        elif choice == '3':
            student_id = input("Enter student ID: ")
            gms.get_student_average(student_id)
        elif choice == '4':
            report = gms.generate_report()
            for record in report:
                print(record)
        elif choice == '5':
            gms.export_report()
        elif choice == '6':
            gms.save_data()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
