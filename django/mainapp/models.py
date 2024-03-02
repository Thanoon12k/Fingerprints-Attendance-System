import os
from django.db import models
DEPARTMENT_CHOICES = [
        ('computer_engineering', 'Computer Engineering'),
        ('electrical_engineering', 'Electrical Engineering'),
        ('construction', 'Construction Engineering'),
        ('power_and_electric_engineering', 'Power and Electric Engineering'),
         ]   
STAGE_CHOICES = [
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
    ]
STUDYTYPE_CHOICES=[
    ('morning','Morning'),
    ('evening','Evening'),
]

DAYOFWEEK_CHOICES = [
     ('sunday', 'Sunday'),
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
  
]

class Subject(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.TimeField() 
    day_of_week = models.CharField(max_length=255, choices=DAYOFWEEK_CHOICES,default='sunday')
    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES,default='computer_engineering')
    stage = models.CharField(max_length=255, choices=STAGE_CHOICES,default='4th')
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']  # Sort by id in descending order by default

def get_image_path(self, filename): 
        path= f'fingers/{self.name}_{self.phone_number}.bmp'   
        print('image fname', filename, 'saved in' ,path)
        return path

class Student(models.Model):
  
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES,default='computer_engineering')
    stage = models.CharField(max_length=255, choices=STAGE_CHOICES,default='4th')
    study_type = models.CharField(max_length=255, choices=STUDYTYPE_CHOICES,default='morning')
    fingerprint_image = models.ImageField(upload_to=get_image_path)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']  # Sort by id in descending order by default
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    attend_date = models.DateTimeField(auto_now_add=True)  # Automatically set to current date when created

    def __str__(self):
        return f"{self.student.name} - {self.class_name.name} ({self.attend_date}) "

    class Meta:
        ordering = ['-id']  # Sort by date in descending order by default
