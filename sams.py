import os
import csv
from datetime import datetime

class Student:
    """
    Represents a student with an ID, name, grade, and subjects.

    Attributes:
        id (str): Unique student ID
        name (str): Student name
        grade (str): Student grade (e.g. "A", "B", etc.)
        subjects (dict): Dictionary of subjects with grades (e.g. {"Math": 90, "English": 85})

    Methods:
        add_grade(subject, grade): Adds a grade for a subject
        get_average(): Calculates the average grade for all subjects
    """
    def __init__(self, id, name, grade):
        """
        Initializes a Student object.

        Args:
            id (str): Unique student ID
            name (str): Student name
            grade (str): Student grade (e.g. "A", "B", etc.)
        """
        self.id = id
        self.name = name
        self.grade = grade
        self.subjects = {}

    def add_grade(self, subject, grade):
        """
        Adds a grade for a subject.

        Args:
            subject (str): Subject name (e.g. "Math", "English")
            grade (float): Grade for the subject (e.g. 90, 85)

        Example:
            student.add_grade("Math", 90)
        """
        self.subjects[subject] = float(grade)

    def get_average(self):
        """
        Calculates the average grade for all subjects.

        Returns:
            float: Average grade (e.g. 87.5)

        Example:
            student.get_average()  # returns 87.5
        """
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)

class GradeManagementSystem:
    """
    Manages a collection of Student objects and provides methods for adding students, grades, and generating reports.

    Attributes:
        students (dict): Dictionary of Student objects with IDs as keys

    Methods:
        add_student(id, name, grade): Adds a new Student object
        remove_student(id): Removes a Student object
        update_student(id, name, grade): Updates a Student's name or grade
        add_grade(student_id, subject, grade): Adds a grade for a subject
        get_student_average(student_id): Calculates the average grade for a student
        get_student_details(student_id): Retrieves details for a specific student
        display_all_students(): Displays all students and their details
        generate_report(): Generates a report with student information and averages
        export_report(): Exports the report to a CSV file
        save_data(): Saves the student data to a CSV file
        load_data(): Loads the student data from a CSV file
    """
    def __init__(self):
        """
        Initializes a GradeManagementSystem object.
        """
        self.students = {}
        self.load_data()

    def add_student(self, id, name, grade):
        """
        Adds a new Student object.

        Args:
            id (str): Unique student ID
            name (str): Student name
            grade (str): Student grade (e.g. "A", "B", etc.)

        Example:
            gms.add_student("12345", "John Doe", "A")
        """
        if id not in self.students:
            self.students[id] = Student(id, name, grade)
            print(f"Student {name} added successfully.")
        else:
            print("Student ID already exists.")

    def remove_student(self, id):
        """
        Removes a Student object.

        Args:
            id (str): Unique student ID

        Example:
            gms.remove_student("12345")
        """
        if id in self.students:
            del self.students[id]
            print(f"Student ID {id} removed successfully.")
        else:
            print("Student not found.")

    def update_student(self, id, name=None, grade=None):
        """
        Updates a Student's name or grade.

        Args:
            id (str): Unique student ID
            name (str, optional): New student name
            grade (str, optional): New student grade (e.g. "A", "B", etc.)

        Example:
            gms.update_student("12345", name="Jane Doe", grade="B")
        """
        if id in self.students:
            if name:
                self.students[id].name = name
            if grade:
                self.students[id].grade = grade
            print(f"Student ID {id} updated successfully.")
        else:
            print("Student not found.")

    def add_grade(self, student_id, subject, grade):
        """
        Adds a grade for a subject.

        Args:
            student_id (str): Student ID
            subject (str): Subject name (e.g. "Math", "English")
            grade (float): Grade for the subject (e.g. 90, 85)

        Example:
            gms.add_grade("12345", "Math", 90)
        """
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
        """
        Calculates the average grade for a student.

        Args:
            student_id (str): Student ID

        Returns:
            float: Average grade (e.g. 87.5)

        Example:
            gms.get_student_average("12345")  # returns 87.5
        """
        if student_id in self.students:
            avg = self.students[student_id].get_average()
            print(f"Average grade for {self.students[student_id].name}: {avg:.2f}")
        else:
            print("Student not found.")

    def get_student_details(self, student_id):
        """
        Retrieves details for a specific student.

        Args:
            student_id (str): Student ID

        Example:
            gms.get_student_details("12345")
        """
        if student_id in self.students:
            student = self.students[student_id]
            print(f"ID: {student.id}, Name: {student.name}, Grade: {student.grade}, Subjects: {student.subjects}")
        else:
            print("Student not found.")

    def display_all_students(self):
        """
        Displays all students and their details.

        Example:
            gms.display_all_students()
        """
        if self.students:
            for student in self.students.values():
                print(f"ID: {student.id}, Name: {student.name}, Grade: {student.grade}, Subjects: {student.subjects}")
        else:
            print("No students found.")

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
        print("2. Remove Student")
        print("3. Update Student")
        print("4. Add Grade")
        print("5. Get Student Average")
        print("6. Get Student Details")
        print("7. Display All Students")
        print("8. Generate Report")
        print("9. Export Report")
        print("10. Save Data")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            gms.add_student(id, name, grade)
        elif choice == '2':
            id = input("Enter student ID: ")
            gms.remove_student(id)
        elif choice == '3':
            id = input("Enter student ID: ")
            name = input("Enter new student name (or press enter to skip): ")
            grade = input("Enter new student grade (or press enter to skip): ")
            gms.update_student(id, name if name else None, grade if grade else None)
        elif choice == '4':
            student_id = input("Enter student ID: ")
            subject = input("Enter subject: ")
            grade = input("Enter grade: ")
            gms.add_grade(student_id, subject, grade)
        elif choice == '5':
            student_id = input("Enter student ID: ")
            gms.get_student_average(student_id)
        elif choice == '6':
            student_id = input("Enter student ID: ")
            gms.get_student_details(student_id)
        elif choice == '7':
            gms.display_all_students()
        elif choice == '8':
            report = gms.generate_report()
            for record in report:
                print(record)
        elif choice == '9':
            gms.export_report()
        elif choice == '10':
            gms.save_data()
        elif choice == '11':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
