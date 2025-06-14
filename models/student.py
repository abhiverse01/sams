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
            return 0.0
        return sum(self.subjects.values()) / len(self.subjects)
