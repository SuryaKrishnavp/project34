from django.db import models

# Create your models here.
class products(models.Model):
    Name=models.CharField(max_length=50)
    Companyname=models.CharField(max_length=50)
    Price=models.IntegerField()
    Image=models.ImageField(upload_to='static/images/')
