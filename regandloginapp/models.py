from django.db import models
# Create your models here.
class RegModel(models.Model):
    FirstName=models.CharField(max_length=10)
    LastName=models.CharField(max_length=10)
    UserName = models.CharField(max_length=10)
    Password=models.CharField(max_length=10)
    CPassword=models.CharField(max_length=10)
    EmailId=models.EmailField()
    MobileNo=models.IntegerField()