from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'stage','class_name', 'phone_number', 'fingerprint_image']
