from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView


from .views import *
urlpatterns=[

    path('',MainScreen.as_view(),name='main_screen'),
    path('about',About.as_view(),name='about_page'),
    path('add-student',AddStudent.as_view(),name='add_student'), 
    path('add-lesson',AddLesson.as_view(),name='add_lesson'), 
    path('students-list/', StudentsList.as_view(), name='students_list'),
    path('attendance-list/', AttendanceList.as_view(), name='attendance_list'),
    path('Lessons-list/', LessonsList.as_view(), name='lessons_list'),
    path('edit_student/<int:pk>/', EditStudent.as_view(), name='edit_student'),
    path('delete_student/<int:pk>/', DeleteStudent.as_view(), name='delete_student'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('register_attendance', RegisterAttendance.as_view(), name='register_attendance'),
    path('get-scanned-image', scan_finger_image, name='get_scanned_image'),
    path('get-student-data', get_student_data, name='get_student_data'),



    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]