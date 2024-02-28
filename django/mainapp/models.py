from django.db import models

class Stage(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Department(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']  # Sort by id in descending order by default

class Student(models.Model):
    name = models.CharField(max_length=255)
    class_name=models.ForeignKey(Subject, on_delete=models.CASCADE)
    stage = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    fingerprint_image = models.ImageField(upload_to='fingers/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']  # Sort by id in descending order by default


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    attend_date = models.DateField(auto_now_add=True)  # Automatically set to current date when created

    def __str__(self):
        return f"{self.student.name} - {self.class_name.name} ({self.attend_date}) "

    class Meta:
        ordering = ['-id']  # Sort by date in descending order by default
