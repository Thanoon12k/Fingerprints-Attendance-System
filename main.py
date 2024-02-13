from gzip import FNAME
import tkinter as tk
from PIL import ImageTk, Image
import random
import connection as finger_scan


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Fingerprint Scanner")

        # Set window size and initial image
        self.master.geometry("500x300")
        self.fingerprint_image = Image.new('RGB', (300, 300)) 
        self.tk_image = ImageTk.PhotoImage(self.fingerprint_image)

        # Create a styled frame to hold the image and button
        self.container = tk.Frame(self.master, bg="#f0f0f0", relief="sunken", bd=5)
        self.container.pack(fill="both", expand=True)

        # Create a label for the fingerprint image
        self.label = tk.Label(self.container, image=self.tk_image, bg="#f0f0f0")
        self.label.pack(padx=20, pady=20)

        # Create a styled recapture button
        self.recapture_button = tk.Button(
            self.container, text="Recapture Fingerprint", command=self.recapture_fingerprint, font=("Arial", 12, "bold"), bg="#337ab7", fg="#fff"
        )
        self.recapture_button.pack(pady=10)

    def recapture_fingerprint(self):
        userid =random.randint(1,1000)
        filename = f"fingers/finger_{userid}.bmp"  # Updated the filename format
        finger_scan.SCAN(userid)
        img = Image.open(filename)
        self.tk_image = ImageTk.PhotoImage(img)
        
        # Update the displayed image and reference
        self.label.configure(image=self.tk_image)
        self.fingerprint_image = img

root = tk.Tk()
root.configure(bg="#f0f0f0")
app = MainWindow(root)
root.mainloop()
