from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    reg_no = models.CharField(max_length=9, primary_key=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
