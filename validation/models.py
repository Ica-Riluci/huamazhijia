from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    sphone = models.CharField(max_length=20)
    pphone = models.CharField(max_length=20)
    school = models.CharField(max_length=100)
    emailadd = models.CharField(max_length=100)
    classx = models.CharField(max_length=100)
    grade = models.IntegerField()
    gender = models.IntegerField()
    potrait = models.ImageField(upload_to='upload/img/%Y/%m/%d')
    def __str__(self):
        return self.name
