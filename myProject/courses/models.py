from django.db import models
from accounts.models import Instructor, Student
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
    # course_number = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section_number = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    time = models.CharField(max_length=100, null=True, blank=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

class GradeCriteria(models.Model):
    id = models.AutoField(primary_key=True)
    # grade_criteria = models.CharField(max_length=50)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    range_start = models.IntegerField()
    range_end = models.IntegerField()
    grade = models.CharField(max_length=50, null=True, blank=True)

class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    grade = models.CharField(max_length=50, null=True, blank=True)

class Assessment(models.Model):
    assessment_id = models.AutoField(primary_key=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    assessment_type = models.CharField(max_length=100)
    max_point = models.IntegerField()
    weight = models.IntegerField()
    date = models.DateField(null=True, blank=True)

class Score(models.Model):
    id = models.AutoField(primary_key=True)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    point = models.IntegerField(null=True, blank=True)

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
