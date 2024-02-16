import customtkinter as ctk
from a_comparing import FindEmployeeData
from a_frames import create_EmployeeNotFoundFrame, create_WelcomeFrame, create_EmployeeFrame, create_ScanFrame
from a_setup_app import setup_application

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
        self.scan_frame = create_ScanFrame(self.root, self.emp_data)
        self.employee_data_frame = create_WelcomeFrame(self.root)
        self.btn_scan = self.createButton("قراءة البصمة", self.scanFinger)
                
        self.scan_frame.grid(row=0, column=0, sticky='nw')
        self.employee_data_frame.grid(row=0, column=1, sticky='nw',padx=40,pady=70)
        self.btn_scan.grid(row=1, column=0, sticky='n')

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
    def show_emp_data(self):
    # Destroy the old employee_data_frame if it exists
        if self.employee_data_frame is not None:
            self.employee_data_frame.destroy()

        # Create a new employee_data_frame based on the emp_data
        if self.emp_data is None:
            self.employee_data_frame = create_EmployeeNotFoundFrame(self.root)
        else:
            self.employee_data_frame = create_EmployeeFrame(self.root, self.emp_data)

        # Pack the new employee_data_frame
        self.employee_data_frame.grid(row=0, column=1, sticky='nw',padx=70)

            
            
            

    def scanFinger(self): 
        root= self.root
        fingerprint_path="fingers/qussay_.bmp"
        # fingerprint_path=capture_fingerprint_image()
        self.emp_data=FindEmployeeData(fingerprint_path)
        self.show_emp_data()
        return 0
app = Application(theme="Dark")
# Run the application
app.run()
