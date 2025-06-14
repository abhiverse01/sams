import customtkinter as ctk
from PIL import Image
import os
from sams import GradeManagementSystem

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SAMS")
        self.geometry("800x600")
        self.gms = GradeManagementSystem()
        self.create_widgets()

    def create_widgets(self):
        # Load and set background image
        bg_image_path = "assets/SAMSbg.png"  # Update the path to your image
        if os.path.exists(bg_image_path):
            bg_image = Image.open(bg_image_path)
            bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
            self.bg_image = ctk.CTkImage(bg_image)
            self.bg_label = ctk.CTkLabel(self, image=self.bg_image)
            self.bg_label.place(relwidth=1, relheight=1)

        # Create a container for frames
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.place(relwidth=1, relheight=1)

        self.frames = {}
        for F in (HomeFrame, SAMSFrame, UpdateFrame, RemoveFrame):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomeFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class HomeFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.header_frame = ctk.CTkFrame(self, height=60, corner_radius=0, fg_color="#003366")
        self.header_frame.pack(fill="x")
        self.header = ctk.CTkLabel(self.header_frame, text="Welcome to SAMS", font=("Arial", 24, "bold"), text_color="white")
        self.header.place(relx=0.5, rely=0.5, anchor="center")

        self.card_frame = ctk.CTkFrame(self, width=300, height=200, corner_radius=15, fg_color="white")
        self.card_frame.pack(pady=50, padx=20)
        self.card_label = ctk.CTkLabel(self.card_frame, text="SAMS", font=("Arial", 18, "bold"), text_color="#333333")
        self.card_label.pack(pady=20)
        self.card_button = ctk.CTkButton(self.card_frame, text="Go to SAMS", command=lambda: self.controller.show_frame("SAMSFrame"), width=120, height=40, corner_radius=20, fg_color="#003366", text_color="white")
        self.card_button.pack(pady=10)

        self.footer_frame = ctk.CTkFrame(self, height=30, corner_radius=0, fg_color="#003366")
        self.footer_frame.pack(side="bottom", fill="x")
        self.footer = ctk.CTkLabel(self.footer_frame, text="Abhishek Shah | 2024", font=("Arial", 12), text_color="white")
        self.footer.place(relx=0.5, rely=0.5, anchor="center")

class SAMSFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.header_frame = ctk.CTkFrame(self, height=60, corner_radius=0, fg_color="#003366")
        self.header_frame.pack(fill="x")
        self.header = ctk.CTkLabel(self.header_frame, text="Student Account Management System", font=("Arial", 20, "bold"), text_color="white")
        self.header.place(relx=0.5, rely=0.5, anchor="center")

        self.label_id = ctk.CTkLabel(self, text="Student ID:", font=("Arial", 14))
        self.label_id.pack(padx=10, pady=5)
        self.entry_id = ctk.CTkEntry(self, font=("Arial", 14))
        self.entry_id.pack(padx=10, pady=5)

        self.label_name = ctk.CTkLabel(self, text="Student Name:", font=("Arial", 14))
        self.label_name.pack(padx=10, pady=5)
        self.entry_name = ctk.CTkEntry(self, font=("Arial", 14))
        self.entry_name.pack(padx=10, pady=5)

        self.label_grade = ctk.CTkLabel(self, text="Student Grade:", font=("Arial", 14))
        self.label_grade.pack(padx=10, pady=5)
        self.entry_grade = ctk.CTkEntry(self, font=("Arial", 14))
        self.entry_grade.pack(padx=10, pady=5)

        self.button_add = ctk.CTkButton(self, text="Add Student", font=("Arial", 14), command=self.add_student)
        self.button_add.pack(pady=10)

        self.text_display = ctk.CTkTextbox(self, width=700, height=250, font=("Arial", 12))
        self.text_display.pack(pady=10)

        self.button_display = ctk.CTkButton(self, text="Display All Students", font=("Arial", 14), command=self.display_all_students)
        self.button_display.pack(pady=10)

        self.button_update = ctk.CTkButton(self, text="Update Student", font=("Arial", 14), command=lambda: self.controller.show_frame("UpdateFrame"))
        self.button_update.pack(pady=10)

        self.button_remove = ctk.CTkButton(self, text="Remove Student", font=("Arial", 14), command=lambda: self.controller.show_frame("RemoveFrame"))
        self.button_remove.pack(pady=10)

    def add_student(self):
        student_id = self.entry_id.get()
        student_name = self.entry_name.get()
        student_grade = self.entry_grade.get()

        if student_id and student_name and student_grade:
            response = self.controller.gms.add_student(student_id, student_name, student_grade)
            self.text_display.insert(ctk.END, response + "\n")
            self.entry_id.delete(0, ctk.END)
            self.entry_name.delete(0, ctk.END)
            self.entry_grade.delete(0, ctk.END)
        else:
            self.text_display.insert(ctk.END, "Please fill in all fields.\n")

    def display_all_students(self):
        self.text_display.delete("1.0", ctk.END)
        students = self.controller.gms.display_all_students()
        for student in students:
            self.text_display.insert(ctk.END, f"{student}\n")

class UpdateFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.header_frame = ctk.CTkFrame(self, height=60, corner_radius=0, fg_color="#003366")
        self.header_frame.pack(fill="x")
        self.header = ctk.CTkLabel(self.header_frame, text="Update Student Information", font=("Arial", 20, "bold"), text_color="white")
        self.header.place(relx=0.5, rely=0.5, anchor="center")

        self.label_id = ctk.CTkLabel(self, text="Student ID:", font=("Arial", 14))
        self.label_id.pack(padx=10, pady=5)
        self.entry_id = ctk.CTkEntry(self, font=("Arial", 14))
        self.entry_id.pack(padx=10, pady=5)

        self.label_name = ctk.CTkLabel(self, text="New Student Name (Optional):", font=("Arial", 14))
        self.label_name.pack(padx=10, pady=5)
        self.entry_name = ctk.CTkEntry(self, font=("Arial", 14))
        self.entry_name.pack(padx=10, pady=5)

        self.label_grade = ctk.CTkLabel(self, text="New Student Grade (Optional):", font=("Arial", 14))
        self.label_grade.pack(padx=10, pady=5)
        self.entry_grade = ctk.CTkEntry(self, font=("Arial", 14))
        self.entry_grade.pack(padx=10, pady=5)

        self.button_update = ctk.CTkButton(self, text="Update Student", font=("Arial", 14), command=self.update_student)
        self.button_update.pack(pady=10)

    def update_student(self):
        student_id = self.entry_id.get()
        student_name = self.entry_name.get()
        student_grade = self.entry_grade.get()

        if student_id:
            response = self.controller.gms.update_student(student_id, student_name, student_grade)
            self.entry_id.delete(0, ctk.END)
            self.entry_name.delete(0, ctk.END)
            self.entry_grade.delete(0, ctk.END)
            self.controller.show_frame("SAMSFrame")
        else:
            self.controller.frames["SAMSFrame"].text_display.insert(ctk.END, "Please provide a valid Student ID.\n")

class RemoveFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.header_frame = ctk.CTkFrame(self, height=60, corner_radius=0, fg_color="#003366")
        self.header_frame.pack(fill="x")
        self.header = ctk.CTkLabel(self.header_frame, text="Remove Student", font=("Arial", 20, "bold"), text_color="white")
        self.header.place(relx=0.5, rely=0.5, anchor="center")

        self.label_id = ctk.CTkLabel(self, text="Student ID:", font=("Arial", 14))
        self.label_id.pack(padx=10, pady=5)
        self.entry_id = ctk.CTkEntry(self, font=("Arial", 14))
        self.entry_id.pack(padx=10, pady=5)

        self.button_remove = ctk.CTkButton(self, text="Remove Student", font=("Arial", 14), command=self.remove_student)
        self.button_remove.pack(pady=10)

    def remove_student(self):
        student_id = self.entry_id.get()

        if student_id:
            response = self.controller.gms.remove_student(student_id)
            self.entry_id.delete(0, ctk.END)
            self.controller.show_frame("SAMSFrame")
        else:
            self.controller.frames["SAMSFrame"].text_display.insert(ctk.END, "Please provide a valid Student ID.\n")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
