from typing import Dict, Union
class Student:
    """
    Represents a student record in SAMS.

    Attributes:
        id (str): Unique student ID.
        name (str): Full name of the student.
        grade (str): Current class/grade level (e.g., '10', 'Grade 12').
        subjects (Dict[str, float]): Dictionary mapping subjects to their respective grades.
    """
    def __init__(self, id, name, grade):
        self.id = id.strip()
        self.name = name.strip().title()
        self.grade = grade.strip()
        self.subjects: Dict[str, float] = {}

    def add_grade(self, subject:str, grade: Union[int, float, str]) -> None:
        """Add or update a subject grade for the student."""
        self.subjects[subject] = float(grade)

    def get_average(self):
        if not self.subjects:
            return 0.0
        return sum(self.subjects.values()) / len(self.subjects)
