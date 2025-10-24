import customtkinter as ctk

class HomeFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#1b1b2f")  # Deep dark background
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # --- Header Section ---
        self.header_frame = ctk.CTkFrame(
            self,
            height=80,
            fg_color="#162447",
            corner_radius=12
        )
        self.header_frame.pack(fill="x", padx=25, pady=(25, 15))

        self.header = ctk.CTkLabel(
            self.header_frame,
            text="Welcome to SAMS",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#f5f7ff"
        )
        self.header.place(relx=0.5, rely=0.5, anchor="center")

        # --- Tagline ---
        self.subheader = ctk.CTkLabel(
            self,
            text="Student Account Management System",
            font=ctk.CTkFont(size=16, slant="italic"),
            text_color="#a3aed0"
        )
        self.subheader.pack(pady=(0, 20))

        # --- Central Card Section ---
        self.card_frame = ctk.CTkFrame(
            self,
            width=400,
            height=250,
            corner_radius=24,
            fg_color="#1f4068",
            border_width=2,
            border_color="#e43f5a"
        )
        self.card_frame.pack(pady=40, padx=20)
        self.card_frame.pack_propagate(False)

        self.card_title = ctk.CTkLabel(
            self.card_frame,
            text="SAMS Dashboard",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#ffffff"
        )
        self.card_title.pack(pady=(35, 10))

        self.card_subtext = ctk.CTkLabel(
            self.card_frame,
            text="Manage Students • View Reports • Update Records",
            font=ctk.CTkFont(size=14),
            text_color="#cbd2f7"
        )
        self.card_subtext.pack(pady=(0, 25))

        self.card_button = ctk.CTkButton(
            self.card_frame,
            text="Open SAMS",
            command=lambda: self.controller.show_frame("SAMSFrame"),
            width=160,
            height=48,
            corner_radius=25,
            fg_color="#e43f5a",
            hover_color="#ff6b81",
            text_color="white",
            font=ctk.CTkFont(size=16, weight="bold"),
        )
        self.card_button.pack(pady=10)

        # --- Footer Section ---
        self.footer_frame = ctk.CTkFrame(
            self,
            height=40,
            fg_color="#162447",
            corner_radius=12
        )
        self.footer_frame.pack(side="bottom", fill="x", padx=25, pady=25)

        self.footer_label = ctk.CTkLabel(
            self.footer_frame,
            text="© 2025 Abhishek Shah — GreyEngineer Labs",
            font=ctk.CTkFont(size=13),
            text_color="#a3aed0"
        )
        self.footer_label.place(relx=0.5, rely=0.5, anchor="center")
