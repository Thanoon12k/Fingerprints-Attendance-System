from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude=[]
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        # Set the default value for the stage field
        self.fields['stage'].initial = '4th'
        self.fields['department'].initial = 'computer_engineering'
