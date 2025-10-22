import customtkinter as ctk
from PIL import Image
import os
from services.gms import GradeManagementSystem
from ui.home_frame import HomeFrame
from ui.sams_frame import SAMSFrame
from ui.update_frame import UpdateFrame
from ui.remove_frame import RemoveFrame

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Basic Window Settings
        self.title("SAMS - Student Account Management System")
        self.geometry("900x650")
        self.minsize(800, 600)
        self.configure(fg_color="#1e1e2f")  # Dark background for modern look

        # Grade Management System instance
        self.gms = GradeManagementSystem()

        # Initialize background variables
        self.bg_image_path = "assets/SAMSbg.png"
        self.bg_image = None
        self.bg_label = None
        self.overlay = None

        # Setup UI components
        self.create_widgets()

        # Bind window resize to update background image
        self.bind("<Configure>", self.on_resize)

        # Bind keyboard shortcuts for frame navigation
        self.bind_all("<Control-h>", lambda e: self.switch_frame_with_animation("HomeFrame"))
        self.bind_all("<Control-a>", lambda e: self.switch_frame_with_animation("SAMSFrame"))
        self.bind_all("<Control-u>", lambda e: self.switch_frame_with_animation("UpdateFrame"))
        self.bind_all("<Control-r>", lambda e: self.switch_frame_with_animation("RemoveFrame"))

    def switch_frame_with_animation(self, frame_name):
        current_frame = None
        for f in self.frames.values():
            if f.winfo_ismapped():
                current_frame = f
                break

        target_frame = self.frames.get(frame_name)
        if target_frame and current_frame != target_frame:
            # Hide current frame
            if current_frame:
                current_frame.grid_remove()
            # Show target frame
            target_frame.grid()
            self.highlight_nav_button(frame_name)

            
    def fade_out_in(self, current_frame, target_frame, step=0):
        # A simple fade-out and fade-in simulation by quickly hiding and showing frames
        if step == 0:
            # Hide current frame
            if current_frame:
                current_frame.grid_remove()
            # Show target frame
            target_frame.grid()
            self.highlight_nav_button(target_frame.__class__.__name__)
        # No actual fade animation possible with CTk frames, but can extend here for complex effects


        # -------------------- Controller Logic -------------------- #

    def add_student(self, student_id, name, grade):
        """Add a new student to the system."""
        result = self.gms.add_student(student_id, name, grade)
        self.refresh_data_views()
        return result

    def update_student(self, student_id, name=None, grade=None):
        """Update an existing student's information."""
        result = self.gms.update_student(student_id, name, grade)
        self.refresh_data_views()
        return result

    def remove_student(self, student_id):
        """Remove a student by ID."""
        result = self.gms.remove_student(student_id)
        self.refresh_data_views()
        return result

    def get_student(self, student_id):
        """Fetch a student record."""
        return self.gms.get_student(student_id)

    def get_all_students(self):
        """Return all students."""
        return self.gms.get_all_students()

    def refresh_data_views(self):
        """Refresh data views across frames (if they exist)."""
        if hasattr(self.frames.get("HomeFrame"), "refresh_data"):
            self.frames["HomeFrame"].refresh_data()
        if hasattr(self.frames.get("SAMSFrame"), "refresh_data"):
            self.frames["SAMSFrame"].refresh_data()
        if hasattr(self.frames.get("UpdateFrame"), "refresh_data"):
            self.frames["UpdateFrame"].refresh_data()
        if hasattr(self.frames.get("RemoveFrame"), "refresh_data"):
            self.frames["RemoveFrame"].refresh_data()

    
    def create_widgets(self):
        # Load initial background image and overlay
        self.load_background_image()

        # Overlay frame to darken background for readability
        self.overlay = ctk.CTkFrame(self, fg_color="#222222")  # Dark gray overlay (solid)
        self.overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
        if self.bg_label:
            self.overlay.lift(self.bg_label)  # overlay above bg_label

        # Main container frame with some padding and corner radius
        self.container = ctk.CTkFrame(self, fg_color="#2b2b44", corner_radius=20)
        self.container.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

        # Navigation sidebar (left)
        self.nav_frame = ctk.CTkFrame(self.container, width=180, fg_color="#262639", corner_radius=15)
        self.nav_frame.grid(row=0, column=0, sticky="ns", padx=15, pady=15)
        self.nav_frame.grid_propagate(False)

        # Title in nav bar
        title_label = ctk.CTkLabel(
            self.nav_frame,
            text="SAMS Menu",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#a1a1c2"
        )
        title_label.pack(pady=(15, 30))

        # Navigation Buttons
        btn_font = ctk.CTkFont(size=16, weight="bold")
        buttons = [
            ("Home", "HomeFrame"),
            ("Add Student", "SAMSFrame"),
            ("Update Student", "UpdateFrame"),
            ("Remove Student", "RemoveFrame"),
        ]
        self.nav_buttons = {}
        for text, frame_name in buttons:
            btn = ctk.CTkButton(
                self.nav_frame,
                text=text,
                font=btn_font,
                fg_color="#3a3a5c",
                hover_color="#57578e",
                corner_radius=12,
                command=lambda name=frame_name: self.show_frame(name),
                width=160,
                height=40
            )
            btn.pack(pady=8)
            self.nav_buttons[frame_name] = btn

        # Highlight HomeFrame button initially
        self.highlight_nav_button("HomeFrame")

        # Frame container on the right side
        self.frames_container = ctk.CTkFrame(self.container, fg_color="#353560", corner_radius=15)
        self.frames_container.grid(row=0, column=1, sticky="nsew", padx=(10, 15), pady=15)
        self.container.grid_columnconfigure(1, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        # Load all frames once and keep
        self.frames = {}
        for F in (HomeFrame, SAMSFrame, UpdateFrame, RemoveFrame):
            frame = F(parent=self.frames_container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show Home frame initially
        self.show_frame("HomeFrame")

    def load_background_image(self):
        if os.path.exists(self.bg_image_path):
            # Load original image
            original_image = Image.open(self.bg_image_path)
            # Resize to current window size
            width = self.winfo_width() if self.winfo_width() > 1 else 900
            height = self.winfo_height() if self.winfo_height() > 1 else 650
            resized_image = original_image.resize((width, height))
            self.bg_image = ctk.CTkImage(resized_image)
            if self.bg_label is None:
                self.bg_label = ctk.CTkLabel(self, image=self.bg_image)
                self.bg_label.place(relwidth=1, relheight=1)
                self.bg_label.lower()  # Send to back
            else:
                self.bg_label.configure(image=self.bg_image)

    def on_resize(self, event):
        # Only update background if root window resizes (not children)
        if event.widget == self:
            self.load_background_image()

    def show_frame(self, name):
        frame = self.frames.get(name)
        if frame:
            frame.tkraise()
            self.highlight_nav_button(name)

    def highlight_nav_button(self, active_name):
        for name, btn in self.nav_buttons.items():
            if name == active_name:
                btn.configure(fg_color="#6060a0", hover_color="#48488c")
            else:
                btn.configure(fg_color="#3a3a5c", hover_color="#57578e")
