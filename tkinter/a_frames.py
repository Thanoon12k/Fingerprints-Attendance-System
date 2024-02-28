from tkinter import ANCHOR
from PIL import ImageTk, Image,ImageDraw
import customtkinter as ctk
from a_tools import create_entry, create_label,createButton,createLableImage

def create_ScanFrame(root, emp_data,finger_path="assets/finger_logo.PNG"):
    frm_employee = ctk.CTkFrame(root) 
    img_box=createLableImage(frm_employee,finger_path,350,400)
    lbl_image = create_label(frm_employee, f"  ضع اصبع الابهام على جهاز البصمة",14)
    img_box.pack(pady=6)
    lbl_image.pack(pady=4) 
    return frm_employee
def create_EmployeeNotFoundFrame(root,cmd):
    frm_employee = ctk.CTkFrame(root)
    lbl_image = create_label(frm_employee, f" !! لا توجد بصمة مطابقة",42)
    btn_add = createButton(frm_employee,"اضافة موظف جديد",command=cmd)
    lbl_image.pack(pady=42)
    btn_add.pack(pady=32)
    return frm_employee

def create_AddEmployeeFrame(root):
    frm_employee = ctk.CTkFrame(root)
    frm_employee.grid()  # Use grid layout
    lbl_name = create_label(frm_employee, "الاسم")
    entry_name = create_entry(frm_employee, "text", "",  22)
    lbl_birthdate = create_label(frm_employee, "سنة الميلاد")
    entry_birthdate = create_entry(frm_employee, "text", "",  22)
    lbl_image_location = create_label(frm_employee, "مكان الصورة")
    entry_image_location = create_entry(frm_employee, "text", "",  22)
    lbl_name.grid(row=0, column=1, sticky='nw', padx=32, pady=5)
    entry_name.grid(row=0, column=0, sticky='e', ipadx=12, padx=32, pady=5)
    lbl_birthdate.grid(row=1, column=1, sticky='nw', padx=32, pady=5)
    entry_birthdate.grid(row=1, column=0, sticky='e', ipadx=12, padx=32, pady=5)
    lbl_image_location.grid(row=2, column=1, sticky='nw', padx=32, pady=5)
    entry_image_location.grid(row=2, column=0, sticky='e', ipadx=12, padx=32, pady=5)
    btn_add = createButton(frm_employee, "حفظ", None)
    btn_add.grid(row=3, column=0, columnspan=2, pady=32)  # Adjust row number as needed
    return frm_employee



def create_WelcomeFrame(root):
    frm_employee = ctk.CTkFrame(root)
    lbl_image = create_label(frm_employee, f"يرجى مسح البصمة لتسجيل الحضور ")
    lbl_image.pack(pady=42,padx=24,fill="both",anchor="center")
    return frm_employee

    
    
def create_EmployeeFrame(root, emp_data):
    frm_employee = ctk.CTkFrame(root)
    img_box=createLableImage(frm_employee,emp_data['face-image'],200,200)
    lbl_image = create_label(frm_employee, f"الصورة الشخصية")
    lbl_id = create_label(frm_employee,             f"الرقم الوظيفي  :  {emp_data['id']}")
    lbl_name = create_label(frm_employee,           f"        الاسم            :  {emp_data['name']}")
    lbl_state = create_label(frm_employee,          f" حالة التسجيل   : {emp_data['state']}")
    lbl_birthdate = create_label(frm_employee,      f" تاريخ الميلاد   : {emp_data['birthdate']}")
    lbl_attendance_date = create_label(frm_employee,f" تاريخ الحضور : {emp_data['attendance_date']}")
    lbl_score = create_label(frm_employee,          f" نسبة التطابق  :  {emp_data['score']}")
    
    
    img_box.pack(anchor='n', padx=10, pady=6, side='top')
    lbl_image.pack(anchor='n', padx=10, pady=6, side='top')
    lbl_id.pack(anchor='ne', padx=10, pady=2, side='top')
    lbl_name.pack(anchor='ne', padx=10, pady=2, side='top')
    lbl_state.pack(anchor='ne', padx=10, pady=2, side='top')
    lbl_birthdate.pack(anchor='ne', padx=10, pady=2, side='top')
    lbl_attendance_date.pack(anchor='ne', padx=10, pady=2, side='top')
    lbl_score.pack(anchor='ne', padx=10, pady=2, side='top')

    
    return frm_employee

