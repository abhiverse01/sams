import customtkinter as ctk

class HomeFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#2b2b44")  # Match main container bg
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Header with gradient-like dark blue background
        self.header_frame = ctk.CTkFrame(self, height=70, fg_color="#001f4d", corner_radius=10)
        self.header_frame.pack(fill="x", padx=20, pady=(20,10))

        self.header = ctk.CTkLabel(
            self.header_frame,
            text="Welcome to SAMS",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color="white"
        )
        self.header.place(relx=0.5, rely=0.5, anchor="center")

        # Card Frame with shadow effect and rounded corners
        self.card_frame = ctk.CTkFrame(
            self,
            width=340,
            height=220,
            corner_radius=20,
            fg_color="#394171",
            border_width=2,
            border_color="#545d9a"
        )
        self.card_frame.pack(pady=40, padx=20)
        self.card_frame.pack_propagate(False)

        # Card Title
        self.card_label = ctk.CTkLabel(
            self.card_frame,
            text="SAMS",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#e1e4ff"
        )
        self.card_label.pack(pady=(30,15))

        # Navigation Button with hover effect
        self.card_button = ctk.CTkButton(
            self.card_frame,
            text="Go to SAMS",
            command=lambda: self.controller.show_frame("SAMSFrame"),
            width=140,
            height=45,
            corner_radius=25,
            fg_color="#003366",
            hover_color="#0059b3",
            text_color="white",
            font=ctk.CTkFont(size=16, weight="bold"),
        )
        self.card_button.pack(pady=10)

        # Footer Frame
        self.footer_frame = ctk.CTkFrame(self, height=35, fg_color="#001f4d", corner_radius=10)
        self.footer_frame.pack(side="bottom", fill="x", padx=20, pady=20)

        self.footer = ctk.CTkLabel(
            self.footer_frame,
            text="Abhishek Shah | 2024",
            font=ctk.CTkFont(size=14),
            text_color="#cbd2f7"
        )
        self.footer.place(relx=0.5, rely=0.5, anchor="center")
