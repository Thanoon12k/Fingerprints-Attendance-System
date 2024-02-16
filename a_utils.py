
from comparing2 import FindEmployeeData
from connection import capture_fingerprint_image
import customtkinter as ctk

def createButton(root,text,command,font_size=22):
    btn=ctk.CTkButton(
            root,
            text=text,
            command=scanFinger,
            corner_radius=8,
            font=("Arial",   font_size, "bold"),border_spacing=8)
    return btn
def scanFinger():
    from a_main import get_Root
    from a_frames import create_EmployeeNotFoundFrame, create_employee_form
    root=get_Root()
    fingerprint_path="fingers/thanoon_.bmp"
    # fingerprint_path=capture_fingerprint_image()
    employee_data=FindEmployeeData(fingerprint_path)
    print(f"employee data : {employee_data}")
    employee_form=None
    if employee_data is None:
        employee_form = create_EmployeeNotFoundFrame(root)
    else:
        employee_form = create_employee_form(root, employee_data)   
    return employee_form