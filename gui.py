# sams/sams_gui.py
import customtkinter as ctk
from sams import GradeManagementSystem

class SAMSApp(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.gms = GradeManagementSystem()
        self.title("Student Account Management System")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        # Header
        self.header = ctk.CTkLabel(self, text="Student Account Management System", font=("Arial", 20))
        self.header.grid(row=0, column=0, columnspan=2, pady=20)

        # Widgets for adding student
        self.label_id = ctk.CTkLabel(self, text="Student ID:")
        self.label_id.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_id = ctk.CTkEntry(self)
        self.entry_id.grid(row=1, column=1, padx=10, pady=5)

        self.label_name = ctk.CTkLabel(self, text="Student Name:")
        self.label_name.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_name = ctk.CTkEntry(self)
        self.entry_name.grid(row=2, column=1, padx=10, pady=5)

        self.label_grade = ctk.CTkLabel(self, text="Student Grade:")
        self.label_grade.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_grade = ctk.CTkEntry(self)
        self.entry_grade.grid(row=3, column=1, padx=10, pady=5)

        self.button_add = ctk.CTkButton(self, text="Add Student", command=self.add_student)
        self.button_add.grid(row=4, column=0, columnspan=2, pady=10)

        # Widgets for displaying students
        self.text_display = ctk.CTkTextbox(self, width=600, height=200)
        self.text_display.grid(row=5, column=0, columnspan=2, pady=10)

        self.button_display = ctk.CTkButton(self, text="Display All Students", command=self.display_all_students)
        self.button_display.grid(row=6, column=0, columnspan=2, pady=10)

    def add_student(self):
        student_id = self.entry_id.get()
        student_name = self.entry_name.get()
        student_grade = self.entry_grade.get()

        if student_id and student_name and student_grade:
            self.gms.add_student(student_id, student_name, student_grade)
            self.entry_id.delete(0, ctk.END)
            self.entry_name.delete(0, ctk.END)
            self.entry_grade.delete(0, ctk.END)
        else:
            self.text_display.insert(ctk.END, "Please fill in all fields.\n")

    def display_all_students(self):
        self.text_display.delete("1.0", ctk.END)
        students = self.gms.display_all_students()
        for student in students:
            self.text_display.insert(ctk.END, f"{student}\n")

if __name__ == "__main__":
    gms = GradeManagementSystem()
    app = SAMSApp(None)
    app.mainloop()
