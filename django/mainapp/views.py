from atexit import register
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.decorators import login_required

from mainapp.utils import getStudentData
from .forms import StudentForm, SubjectForm
from .models import Attendance, Student, Subject
from .utils import scanFingerprintImage,temp_image_url
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

class MainScreen(LoginRequiredMixin,TemplateView):
    model = Student  # Automatically fetches all students
    template_name = 'main.html'
    

class AddStudent(LoginRequiredMixin,CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'
    success_url = reverse_lazy('main_screen')  # Redirect to main screen after saving

class StudentsList(LoginRequiredMixin,ListView):
    model = Student
    template_name = 'students_list.html'
    context_object_name='students'

class AttendanceList(LoginRequiredMixin,ListView):
    model = Attendance
    template_name = 'attendance_list.html'
    context_object_name='attendance'
class LessonsList(LoginRequiredMixin,ListView):
    model = Subject
    template_name = 'lesson_list.html'
    context_object_name='lessons'


class EditStudent(LoginRequiredMixin,UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'edit_student.html'
    success_url = reverse_lazy('students_list')

class DeleteStudent(LoginRequiredMixin,DeleteView):
    model = Student
    template_name = 'delete_student.html'
    success_url = reverse_lazy('students_list')



class StudentDetailView(LoginRequiredMixin,DetailView):
    model = Student
    template_name = 'student_details.html'
    context_object_name = 'student'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_fingerprintimage_url'] =temp_image_url
        return context

class RegisterAttendance(LoginRequiredMixin,TemplateView):
    template_name = 'register_attendance.html' # Make sure this matches the template name
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['scanned_image_url'] = 'media/images/fingerprint_logo.png' # Add your variable here
        return context
    def post(self,request):
                student_id=request.POST.get('student_id')
                if student_id:
                      student_obj=Student.objects.filter(id=student_id).first()
                       
                      att=Attendance(student=student_obj,class_name=Subject.objects.first(),attend_date=datetime.now().date())
                      att.save()
                      pass
                return render(request,'main_screen.html')
class About(TemplateView):
      template_name='about.html'

class AddLesson(LoginRequiredMixin,CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'add_lesson.html'
    success_url = reverse_lazy('main_screen')  # Redirect to main screen after saving


def scan_finger_image(request):
            scanFingerprintImage()
            print('scanned image url:',temp_image_url)
            return JsonResponse({'scanned_image_url': temp_image_url})
def get_student_data(request):
          
            scanFingerprintImage()
            studentdata=getStudentData()
            return render(request,'register_attendance.html',studentdata)
