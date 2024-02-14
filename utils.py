
from PIL import ImageTk, Image,ImageOps


    
def getImage(width=200, height=250, path="fingers/finger_943.bmp", border_thickness=2):
    pil_image = Image.open(path)
    pil_image = pil_image.resize((width, height), Image.ADAPTIVE)
    border_color = 'black'  # Black color for the border
    pil_image = ImageOps.expand(pil_image, border=border_thickness, fill=border_color)
    image = ImageTk.PhotoImage(pil_image)
    return image