from django.db import models

class data(models.Model):
    poster=models.ImageField(upload_to='uploads/') 
    eve=models.CharField(max_length=20)
    date=models.DateField(max_length=20)
    venue=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    link=models.CharField(max_length=100)
