
import os
from tkinter import image_names
from django.conf import settings
from datetime import datetime
from datetime import datetime
from django.db.models import Q

from mainapp.models import Student
from .connections import SCAN_IMAGE
from .comparing import compare_fingerprints
from pathlib import Path


temp_image_name='temp_000.bmp'
compare_folder=settings.BASE_DIR / 'media/fingers'
temp_image_path=settings.BASE_DIR / f'media/temp/{temp_image_name}'
temp_image_url='/media/temp/'+temp_image_name
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
    SCAN_IMAGE(temp_image_path)
    return temp_image_path

def getStudentData():

    for filename in os.listdir(compare_folder):
        compare_image_path = compare_folder / filename
        
        similarity_score = compare_fingerprints(str(temp_image_path), str(compare_image_path))
        if similarity_score > 1:        
            file_name = os.path.basename(compare_image_path)
            name, phone_number = file_name.split('_')[0], file_name.split('_')[1].split('.')[0]
            print(f'\n\nFound simsilarity: {name}, Phone: {phone_number} , vaue <  {similarity_score}  >')

            student = Student.objects.filter(Q(name__iexact=name) & Q(phone_number__iexact=phone_number)).first()
           
            if student:
                context = {
                    'name': student.name,
                    'id': student.id,
                    'lesson': 'mathmatic',
                    'department': 'computers',
                    'phone_number': student.phone_number,
                    'stage': '4th',
                    'scanned_image_url':temp_image_url,
                    'attend_time': getArrivalTime(),
                }
                print(f'Found in the database: {student.name}, Phone: {student.phone_number}')
                return context
            else:
                print('No student found with the given name and phone number.')
           
    print('no match was founding !!!')
    return {'name':'student not found !!'}
