from tkinter import LabelFrame, Canvas, Label, Tk,Frame
from PIL import ImageTk, Image,ImageOps

import customtkinter as ctk
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
        self.emp_id_label = ctk.CTkLabel(self, text     ="  ID         :  "+str(self.employee_data['id']),text_color="black" ,font=("Arial",  24))
        self.emp_name_label = ctk.CTkLabel(self, text   ="  Name       :  "+str(self.employee_data['name']),text_color="black" ,font=("Arial",  26)) 
        self.attendance_state = ctk.CTkLabel(self, text="  Attendance Status :  "+str(self.employee_data['state']),text_color="black" ,font=("Arial",  22))
        self.attendance_date = ctk.CTkLabel(self, text="  Attendance Date :  "+str(self.employee_data['Attendance Date']),text_color="black" ,font=("Arial",  20))
        self.emp_birthdate_label =ctk.CTkLabel(self,text="  BirthDate  :  "+str(self.employee_data['birthdate']),text_color="black" ,font=("Arial",  18))
        img=Image.open("fingers/avatar.jpeg")
        self.UserImage=ctk.CTkImage(light_image=img,size=(150,150))
        self.image_label = ctk.CTkLabel(self,text="", image=self.UserImage)

        self.image_label.grid(row=0, column=0, sticky="w",pady=12)
        self.emp_id_label.grid(row=1, column=0, sticky="w",pady=2)
        self.emp_name_label.grid(row=2, column=0, sticky="w",pady=2)
        self.attendance_state.grid(row=3, column=0, sticky="w",pady=2)
        self.attendance_date.grid(row=4, column=0, sticky="w",pady=2)
        self.emp_birthdate_label.grid(row=5, column=0, sticky="w",pady=2)
    
        
class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("750x450")
        self.title("Employee Information App")
        img=Image.open("fingers/finger_78.bmp")
        img = ImageOps.expand(img, border=2)
        self.fingerPrintImage=ctk.CTkImage(light_image=img,size=(200,250))
        self.image_label = ctk.CTkLabel(self,text="", image=self.fingerPrintImage)
        
        self.content_frame = Frame(self)
        
        self.content_frame.grid(row=0, column=0, padx=10, pady=(40,  20), sticky='ew')
        self.employee_info_frame = None
        self.ScanButton = ctk.CTkButton(self, text="SCAN FINGERPRINT", command=self.ScanFinger, width=100, height=50, corner_radius=8)
        
        self.ScanButton.grid(row=2, column=0, pady=5)
        self.image_label.grid(row=0, column=0, padx=10, pady=(10,  10), sticky='ns')        
  
        
    def ScanFinger(self):
        self.updateImage(path="fingers/finger_915.bmp")        
  
        if self.employee_info_frame is not None:
            self.employee_info_frame.destroy()
            self.employee_info_frame = None
        else:
            self.display_employee_info()

    def updateImage(self,path):
        img=Image.open(path)
        img = ImageOps.expand(img, border=2)
        self.UserImage=ctk.CTkImage(light_image=img,size=(200,250))
        self.image_label = ctk.CTkLabel(self,text="", image=self.UserImage)
        self.image_label.grid(row=0, column=0, padx=10, pady=(10,  10), sticky='ns')
    
    def display_employee_info(self):
            employee_data = {
                'state': 'Registered Successfully',
                'id':  5,
                'name': 'ali hameed younois',
                'birthdate': '25/8/2000',
                'Attendance Date': '25/8/2025-08:15 PM',
                'face_image': 'aa',
                'fingerprint_image': 'aaa'
            }
            self.employee_info_frame = EmployeeInfoFrame(self, employee_data)
            self.employee_info_frame.grid(row=0, column=1, padx=10, pady=10, sticky='ns')

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
