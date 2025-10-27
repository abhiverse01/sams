import customtkinter as ctk
from tkinter import Toplevel, Label, Button


class UpdateFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#2b2b44")
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Header Frame
        self.header_frame = ctk.CTkFrame(self, height=70, fg_color="#001f4d", corner_radius=12)
        self.header_frame.pack(fill="x", padx=20, pady=(20, 15))

        self.header = ctk.CTkLabel(
            self.header_frame,
            text="Update Student Information",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="white"
        )
        self.header.place(relx=0.5, rely=0.5, anchor="center")

        # Fonts for labels and entries
        label_font = ctk.CTkFont(size=16)
        entry_font = ctk.CTkFont(size=16)

        # Student ID
        self.label_id = ctk.CTkLabel(self, text="Student ID to Update:", font=label_font, text_color="#cbd2f7")
        self.label_id.pack(padx=20, pady=(15, 5), anchor="w")
        self.entry_id = ctk.CTkEntry(
            self,
            font=entry_font,
            width=360,
            corner_radius=12,
            fg_color="#394171",
            text_color="white",
            placeholder_text="Enter Student ID"
        )
        self.entry_id.pack(padx=20, pady=(0, 10))

        # New Name
        self.label_name = ctk.CTkLabel(self, text="New Name:", font=label_font, text_color="#cbd2f7")
        self.label_name.pack(padx=20, pady=(10, 5), anchor="w")
        self.entry_name = ctk.CTkEntry(
            self,
            font=entry_font,
            width=360,
            corner_radius=12,
            fg_color="#394171",
            text_color="white",
            placeholder_text="Enter New Name (optional)"
        )
        self.entry_name.pack(padx=20, pady=(0, 10))

        # New Grade
        self.label_grade = ctk.CTkLabel(self, text="New Grade:", font=label_font, text_color="#cbd2f7")
        self.label_grade.pack(padx=20, pady=(10, 5), anchor="w")
        self.entry_grade = ctk.CTkEntry(
            self,
            font=entry_font,
            width=360,
            corner_radius=12,
            fg_color="#394171",
            text_color="white",
            placeholder_text="Enter New Grade (optional)"
        )
        self.entry_grade.pack(padx=20, pady=(0, 15))

        # Buttons Frame
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(padx=20, pady=10, fill="x")

        btn_params = dict(width=180, height=45, corner_radius=20, font=ctk.CTkFont(size=16, weight="bold"))

        self.button_update = ctk.CTkButton(
            self.buttons_frame,
            text="Update Student",
            fg_color="#007acc",
            hover_color="#0099ff",
            **btn_params, # type: ignore
            command=self.update_student
        )
        self.button_update.grid(row=0, column=0, padx=10, pady=10)

        self.button_back = ctk.CTkButton(
            self.buttons_frame,
            text="Back to SAMS",
            fg_color="#a02c2c",
            hover_color="#d13f3f",
            **btn_params, # type: ignore
            command=lambda: self.controller.show_frame("SAMSFrame")
        )
        self.button_back.grid(row=0, column=1, padx=10, pady=10)

        # Output Textbox 
        self.text_display = ctk.CTkTextbox(
            self,
            width=700,
            height=150,
            font=ctk.CTkFont(size=14),
            corner_radius=12,
            fg_color="#394171",
            text_color="#e1e4ff"
        )
        self.text_display.pack(padx=20, pady=(15, 25))
        self.text_display.configure(state="disabled")

    def update_student(self):
        self.text_display.delete("1.0", ctk.END)

        student_id = self.entry_id.get().strip()
        new_name = self.entry_name.get().strip()
        new_grade = self.entry_grade.get().strip()

        if not student_id:
            self.show_error_modal("Student ID is required.")
            self.highlight_error(self.text_display, "Please enter the student ID.\n")
            return

        if not new_name and not new_grade:
            self.show_error_modal("Provide at least one field to update.")
            self.highlight_error(self.text_display, "Please enter new name or new grade.\n")
            return

        if new_grade and not self.is_valid_grade(new_grade):
            self.show_error_modal("Invalid Grade format. Use A, B, C, or 0-100.")
            self.highlight_error(self.text_display, "Invalid Grade format.\n")
            return

        if not self.controller.gms.student_exists(student_id):
            self.show_error_modal("Student ID does not exist.")
            self.highlight_error(self.text_display, "No student found with this ID.\n")
            return

        result = self.controller.gms.update_student(student_id, new_name, new_grade)
        self.show_info_modal("Update Result", result)
        self.text_display.insert(ctk.END, result + "\n")

        self.entry_id.delete(0, ctk.END)
        self.entry_name.delete(0, ctk.END)
        self.entry_grade.delete(0, ctk.END)


    def is_valid_grade(self, grade):
        valid_grades = ['A', 'B', 'C', 'D', 'F']
        if grade.upper() in valid_grades:
            return True
        try:
            score = int(grade)
            return 0 <= score <= 100
        except ValueError:
            return False

    def highlight_error(self, widget, message):
        widget.insert(ctk.END, message)
        widget.configure(fg_color="#330000")

    def show_error_modal(self, message):
        self.show_modal("Error", message, fg_color="#cc0000")

    def show_info_modal(self, title, message):
        self.show_modal(title, message, fg_color="#008000")

    def show_modal(self, title, message, fg_color="#222222"):
        modal = Toplevel(self)
        modal.title(title)
        modal.geometry("300x150")
        modal.configure(bg=fg_color)
        modal.resizable(False, False)
        modal.grab_set()

        label = Label(modal, text=message, fg="white", bg=fg_color, font=("Arial", 14), wraplength=280)
        label.pack(pady=20)

        btn = Button(modal, text="OK", command=modal.destroy)
        btn.pack(pady=10)

"""
The Update Frame for the Student Administration Management System (SAMS).

"""