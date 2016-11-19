from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.IntegerField(primary_key=True)
    student_picture = models.CharField(max_length=500)
    major = models.CharField(max_length=100)

class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instructor_id = models.IntegerField(primary_key=True)
    degree = models.CharField(max_length=100)
    instructor_picture = models.CharField(max_length=500)
    department = models.CharField(max_length=100)
