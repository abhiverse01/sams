from models.student import Student
from utils.file_handler import load_students_from_file, save_students_to_file


# Grade Management System Core Logic
class GradeManagementSystem:
    def __init__(self):
        # Ensure we always get a dict structure
        self.students = load_students_from_file() or {}

    # Utility to check if student exists
    def student_exists(self, student_id):
        return student_id in self.students

    # Add new student with basic validation
    def add_student(self, id, name, grade):
        if not all([id, name, grade]):
            return {"success": False, "message": "All fields (ID, name, grade) are required."}

        if id in self.students:
            return {"success": False, "message": "Student ID already exists."}

        self.students[id] = Student(id, name, grade)
        save_students_to_file(self.students)
        return {"success": True, "message": f"Student {name} added successfully."}

    # Remove student safely
    def remove_student(self, id):
        if id not in self.students:
            return {"success": False, "message": "Student not found."}

        del self.students[id]
        save_students_to_file(self.students)
        return {"success": True, "message": f"Student ID {id} removed successfully."}

    # Update student name or grade (no-op protection)
    def update_student(self, id, name=None, grade=None):
        if id not in self.students:
            return {"success": False, "message": "Student not found."}

        student = self.students[id]
        updated = False

        if name and name != student.name:
            student.name = name
            updated = True

        if grade and grade != student.grade:
            student.grade = grade
            updated = True

        if not updated:
            return {"success": False, "message": "No changes were made."}

        save_students_to_file(self.students)
        return {"success": True, "message": f"Student ID {id} updated successfully."}

    # Add a grade to a student's subject
    def add_grade(self, student_id, subject, grade):
        if student_id not in self.students:
            return {"success": False, "message": "Student not found."}

        if not subject or grade is None:
            return {"success": False, "message": "Subject and grade are required."}

        try:
            self.students[student_id].add_grade(subject, float(grade))
            save_students_to_file(self.students)
            return {
                "success": True,
                "message": f"Grade added for {self.students[student_id].name} in {subject}."
            }
        except ValueError:
            return {"success": False, "message": "Invalid grade value. Please enter a numeric grade."}

    # Fetch a student's average cleanly
    def get_student_average(self, student_id):
        if student_id not in self.students:
            return {"success": False, "message": "Student not found."}

        avg = self.students[student_id].get_average()
        return {
            "success": True,
            "message": f"Average grade for {self.students[student_id].name}: {avg:.2f}",
            "average": avg
        }

    # Get a single student's full record
    def get_student(self, student_id):
        if student_id not in self.students:
            return {"success": False, "message": "Student not found."}

        student = self.students[student_id]
        data = {
            "id": student.id,
            "name": student.name,
            "grade": student.grade,
            "subjects": student.subjects,
            "average": student.get_average(),
        }
        return {"success": True, "student": data}

    # Get all students (wrapper of display_all_students)
    def get_all_students(self):
        # This simply reuses your existing display_all_students() logic
        return self.display_all_students()

    
    # Return structured data for UI rendering
    def display_all_students(self):
        if not self.students:
            return {"success": False, "students": [], "message": "No students found."}

        student_list = [
            {
                "id": s.id,
                "name": s.name,
                "grade": s.grade,
                "subjects": s.subjects,
                "average": s.get_average()
            }
            for s in self.students.values()
        ]
        return {"success": True, "students": student_list}
