
import os
from django.conf import settings
from datetime import datetime
from datetime import datetime
from .connections import SCAN_IMAGE
from .comparing import compare_fingerprints
def getArrivalTime():
        now = datetime.now()
        day_of_week = now.strftime("%A")  # Ex: "Tuesday"
        day = now.strftime("%d")  # Ex: "29" (day of the month)
        month = now.strftime("%m")  # Ex: "02" (month as a string)
        year = now.strftime("%Y")  # Ex: "2024"
        hours = now.strftime("%H")  # 24-hour format
        minutes = now.strftime("%M")  # Ex: "05"

        # Convert hours to 12-hour format and add AM/PM
        if int(hours) > 12:
          hours = str(int(hours) - 12)
          period = "PM"
        else:
          period = "AM"

        arrival_time = f"{day_of_week} {day}-{month}-{year} {hours}:{minutes} {period}"
        return arrival_time

def scanFingerprintImage():
    image_name = 'img_001.bmp'
    img_path = settings.MEDIA_ROOT+'/temp/'+image_name
    img_url = settings.MEDIA_URL+ 'temp/'+ image_name
    print(f'returned \nurl: {img_url},\n   path: {img_path}')

    SCAN_IMAGE(img_path)
    
    return img_url, img_path
def getStudentData(img1_path='',img2_path=''):
    img1_path = settings.MEDIA_ROOT+'/temp/img_000.bmp'
    img2_path1 = settings.MEDIA_ROOT+'/temp/img_001.bmp'
    
    similarity_score = compare_fingerprints(img1_path, img2_path1)
    if similarity_score>1: 
        print("we found person")
    else:
        print("we cant find person")
    print(f"Similarity score: {similarity_score}")


    context={
        'name':"Thanoon Younis",
        'id':99,
        'lesson':'mathmatic',
        'department':'computers',
        'phone_number':7704564613,
        'stage':'4th',
        'attend_time':getArrivalTime(),
    }
    return context