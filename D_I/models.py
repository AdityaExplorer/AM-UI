from django.db import models
# from django.contrib.auth.models import User
# Create your models here.


class Create_Acc(models.Model):
    sno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200, default='')
    Password = models.CharField(max_length=200)
    Email_id = models.CharField(max_length=200, unique=True, default='')

class UserData(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)
    aadhaar = models.CharField(max_length=12, unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=200)
    document_path = models.CharField(max_length=255)
    doct_file_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name