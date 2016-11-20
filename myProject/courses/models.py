from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    course_number = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    major = models.CharField(max_length=50)

class Section(models.Model):
    id = models.AutoField(primary_key=True)
    course_number = models.CharField(max_length=50)
    section_number = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    grade_criteria = models.CharField(max_length=50)
    time = models.CharField(max_length=100)
    instructor_id = models.IntegerField()
