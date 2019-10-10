
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=225)
    enrollment = models.CharField(max_length=225)
    verbal_skills_score = models.IntegerField(default=0)
    technical_skills_score = models.IntegerField(default=0)
    percentage_tenth = models.FloatField(default=0)
    percentage_twelfth = models.FloatField(default=0)
    percentage_graduation = models.FloatField(default=0)
    skills = models.ManyToManyField('Skills', blank=True, related_name="student_skills")

    def __str__(self):
        return str(self.name) 

class Skills(models.Model):
    name = models.CharField(max_length=225)
    students = models.ManyToManyField(Student, null=True, blank=True, related_name="students")

    def __str__(self):
        return str(self.name)

class Companies(models.Model):
    company_name = models.CharField(max_length=300)
    packages_range = models.CharField(max_length=200)
    skills_included = models.ManyToManyField(Skills, null=True, blank=True, related_name='company_skills')
    student_eligible = models.ManyToManyField(Student, null=True, blank=True, related_name='eligible')
    tenth_criteria = models.FloatField(default=0)
    twelfth_criteria = models.FloatField(default=0)
    graduation_criteria = models.FloatField(default=0)

    def __str__(self):
        return str(self.company_name) + " : " + str(self.packages_range)



# from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


