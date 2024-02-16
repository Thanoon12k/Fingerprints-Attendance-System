import customtkinter as ctk

def setup_application(w=900,h=600,theme="Dark"):
    ctk.set_appearance_mode(theme)
    root = ctk.CTk()
    root.geometry(f"{w}x{h}")
    root.title("Add Employee")
    return root
    