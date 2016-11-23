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

class GradeCriteria(models.Model):
    id = models.AutoField(primary_key=True)
    grade_criteria = models.CharField(max_length=50)
    range_start = models.IntegerField()
    range_end = models.IntegerField()
    grade = models.CharField(max_length=50)

class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField()
    section_number = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)

class Assessment(models.Model):
    assessment_id = models.AutoField(primary_key=True)
    section_number = models.CharField(max_length=50)
    assessment_type = models.CharField(max_length=100)
    max_point = models.IntegerField()
    weight = models.IntegerField()
    date = models.DateField()

class Score(models.Model):
    id = models.AutoField(primary_key=True)
    enrollment_id = models.IntegerField()
    assessment_id = models.IntegerField()
    point = models.IntegerField()

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    enrollment_id = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=50)
