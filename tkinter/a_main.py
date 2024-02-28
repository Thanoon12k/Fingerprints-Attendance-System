import customtkinter as ctk
from a_comparing import FindEmployeeData
from a_employees_table import create_EmployeeTableFrame
from a_frames import  create_EmployeeNotFoundFrame, create_WelcomeFrame, create_EmployeeFrame, create_ScanFrame
from a_setup_app import setup_application
from a_addFrame import create_AddEmployeeFrame
from a_tools import saveToDataset
from device import capture_fingerprint_image
class Application:
    def __init__(self, theme="Dark"):
        self.emp_data = {
        "image": "example_image.jpg",
        "id": "234",
        "name": "ذنون يونس محمد",
        "state": "تم تسجيل الحضور بنجاح",
        "birthdate": "01/01/1996",
        "attendance_date": "02/15/2024 08:15 م",
        "score": "95", }    
        self.root = setup_application(theme=theme)
        self.fingerprint_path="assets/ali.png"
        self.scan_frame = create_ScanFrame(self.root, self.emp_data)
        self.employee_data_frame = create_WelcomeFrame(self.root)
        self.add_employee_frame=None
        self.employees_table_frame = None
        self.btn_scan = self.createButton("قراءة البصمة", self.scanFinger)
        self.btn_employees_table = self.createButton("عرض سجل الموظفين ", self.show_employeesTable)
                
        self.scan_frame.grid(row=0, column=0, sticky='nw')
        self.employee_data_frame.grid(row=0, column=1, sticky='nw',padx=40,pady=70)
        self.btn_scan.grid(row=1, column=0, sticky='n')
        self.btn_employees_table.grid(row=2,column=0,pady=20)
    def createButton(self, text, command,font_size=22):
        btn=ctk.CTkButton(
            self.root,
            text=text,
            command=command,
            corner_radius=8,
            font=("Arial",   font_size, "bold"),border_spacing=8)
        return btn

    def run(self):
        self.root.mainloop()
    def show_EmployeeInfoFrame(self):
        if self.employee_data_frame is not None:
            self.employee_data_frame.destroy()
        if self.emp_data is None:
            self.employee_data_frame = create_EmployeeNotFoundFrame(self.root,self.show_addEmployeeFrame)
        else:
            self.employee_data_frame = create_EmployeeFrame(self.root, self.emp_data)
        self.employee_data_frame.grid(row=0, column=1, sticky='nw',padx=70)

            
    def show_addEmployeeFrame(self):
        if self.add_employee_frame is not None:
            self.add_employee_frame.destroy()
            
        self.add_employee_frame=create_AddEmployeeFrame(self.root,self.fingerprint_path)
        self.employee_data_frame.destroy()
        self.add_employee_frame.grid(row=0, column=1, sticky='nw',padx=70)

    def show_employeesTable(self):
        if self.add_employee_frame is not None:
            self.add_employee_frame.destroy()
           
        self.employee_data_frame.destroy()
        self.scan_frame.destroy()
        self.btn_scan.destroy()
        self.btn_employees_table.destroy()
        self.employees_table_frame=create_EmployeeTableFrame(self.root)
        self.employees_table_frame.grid()

            
            
            

    def scanFinger(self):   
        self.fingerprint_path="fingers/qussay_.bmp"
        if self.scan_frame is not None:
            self.scan_frame.destroy()

            self.scan_frame=create_ScanFrame(self.root, self.emp_data,self.fingerprint_path)
            self.scan_frame.grid(row=0, column=0, sticky='nw')

        self.emp_data=FindEmployeeData(self.fingerprint_path)
        self.show_EmployeeInfoFrame()
        return 0
app = Application(theme="Dark")
# Run the application
app.run()
