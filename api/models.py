from django.db import models

# Create your models here.
class LoginUsers(models.Model):
    fullname = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)