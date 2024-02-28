from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import StudentForm
from .models import Student
from django.conf import settings

# Create your views here.

class MainScreen(ListView):
    """Renders the main screen template."""
    model = Student  # Automatically fetches all students
    template_name = 'main.html'

class AddStudent(CreateView):
    """Handles adding a new student."""
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'
    success_url = reverse_lazy('main_screen')  # Redirect to main screen after saving

class StudentsList(ListView):
    """Lists all students."""
    model = Student
    template_name = 'students_list.html'
    context_object_name='students'

class EditStudent(UpdateView):
    """Handles editing a student."""
    model = Student
    form_class = StudentForm
    template_name = 'edit_student.html'
    success_url = reverse_lazy('students_list')

class DeleteStudent(DeleteView):
    """Handles deleting a student."""
    model = Student
    template_name = 'delete_student.html'
    success_url = reverse_lazy('students_list')

class ScanFinger(TemplateView):
    template_name = 'scanfinger.html' # Make sure this matches the template name
     
class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_details.html'
    context_object_name = 'student'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_fingerprintimage_url'] = scanFingerprintImage()
        return context
def scanFingerprintImage():
    img=settings.MEDIA_URL + 'fingers/OIP.jpg'
    return img