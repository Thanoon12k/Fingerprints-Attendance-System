import random
from customtkinter import filedialog
from a_tools import *

def create_AddEmployeeFrame(root,fingerprintpath):
    frm_employee = ctk.CTkFrame(root)
    frm_employee.grid()  # Use grid layout

    # Create labels and entries
    lbl_name = create_label(frm_employee, "الاسم")
    entry_name = create_entry(frm_employee, "text", "",  22)
    lbl_birthdate = create_label(frm_employee, "سنة الميلاد")
    entry_birthdate = create_entry(frm_employee, "text", "",  22)

    # Replace the entry for image location with a button to select an image
    lbl_image_location = create_label(frm_employee, "مكان الصورة")
    btn_image_location = createButton(frm_employee, "اختر  صورة", None)
    btn_image_location.grid(row=2, column=1, sticky='e', padx=32, pady=5)

    # Function to handle button press and store data in a dictionary
    def on_add_button_click():

        employee_data = {
            "id": random.randint(0, 9999),
            "name": entry_name.get(),
            "birthdate": entry_birthdate.get(),
            "face_image_path": image_path,
            "fingerprint_image_path": fingerprintpath
        }
        saveToDataset(employee_data) 
        print('saved : ', employee_data)  # Or do something else with the data
        return True
    # Function to open file dialog and update the button text with the selected file path
    def on_image_button_click():
        global image_path  # Declare image_path as a global variable

        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.gif")])
        if file_path:
            btn_image_location.configure(text=file_path)
            image_path = file_path
    # Grid the labels and entries
    lbl_name.grid(row=0, column=1, sticky='nw', padx=32, pady=5)
    entry_name.grid(row=0, column=0, sticky='e', ipadx=12, padx=32, pady=5)
    lbl_birthdate.grid(row=1, column=1, sticky='nw', padx=32, pady=5)
    entry_birthdate.grid(row=1, column=0, sticky='e', ipadx=12, padx=32, pady=5)
    lbl_image_location.grid(row=2, column=1, sticky='nw', padx=32, pady=5)

    # Create the add button and bind the click event to the on_add_button_click function
    btn_add = createButton(frm_employee, "حفظ", on_add_button_click)
    btn_add.grid(row=3, column=0, columnspan=2, pady=32)

    # Bind the click event of the image button to the on_image_button_click function
    btn_image_location.configure(command=on_image_button_click)

    return frm_employee
