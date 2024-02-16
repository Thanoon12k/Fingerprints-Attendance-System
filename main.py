import datetime
import random
from tkinter import LabelFrame, Canvas, Label, Tk,Frame
from PIL import ImageTk, Image,ImageOps

import customtkinter as ctk
from sympy import false
from comparing import FindEmployeeData, createDataSet
from connection import capture_fingerprint_image
from utils import getImage
from PIL import Image
class EmployeeInfoFrame(LabelFrame):
    def __init__(self, master, employee_data):
        super().__init__(master, text="Employee Information", font=ctk.CTkFont(size=22, weight="bold"))
        self.employee_data = employee_data
        
        self.create_labels()

    def create_labels(self):
        # Define a CTkFont with the desired color
        self.empty_label = ctk.CTkLabel(self, text     ="")
        self.emp_id_label = ctk.CTkLabel(self, text     ="  ID         :  "+str(self.employee_data['id']),text_color="black" ,font=("Arial", 12, "bold"))
        self.emp_name_label = ctk.CTkLabel(self, text   ="  Name       :  "+str(self.employee_data['name']),text_color="black" ,font=("Arial", 12, "bold")) 
        self.attendance_state = ctk.CTkLabel(self, text="  Attendance Status :  "+str(self.employee_data['state']),text_color="black" ,font=("Arial", 12, "bold"))
        self.attendance_date = ctk.CTkLabel(self, text="  Attendance Date :  "+str(self.employee_data['Attendance Date']),text_color="black" ,font=("Arial", 12, "bold"))
        self.emp_birthdate_label =ctk.CTkLabel(self,text="  BirthDate  :  "+str(self.employee_data['birthdate']),text_color="black" ,font=("Arial", 12, "bold"))
        self.finger_score =ctk.CTkLabel(self,text="  Score    :  #############  "+str(self.employee_data['score'])+" %  #############  ",text_color="black" ,font=("Arial", 12, "bold"))
        img=Image.open(self.employee_data['face_image_path'])
        self.UserImage=ctk.CTkImage(light_image=img,size=(150,150))
        self.image_label = ctk.CTkLabel(self,text="", image=self.UserImage)

        self.image_label.grid(row=0, column=0, sticky="w",pady=12)
        self.emp_id_label.grid(row=1, column=0, sticky="w",pady=2)
        self.emp_name_label.grid(row=2, column=0, sticky="w",pady=2)
        self.attendance_state.grid(row=3, column=0, sticky="w",pady=2)
        self.attendance_date.grid(row=4, column=0, sticky="w",pady=2)
        self.emp_birthdate_label.grid(row=5, column=0, sticky="w",pady=2)
        self.finger_score.grid(row=6, column=0, sticky="w",pady=2)
    
        
class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.employee_data = None

        self.geometry("750x450")
        self.title("Employee Information App")
        img=Image.open("assets/finger_logo.PNG")
        img = ImageOps.expand(img, border=2)
        self.fingerPrintImage=ctk.CTkImage(light_image=img,size=(220,360))
        self.image_label = ctk.CTkLabel(self,text="", image=self.fingerPrintImage,width=240,height=360)
        
        self.content_frame = Frame(self)
        
        self.content_frame.grid(row=0, column=0, padx=10, pady=(40,  20), sticky='ew')
        self.employee_info_frame = None
        self.ScanButton = ctk.CTkButton(self, text="SCAN FINGERPRINT", command=self.ScanFinger, width=100, height=50, corner_radius=8)
        self.AddButton = ctk.CTkButton(self, text="ADD NEW", command=self.AddEmployee, width=100, height=50, corner_radius=8)
        
        self.image_label.grid(row=0, column=0, padx=10, pady=(10,  10), sticky='ns')        
        self.ScanButton.grid(row=1, column=0, pady=5)
        self.AddButton.grid(row=2, column=0, pady=5)
        
    def AddEmployee(self):
        createDataSet()
    def ScanFinger(self):
        fingerprint_image_path=capture_fingerprint_image()
        self.updateImage(path=fingerprint_image_path)        
        employee_data=FindEmployeeData(fingerprint_image_path)
        print(f"returned employee: {employee_data}")
        self.employee_data=employee_data
        self.employee_data['score']= employee_data['score']
        
        if self.employee_info_frame is None:
            self.display_employee_info()
        elif self.employee_info_frame is not None :
            self.employee_info_frame.destroy()
            self.employee_info_frame = None
        
        
    def updateImage(self,path):
        pil_image = Image.open(path)
        pil_image = ImageOps.expand(pil_image, border=2)
        self.UserImage=ctk.CTkImage(light_image=pil_image,size=(200,225))
        self.image_label = ctk.CTkLabel(self,text="", image=self.UserImage)
        self.image_label.grid(row=0, column=0, padx=10, pady=(10,  10), sticky='ns')
    
    def display_employee_info(self):
            self.employee_data[ 'state']= 'Registered Successfully'
            self.employee_data['Attendance Date']= datetime.datetime.now()
            
            
            self.employee_info_frame = EmployeeInfoFrame(self, self.employee_data)
            self.employee_info_frame.grid(row=0, column=1, padx=10, pady=10, sticky='ns')

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
