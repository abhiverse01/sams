# tests/test_student.py

import pytest 
from models.student import Student

def test_student_initialization():
    student = Student("S101", "alice mack", "10")
    assert student.id == "S101"
    assert student.name == "Alice Mack"
    assert student.grade == "10"
    assert student.subjects == {}

def test_add_grade_and_average():
    student = Student("S102", "bob stone", "11")
    student.add_grade("Math", 85)
    student.add_grade("Science", "90.5")

    assert len(student.subjects) == 2
    assert student.subjects["Math"] == 85.0
    assert student.get_average() == 87.75

def test_get_average_no_grades():
    student = Student("S103", "charlie day", "12")
    assert student.get_average() == 0.0
    
def test_to_dict_method():
    student = Student('S104', 'diana prince', '10')
    student.add_grade('English', 92)
    data = student.to_dict()

    assert data['id'] == 'S104'
    assert "subjects" in data
    assert "average" in data
    assert data['average'] == 92.0
