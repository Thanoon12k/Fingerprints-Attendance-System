import tkinter as tk
import customtkinter as ctk
import csv

from a_tools import create_label
def create_EmployeeTableFrame(root):
    csv_path = "dataset/employees.csv"
    container = ctk.CTkFrame(root)
    container.grid(sticky='nswe')  # Make the container frame expand to fill the entire window
    canvas = ctk.CTkCanvas(container)
    canvas.grid(row=0, column=0, sticky='nswe')  # Make the canvas expand to fill the container frame
    scrollbar = ctk.CTkScrollbar(root, command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky='nswe')
    canvas.configure(yscrollcommand=scrollbar.set)

    frm_employee = ctk.CTkFrame(root)

    # Read the CSV file
    with open(csv_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader)  # Get the header row
        data = list(csv_reader)  # Get the rest of the data

    for i, heading in enumerate(headers):
        label = create_label(frm_employee, text=heading, font_size=26,text_color="yellow")
        label.grid(row=0, column=i, padx=5, pady=15, sticky='w')
    for i, row in enumerate(data, start=1):
        for j, cell in enumerate(row):
            label = create_label(frm_employee, text=cell, font_size=18)
            label.grid(row=i, column=j, padx=2, pady=2, sticky='n')

    canvas.create_window((0,  0), window=frm_employee, anchor='nw')
    canvas.update_idletasks()  # Refresh the canvas to get the correct bbox
    canvas.configure(scrollregion=canvas.bbox('all'))  # Set the scroll region to the size of the frame
    
    return container
