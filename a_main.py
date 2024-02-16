import customtkinter as ctk

from a_database import emp_data
from a_frames import create_WelcomeScreen, create_fingerprint_frame
from a_setup_app import setup_application
from a_utils import createButton


root=setup_application(theme="Dark")
btn_scan            = createButton(root,"قراءة البصمة",None)
scan_frame   =create_fingerprint_frame(root, emp_data)
employee_data_frame=create_WelcomeScreen(root)

employee_data_frame.pack(anchor='nw', padx=10, pady=10, side='right')
scan_frame.pack(anchor='nw', padx=10, pady=10, side='top')
btn_scan.pack(anchor='n',padx=10, pady=10, side='top')

root.mainloop()

def get_Root():
    return root
    
