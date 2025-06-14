import customtkinter as ctk
from tkinter import Toplevel, Label, Button


class RemoveFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#2b2b44")  # dark bg consistent with main app
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Header
        self.header_frame = ctk.CTkFrame(self, height=65, fg_color="#001f4d", corner_radius=12)
        self.header_frame.pack(fill="x", padx=20, pady=(20, 10))

        self.header = ctk.CTkLabel(
            self.header_frame,
            text="Remove Student",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="white"
        )
        self.header.place(relx=0.5, rely=0.5, anchor="center")

        # Student ID Label and Entry
        self.label_id = ctk.CTkLabel(
            self,
            text="Student ID to Remove:",
            font=ctk.CTkFont(size=16),
            text_color="#cbd2f7"
        )
        self.label_id.pack(padx=20, pady=(20, 5), anchor="w")

        self.entry_id = ctk.CTkEntry(
            self,
            font=ctk.CTkFont(size=16),
            width=320,
            corner_radius=10,
            fg_color="#394171",
            text_color="white",
            placeholder_text="Enter Student ID"
        )
        self.entry_id.pack(padx=20, pady=5)

        # Remove Button
        self.button_remove = ctk.CTkButton(
            self,
            text="Remove Student",
            font=ctk.CTkFont(size=16, weight="bold"),
            width=180,
            height=45,
            corner_radius=20,
            fg_color="#a02c2c",
            hover_color="#d13f3f",
            command=self.remove_student
        )
        self.button_remove.pack(pady=(15, 5))

        # Back Button
        self.button_back = ctk.CTkButton(
            self,
            text="Back to SAMS",
            font=ctk.CTkFont(size=14, weight="bold"),
            width=140,
            height=40,
            corner_radius=20,
            fg_color="#003366",
            hover_color="#0059b3",
            command=lambda: self.controller.show_frame("SAMSFrame")
        )
        self.button_back.pack(pady=5)

        # Text Display for messages with scrollbar
        self.text_display = ctk.CTkTextbox(
            self,
            width=720,
            height=160,
            font=ctk.CTkFont(size=13),
            corner_radius=10,
            fg_color="#394171",
            text_color="#e1e4ff"
        )
        self.text_display.pack(padx=20, pady=20)
        self.text_display.configure(state="disabled")  # read-only by default

    def remove_student(self):
        self.text_display.delete("1.0", ctk.END)

        student_id = self.entry_id.get().strip()

        if not student_id:
            self.show_error_modal("Student ID is required to remove a student.")
            self.highlight_error(self.text_display, "Please enter a valid Student ID.\n")
            return

        if not self.controller.gms.student_exists(student_id):
            self.show_error_modal("Student ID does not exist.")
            self.highlight_error(self.text_display, "No student found with this ID.\n")
            return

        # Confirm removal
        self.show_confirm_modal(student_id)

    def do_removal(self, student_id):
        result = self.controller.gms.remove_student(student_id)
        self.show_info_modal("Remove Result", result)
        self.text_display.insert(ctk.END, result + "\n")
        self.entry_id.delete(0, ctk.END)

    def show_confirm_modal(self, student_id):
        modal = Toplevel(self)
        modal.title("Confirm Removal")
        modal.geometry("350x150")
        modal.resizable(False, False)
        modal.grab_set()

        label = Label(modal, text=f"Are you sure you want to remove student ID '{student_id}'?", font=("Arial", 12), wraplength=320)
        label.pack(pady=20)

        btn_frame = ctk.CTkFrame(modal)
        btn_frame.pack(pady=10)

        def confirm():
            self.do_removal(student_id)
            modal.destroy()

        def cancel():
            modal.destroy()

        confirm_btn = Button(btn_frame, text="Yes", command=confirm, width=10)
        confirm_btn.pack(side="left", padx=10)

        cancel_btn = Button(btn_frame, text="No", command=cancel, width=10)
        cancel_btn.pack(side="right", padx=10)

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