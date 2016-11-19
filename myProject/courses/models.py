from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50,primary_key=True)
    year = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    major = models.CharField(max_length=50)

class Section(models.Model):
    number = models.CharField(max_length=50,primary_key=True)
    year = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    range_start = models.CharField(max_length=100)
    range_end = models.CharField(max_length=100)
    grade = models.CharField(max_length=50)
    time = models.DateTimeField()
