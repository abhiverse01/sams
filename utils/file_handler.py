import csv
import os
from models.student import Student

DATA_FILE = os.path.join("data", "students.csv")

def save_students_to_file(students):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Grade', 'Subjects'])
        for student in students.values():
            subjects_str = ','.join(f"{k}:{v}" for k, v in student.subjects.items())
            writer.writerow([student.id, student.name, student.grade, subjects_str])

def load_students_from_file():
    students = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                if len(row) < 4:
                    continue
                id, name, grade, subjects = row
                student = Student(id, name, grade)
                if subjects:
                    for subject in subjects.split(','):
                        if ':' in subject:
                            subj, mark = subject.split(':')
                            student.add_grade(subj.strip(), float(mark.strip()))
                students[id] = student
    return students
