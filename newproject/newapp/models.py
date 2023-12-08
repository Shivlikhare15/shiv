from django.db import models

# Create your models here.
class Home(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    fathername = models.CharField(max_length=255)
    mothername = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    fathermobileno = models.CharField(max_length=255)
    mothermobileno = models.CharField(max_length=255)





