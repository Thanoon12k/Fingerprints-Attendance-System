from tkinter import ANCHOR
from PIL import ImageTk, Image,ImageDraw
import customtkinter as ctk
def create_label(parent, text,font_size=26):
    return ctk.CTkLabel(parent, text=text, font=("Arial",   font_size, "bold"))



def create_ScanFrame(root, emp_data,finger_path="assets/finger_logo.PNG"):
    frm_employee = ctk.CTkFrame(root) 
    img_box=createLableImage(frm_employee,finger_path,350,400)
    lbl_image = create_label(frm_employee, f"  ضع اصبع الابهام على جهاز البصمة",14)
    img_box.pack(pady=6)
    lbl_image.pack(pady=4)
   

   
    
    return frm_employee
def create_EmployeeNotFoundFrame(root):
    frm_employee = ctk.CTkFrame(root)
    lbl_image = create_label(frm_employee, f" !! لا توجد بصمة مطابقة",42)
    btn_add = createButton(frm_employee,"اضافة موظف جديد",None)
    lbl_image.pack(pady=42)
    btn_add.pack(pady=32)
    return frm_employee

def create_WelcomeFrame(root):
    frm_employee = ctk.CTkFrame(root)
    lbl_image = create_label(frm_employee, f"يرجى مسح البصمة لتسجيل الحضور ")
    lbl_image.pack(pady=42,padx=24,fill="both",anchor="center")
    return frm_employee

    
    
def create_EmployeeFrame(root, emp_data):
    frm_employee = ctk.CTkFrame(root)
    img_box=createLableImage(frm_employee,"assets/ali.png",200,200)
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

def createLableImage(root,path,w,h):
    img = Image.open(path)
    UserImage = ctk.CTkImage(light_image=img, size=(w, h))
    print("path===",path)
    lbl_image = ctk.CTkLabel(root, text="", image=UserImage)

    return lbl_image
