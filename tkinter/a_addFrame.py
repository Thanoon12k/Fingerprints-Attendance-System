import random
from customtkinter import filedialog
from a_tools import *

def create_AddEmployeeFrame(root,fingerprintpath):
    frm_employee = ctk.CTkFrame(root)
    frm_employee.grid()  # Use grid layout

    # Create labels and entries
    lbl_name = create_label(frm_employee, "الاسم")
    lbl_birthdate = create_label(frm_employee, "سنة الميلاد")
    lbl_path = create_label(frm_employee, "",12)
    
    entry_name = create_entry(frm_employee, "text", "",  22)
    entry_birthdate = create_entry(frm_employee, "text", "",  22)
    btn_get_image = createButton(frm_employee, "اختر  صورة", None)
    
    # Replace the entry for image location with a button to select an image
    
    # Function to handle button press and store data in a dictionary
    def on_add_button_click():
        if entry_name.get()=="" or entry_birthdate.get()=="":
            return
        employee_data = {
            "id": random.randint(0, 9999),
            "name": entry_name.get(),
            "birthdate": entry_birthdate.get(),
            "face_image_path": image_path,
            "fingerprint_image_path": fingerprintpath
        }
        saveToDataset(employee_data) 
        print('saved : ', employee_data)  # Or do something else with the data
        root.destroy()
        return True
    # Function to open file dialog and update the button text with the selected file path
    def on_image_button_click():
        global image_path
        if entry_name=="" or entry_birthdate=="":
            return
        
          # Declare image_path as a global variable

        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.gif")])
        if file_path:
            lbl_path.configure(text=file_path)
            image_path = file_path
    btn_add = createButton(frm_employee, "حفظ", on_add_button_click)

    # Grid the labels and entries
    lbl_name.grid(row=0, column=1, sticky='nw', padx=32, pady=5)
    entry_name.grid(row=0, column=0, sticky='e', ipadx=12, padx=32, pady=5)
    lbl_birthdate.grid(row=1, column=1, sticky='nw', padx=32, pady=5)
    entry_birthdate.grid(row=1, column=0, sticky='e', ipadx=12, padx=32, pady=5)
    btn_get_image.grid(row=2, column=1, sticky='e', padx=32, pady=5)
    lbl_path.grid(row=3, column=0, columnspan=3, padx=2, pady=2)  # Span three columns
    
    # Create the add button and bind the click event to the on_add_button_click function
    btn_add.grid(row=4, column=0, columnspan=2, pady=32)

    # Bind the click event of the image button to the on_image_button_click function
    btn_get_image.configure(command=on_image_button_click)

    return frm_employee
