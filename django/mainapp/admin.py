from django.contrib import admin
from .models import Student,Department,Attendance,Subject,Stage
# Register your models here.
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Attendance)
admin.site.register(Subject)
admin.site.register(Stage)