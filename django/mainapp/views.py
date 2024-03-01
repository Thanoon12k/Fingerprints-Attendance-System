import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.decorators import login_required

from mainapp.utils import getStudentData
from .forms import StudentForm
from .models import Student
from .utils import scanFingerprintImage
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

class MainScreen(LoginRequiredMixin,TemplateView):
    """Renders the main screen template."""
    model = Student  # Automatically fetches all students
    template_name = 'main.html'
    

class AddStudent(LoginRequiredMixin,CreateView):
    """Handles adding a new student."""
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'
    success_url = reverse_lazy('main_screen')  # Redirect to main screen after saving

class StudentsList(LoginRequiredMixin,ListView):
    """Lists all students."""
    model = Student
    template_name = 'students_list.html'
    context_object_name='students'


class EditStudent(LoginRequiredMixin,UpdateView):
    """Handles editing a student."""
    model = Student
    form_class = StudentForm
    template_name = 'edit_student.html'
    success_url = reverse_lazy('students_list')

class DeleteStudent(LoginRequiredMixin,DeleteView):
    """Handles deleting a student."""
    model = Student
    template_name = 'delete_student.html'
    success_url = reverse_lazy('students_list')

class ScanFinger(LoginRequiredMixin,TemplateView):
    template_name = 'scanfinger.html' 
    def get(self,request):
        image_url=settings.MEDIA_URL + 'images/fingerprint_logo.png'
        return render(request,self.template_name,{'fingerprint_image_url':image_url})
    def post(self,request):
        image_url,img_path=scanFingerprintImage()
        print(f'returned url: {image_url},   path: {img_path}')
        context=getStudentData(img_path)
        context['fingerprint_image_url']=image_url

        return render(request,self.template_name,context)

class StudentDetailView(LoginRequiredMixin,DetailView):
    model = Student
    template_name = 'student_details.html'
    context_object_name = 'student'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_fingerprintimage_url'] = scanFingerprintImage()
        return context

class RegisterAttendance(LoginRequiredMixin,TemplateView):
    template_name = 'register_attendance.html' # Make sure this matches the template name
    def get(self,request):
        image_url=settings.MEDIA_URL + 'images/fingerprint_logo.png'
        return render(request,self.template_name,{'fingerprint_image_url':image_url})
    def post(self,request):
        image_url,img_path=scanFingerprintImage()
        print(f'returned url: {image_url},   path: {img_path}')
        context=getStudentData(img_path)
        context['fingerprint_image_url']=image_url
        return render(request,self.template_name,context)
    
def process_image(request):
            image_url,img_path=scanFingerprintImage()
            print('scanned image url:',image_url)
            return JsonResponse({'scanned_image_url': image_url})
