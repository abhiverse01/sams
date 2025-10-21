import pytest
from models.student import Student

@pytest.fixture
def sample_student():
    """Fixture that returns a pre-configured Student object"""
    student = Student("S200", "test user", "9")
    student.add_grade("Math", 80)
    student.add_grade("Science", 90)
    return student
