from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50,primary_key=True)
    year = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    major = models.CharField(max_length=50)
