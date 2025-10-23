import customtkinter as ctk
from tkinter import Toplevel, Label, Button

class SAMSFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#2b2b44")  # dark background for consistency
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Header Frame
        self.header_frame = ctk.CTkFrame(self, height=70, fg_color="#001f4d", corner_radius=12)
        self.header_frame.pack(fill="x", padx=20, pady=(20, 15))

        self.header = ctk.CTkLabel(
            self.header_frame,
            text="Student Account Management System",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color="white"
        )
        self.header.place(relx=0.5, rely=0.5, anchor="center")

        # Form Fields
        label_font = ctk.CTkFont(size=16)
        entry_font = ctk.CTkFont(size=16)

        self.label_id = ctk.CTkLabel(self, text="Student ID:", font=label_font, text_color="#cbd2f7")
        self.label_id.pack(padx=20, pady=(10, 3), anchor="w")
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

        self.label_name = ctk.CTkLabel(self, text="Student Name:", font=label_font, text_color="#cbd2f7")
        self.label_name.pack(padx=20, pady=(10, 3), anchor="w")
        self.entry_name = ctk.CTkEntry(
            self,
            font=entry_font,
            width=360,
            corner_radius=12,
            fg_color="#394171",
            text_color="white",
            placeholder_text="Enter Student Name"
        )
        self.entry_name.pack(padx=20, pady=(0, 10))

        self.label_grade = ctk.CTkLabel(self, text="Student Grade:", font=label_font, text_color="#cbd2f7")
        self.label_grade.pack(padx=20, pady=(10, 3), anchor="w")
        self.entry_grade = ctk.CTkEntry(
            self,
            font=entry_font,
            width=360,
            corner_radius=12,
            fg_color="#394171",
            text_color="white",
            placeholder_text="Enter Student Grade"
        )
        self.entry_grade.pack(padx=20, pady=(0, 15))

        # Buttons Frame for neat alignment
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(padx=20, pady=10, fill="x")

        btn_params = dict(width=180, height=45, corner_radius=20, font=ctk.CTkFont(size=16, weight="bold")) # type: ignore

        self.button_add = ctk.CTkButton(
            self.buttons_frame,
            text="Add Student",
            fg_color="#007acc",
            hover_color="#0099ff",
            **btn_params, # type: ignore
            command=self.add_student
        )
        self.button_add.grid(row=0, column=0, padx=10, pady=10)

        self.button_display = ctk.CTkButton(
            self.buttons_frame,
            text="Display All Students",
            fg_color="#007acc",
            hover_color="#0099ff",
            **btn_params, # type: ignore
            command=self.display_all_students
        )
        self.button_display.grid(row=0, column=1, padx=10, pady=10)

        self.button_update = ctk.CTkButton(
            self.buttons_frame,
            text="Update Student",
            fg_color="#004080",
            hover_color="#0059b3",
            **btn_params, # type: ignore
            command=lambda: self.controller.show_frame("UpdateFrame")
        )
        self.button_update.grid(row=1, column=0, padx=10, pady=10)

        self.button_remove = ctk.CTkButton(
            self.buttons_frame,
            text="Remove Student",
            fg_color="#a02c2c",
            hover_color="#d13f3f",
            **btn_params, # type: ignore
            command=lambda: self.controller.show_frame("RemoveFrame")
        )
        self.button_remove.grid(row=1, column=1, padx=10, pady=10)

        # Output Text Box with scrollbar
        self.text_display = ctk.CTkTextbox(
            self,
            width=740,
            height=220,
            font=ctk.CTkFont(size=14),
            corner_radius=12,
            fg_color="#394171",
            text_color="#e1e4ff"
        )
        self.text_display.pack(padx=20, pady=(15, 25))
        self.text_display.configure(state="disabled")  # read-only

    def add_student(self):
        # Clear previous messages
        self.text_display.delete("1.0", ctk.END)

        student_id = self.entry_id.get().strip()
        student_name = self.entry_name.get().strip()
        student_grade = self.entry_grade.get().strip()

        # Validate inputs
        if not student_id or not student_name or not student_grade:
            self.show_error_modal("All fields are required.")
            self.highlight_error(self.text_display, "Please fill in all fields.\n")
            return

        if not self.is_valid_grade(student_grade):
            self.show_error_modal("Invalid Grade format. Use A, B, C, or 0-100.")
            self.highlight_error(self.text_display, "Invalid Grade format.\n")
            return

        if self.controller.gms.student_exists(student_id):
            self.show_error_modal("Student ID already exists.")
            self.highlight_error(self.text_display, "Student ID must be unique.\n")
            return

        # Proceed to add student
        response = self.controller.gms.add_student(student_id, student_name, student_grade)

        # Extract message safely
        if isinstance(response, dict):
            message = response.get("message", str(response))
        else:
            message = str(response)

        # Display message in text box
        self.text_display.insert(ctk.END, message + "\n")

        # Show modal with message only
        self.show_info_modal("Success", message)

        # Clear entries
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
        widget.configure(fg_color="#330000")  # Dark red background for error highlight
        # Optionally, you can revert color after some time

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
        modal.grab_set()  # Make modal

        label = Label(modal, text=message, fg="white", bg=fg_color, font=("Arial", 14), wraplength=280)
        label.pack(pady=20)

        btn = Button(modal, text="OK", command=modal.destroy)
        btn.pack(pady=10)

    def display_all_students(self):
        self.text_display.configure(state="normal")
        self.text_display.delete("0.0", ctk.END)

        students = self.controller.gms.display_all_students()
        if students:
            for student in students:
                self.text_display.insert(ctk.END, f"• {student}\n")
        else:
            self.text_display.insert(ctk.END, "No students found.\n")

        self.text_display.configure(state="disabled")
