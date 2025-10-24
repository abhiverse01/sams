import customtkinter as ctk
from tkinter import Toplevel, Label, Button


class SAMSFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#1e1e2f")  # Deep navy background
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # ---------- Layout Configuration ----------
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ---------- Header ----------
        self.header_frame = ctk.CTkFrame(self, height=80, fg_color="#0a1744", corner_radius=16)
        self.header_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        self.header = ctk.CTkLabel(
            self.header_frame,
            text="🎓 Student Account Management System",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color="white"
        )
        self.header.place(relx=0.5, rely=0.5, anchor="center")

        # ---------- Content Frame (Main Section) ----------
        self.content_frame = ctk.CTkFrame(self, fg_color="#2b2b44", corner_radius=16)
        self.content_frame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")

        self.content_frame.grid_columnconfigure(0, weight=1, uniform="half")
        self.content_frame.grid_columnconfigure(1, weight=1, uniform="half")
        self.content_frame.grid_rowconfigure(0, weight=1)

        # ---------- Left Side: Form Section ----------
        form_frame = ctk.CTkFrame(self.content_frame, fg_color="#323259", corner_radius=12)
        form_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        form_frame.grid_columnconfigure(0, weight=1)

        self._add_form_field(form_frame, "Student ID:", "Enter Student ID", row=0)
        self.entry_id = self._get_last_entry(form_frame)

        self._add_form_field(form_frame, "Student Name:", "Enter Student Name", row=1)
        self.entry_name = self._get_last_entry(form_frame)

        self._add_form_field(form_frame, "Student Grade:", "Enter Student Grade", row=2)
        self.entry_grade = self._get_last_entry(form_frame)

        # ---------- Buttons ----------
        buttons_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        buttons_frame.grid(row=3, column=0, pady=(20, 10))

        btn_params = dict(width=160, height=40, corner_radius=20, font=ctk.CTkFont(size=15, weight="bold"))

        self.button_add = ctk.CTkButton(
            buttons_frame,
            text="➕ Add Student",
            fg_color="#0078d7",
            hover_color="#339cff",
            command=self.add_student,
            **btn_params  # type: ignore
        )
        self.button_add.grid(row=0, column=0, padx=8, pady=6)

        self.button_display = ctk.CTkButton(
            buttons_frame,
            text="📋 Display All",
            fg_color="#0066cc",
            hover_color="#339cff",
            command=self.display_all_students,
            **btn_params  # type: ignore
        )
        self.button_display.grid(row=0, column=1, padx=8, pady=6)

        self.button_update = ctk.CTkButton(
            buttons_frame,
            text="✏️ Update Student",
            fg_color="#004080",
            hover_color="#0059b3",
            command=lambda: self.controller.show_frame("UpdateFrame"),
            **btn_params  # type: ignore
        )
        self.button_update.grid(row=1, column=0, padx=8, pady=6)

        self.button_remove = ctk.CTkButton(
            buttons_frame,
            text="🗑 Remove Student",
            fg_color="#a82c2c",
            hover_color="#d63b3b",
            command=lambda: self.controller.show_frame("RemoveFrame"),
            **btn_params  # type: ignore
        )
        self.button_remove.grid(row=1, column=1, padx=8, pady=6)

        # ---------- Right Side: Output Box ----------
        output_frame = ctk.CTkFrame(self.content_frame, fg_color="#33335c", corner_radius=12)
        output_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        output_label = ctk.CTkLabel(
            output_frame,
            text="📄 Student Records",
            font=ctk.CTkFont(size=17, weight="bold"),
            text_color="#bfc3ff"
        )
        output_label.pack(pady=(15, 5))

        self.text_display = ctk.CTkTextbox(
            output_frame,
            width=500,
            height=240,
            font=ctk.CTkFont(size=14),
            corner_radius=12,
            fg_color="#3a3a63",
            text_color="#e2e6ff"
        )
        self.text_display.pack(padx=15, pady=(0, 15), fill="both", expand=True)
        self.text_display.configure(state="disabled")

    # ---------------- Helper UI Methods ----------------
    def _add_form_field(self, frame, label_text, placeholder, row):
        label = ctk.CTkLabel(frame, text=label_text, font=ctk.CTkFont(size=15), text_color="#b3b9ff")
        label.grid(row=row * 2, column=0, sticky="w", padx=10, pady=(10, 4))

        entry = ctk.CTkEntry(
            frame,
            font=ctk.CTkFont(size=15),
            width=300,
            corner_radius=10,
            fg_color="#404070",
            text_color="white",
            placeholder_text=placeholder,
        )
        entry.grid(row=row * 2 + 1, column=0, padx=10, pady=(0, 8))

    def _get_last_entry(self, frame) -> ctk.CTkEntry:
        return list(frame.children.values())[-1]  # type: ignore

    # ---------------- Core Logic ----------------
    def add_student(self):
        self.text_display.configure(state="normal")
        self.text_display.delete("1.0", ctk.END)

        student_id = self.entry_id.get().strip()
        student_name = self.entry_name.get().strip()
        student_grade = self.entry_grade.get().strip()

        if not student_id or not student_name or not student_grade:
            self.show_error_modal("All fields are required.")
            self.text_display.insert(ctk.END, "⚠️ Please fill in all fields.\n")
            return

        if not self.is_valid_grade(student_grade):
            self.show_error_modal("Invalid grade format. Use A–F or 0–100.")
            self.text_display.insert(ctk.END, "⚠️ Invalid grade format.\n")
            return

        if self.controller.gms.student_exists(student_id):
            self.show_error_modal("Student ID already exists.")
            self.text_display.insert(ctk.END, "⚠️ Student ID must be unique.\n")
            return

        response = self.controller.gms.add_student(student_id, student_name, student_grade)
        message = response.get("message", str(response)) if isinstance(response, dict) else str(response)
        self.text_display.insert(ctk.END, "✅ " + message + "\n")
        self.show_info_modal("Success", message)

        self.entry_id.delete(0, ctk.END)
        self.entry_name.delete(0, ctk.END)
        self.entry_grade.delete(0, ctk.END)
        self.text_display.configure(state="disabled")

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

    # ---------------- Validation & Modals ----------------
    def is_valid_grade(self, grade):
        valid_grades = ['A', 'B', 'C', 'D', 'F']
        if grade.upper() in valid_grades:
            return True
        try:
            score = int(grade)
            return 0 <= score <= 100
        except ValueError:
            return False

    def show_error_modal(self, message):
        self.show_modal("Error", message, fg_color="#b30000")

    def show_info_modal(self, title, message):
        self.show_modal(title, message, fg_color="#007a3d")

    def show_modal(self, title, message, fg_color="#222222"):
        modal = Toplevel(self)
        modal.title(title)
        modal.geometry("340x160")
        modal.configure(bg=fg_color)
        modal.resizable(False, False)
        modal.grab_set()

        Label(modal, text=message, fg="white", bg=fg_color, font=("Segoe UI", 13), wraplength=300).pack(pady=25)
        Button(modal, text="OK", command=modal.destroy).pack(pady=10)
