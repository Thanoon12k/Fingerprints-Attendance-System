from django.urls import path
from .views import *
urlpatterns=[
    path('',MainScreen.as_view(),name='main_screen'),
    path('add_student',AddStudent.as_view(),name='add_student'), 
    path('students/', StudentsList.as_view(), name='students_list'),
    path('edit_student/<int:pk>/', EditStudent.as_view(), name='edit_student'),
    path('delete_student/<int:pk>/', DeleteStudent.as_view(), name='delete_student'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('scan_finger', ScanFinger.as_view(), name='scan_finger'),



]