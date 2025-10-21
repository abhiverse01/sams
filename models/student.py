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
        try:
            self.subjects[subject.strip().title()] = float(grade)
        except ValueError:
            raise ValueError(f"Invalid grade value for subject' {subject}': {grade}")

    def get_average(self):
        """Return the average grade score across all subjects."""
        if not self.subjects:
            return 0.0
        return sum(self.subjects.values()) / len(self.subjects)
    
    def __repr__(self) -> str:
        """Developer-friendly representation"""
        return f"Student({self.id}, {self.name}, Grade: {self.grade}, Subjects: {len(self.subjects)})"

    def to_dict(self) -> Dict[str, Union[str, float, dict]]:
        """Convert the student record to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "grade": self.grade,
            "subjects": self.subjects,
            "average": self.get_average()
        }