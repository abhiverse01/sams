# sams/main_gui.py
import customtkinter as ctk
from gui import SAMSApp

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Student Account Management System")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        # Header
        self.header = ctk.CTkLabel(self, text="Welcome to SAMS", font=("Arial", 24))
        self.header.pack(pady=20)

        # Card
        self.card_frame = ctk.CTkFrame(self, width=200, height=150)
        self.card_frame.pack(pady=50)
        
        self.card_label = ctk.CTkLabel(self.card_frame, text="SAMS", font=("Arial", 18))
        self.card_label.pack(pady=20)
        
        self.card_button = ctk.CTkButton(self.card_frame, text="Go to SAMS", command=self.open_sams)
        self.card_button.pack(pady=10)

        # Footer
        self.footer = ctk.CTkLabel(self, text="Abhishek Shah | 2024", font=("Arial", 12))
        self.footer.pack(side="bottom", pady=10)

    def open_sams(self):
        self.withdraw()
        self.sams_app = SAMSApp(self)
        self.sams_app.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
