from datetime import datetime, timedelta
from os import name
from django.db.models.query import QuerySet
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import *
from django.db.models import Q

from mainapp.comparing import getStudentData, scanFingerprintImage, temp_image_url
from .forms import StudentForm, SubjectForm
from .models import Attendance, Student, Subject
from .utils import getArrivalTime, getNowLesson
from django.contrib.auth.mixins import LoginRequiredMixin


class MainScreen(LoginRequiredMixin, TemplateView):
    model = Student  # Automatically fetches all students
    template_name = 'main.html'


class AddStudent(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'
    # Redirect to main screen after saving
    success_url = reverse_lazy('main_screen')


class StudentsList(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students_list.html'
    context_object_name = 'students'


class AttendanceList(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = 'attendance_list.html'
    context_object_name = 'attendances'
    def get_queryset(self) :
        all_data=Attendance.objects.all().order_by('id')
        search_term =self.request.GET.get('search_term') 

        if search_term and search_term != '':
           all_data = Attendance.objects.filter(
            Q(student__name__icontains=search_term) |
            Q(student__name__icontains=search_term) |
            Q(class_name__stage__icontains=search_term) 
        ).order_by('id')
        return all_data

class LessonsList(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'lesson_list.html'
    context_object_name = 'lessons'


class EditStudent(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'edit_student.html'
    success_url = reverse_lazy('students_list')


class DeleteStudent(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'delete_student.html'
    success_url = reverse_lazy('students_list')


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'student_details.html'
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_fingerprintimage_url'] = temp_image_url
        return context



class About(TemplateView):
    template_name = 'about.html'


class AddLesson(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'add_lesson.html'
    # Redirect to main screen after saving
    success_url = reverse_lazy('main_screen')

class RegisterAttendance(LoginRequiredMixin, TemplateView):
    # Make sure this matches the template name
    template_name = 'register_attendance.html'

    def get(self, request):
        context={}
        lesson_now=getNowLesson(minutes_allowed=60)
        if lesson_now:
            context={

                'lesson':lesson_now.name,
                'department':lesson_now.department,
                'attend_time':getArrivalTime(only_time=True),
                'stage':lesson_now.stage
           
            }
        else:
           context= {
                'no_lesson':'no_lesson'
        }
        return render(request,self.template_name,context)
    def post(self, request):
        student_id = request.POST.get('student_id')
        lesson_name = request.POST.get('lesson_name')
        lesson=Subject.objects.filter(name=lesson_name).first()
        print('less-name: ',lesson,'less-name: ',lesson_name,'  id:',student_id)
             
        if student_id and lesson:
            student = Student.objects.filter(id=student_id).first()
            thirty_minutes_ago = datetime.now() - timedelta(minutes=30)
            already_attend = Attendance.objects.filter(
                student=student,
                class_name=lesson,
                attend_date__gte=thirty_minutes_ago
            ).exists()

            if not already_attend:
                att = Attendance(student=student, class_name=lesson, attend_date=datetime.now())
                att.save()
                print('attend done')
            else:
                print('already attend')
        return render(request, 'main.html')


def scan_finger_image(request):
    scanFingerprintImage()
    print('scanned image url:', temp_image_url)
    return JsonResponse({'scanned_image': temp_image_url})


def get_student_data(request):
    context={}
    scanFingerprintImage()
    student = getStudentData()
    now_lesson=getNowLesson(minutes_allowed=30)
    now_time=getArrivalTime(day_of_week=True)
    if not now_lesson:
            context={'card_title':'Sorry no lesson allowed to attend now !!!'}
    elif student:
          context = {
                    "card_title": student.name,
                    "id": student.id,
                    "lesson": now_lesson.name,
                    "department": student.department,
                    "phone_number": student.phone_number,
                    "stage": student.department,
                    "scanned_image": temp_image_url,
                    "attend_time": now_time,
                }
    elif now_lesson and (not student) :
        context={
            'card_title':'no student Exist with this fingerprint !!',
            'lesson':now_lesson.name,
            'department':now_lesson.department,
            'stage':now_lesson.stage,
            "attend_time": now_time}

    context['scanned_image']=temp_image_url
    return render(request, 'register_attendance.html', context)
