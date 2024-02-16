from tkinter import ANCHOR
from PIL import ImageTk, Image, ImageDraw
import customtkinter as ctk
import pandas as pd


def create_label(parent, text, font_size=26):
    return ctk.CTkLabel(parent, text=text, font=("Arial", font_size, "bold"))


def create_entry(parent, text, holder, font_size=26):
    return ctk.CTkEntry(
        parent, placeholder_text=holder, font=("Arial", font_size, "bold")
    )


def createButton(root, text, command, font_size=22):
    btn = ctk.CTkButton(
        root,
        text=text,
        command=command,
        corner_radius=8,
        font=("Arial", font_size, "bold"),
        border_spacing=8,
    )
    return btn


def createLableImage(root, path, w, h):
    img = Image.open(path)
    UserImage = ctk.CTkImage(light_image=img, size=(w, h))
    lbl_image = ctk.CTkLabel(root, text="", image=UserImage)

    return lbl_image


import pandas as pd
import os

def saveToDataset(data):
    # Pass an index when creating the DataFrame
    df = pd.DataFrame(data, index=[0])
    csv_filename = "dataset/employees.csv"
    header = not os.path.exists(csv_filename)
    df.to_csv(csv_filename, mode='a', index=False, header=header)
