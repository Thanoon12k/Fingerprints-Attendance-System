
import os
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone

from mainapp.models import Student, Subject
from pathlib import Path




def getArrivalTime(only_time=False,day_of_week=False):
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

   
    if only_time:
        return f'{hours}:{minutes}  {period}'
    elif day_of_week:
        return  f"{day_of_week}  {day}/{month} {hours}:{minutes} {period}"
    else:
        return  f"{day}/{month}/{year} {hours}:{minutes} {period}"




def getNowLesson(minutes_allowed):
    day_of_week = timezone.now().strftime("%A").lower() # Convert to lowercase to match choices

    now_datetime =( datetime.combine(timezone.now().date(), timezone.now().time()))+ timedelta(hours=3)
    thirty_minutes_before = now_datetime - timedelta(minutes=minutes_allowed)
    thirty_minutes_after = now_datetime + timedelta(minutes=minutes_allowed)

    lessons = Subject.objects.filter(
        # day_of_week=day_of_week,
        start_time__gte=thirty_minutes_before,
        start_time__lte=thirty_minutes_after
    )
    
    if lessons.exists():
        print('leessons :',lessons)
        return lessons.first()
    else:
        print('no outgoing leesson :')
        return None
