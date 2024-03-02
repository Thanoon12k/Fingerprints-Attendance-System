from django import forms
from .models import Student, Subject

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude=[]

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        exclude=[]
