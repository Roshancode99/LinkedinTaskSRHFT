from django.db import models

class Contacts(models.Model):
    username = models.CharField(max_length=122)
    email = models.EmailField(max_length=122) 
    password = models.CharField(max_length=12)
    confirm_password = models.CharField(max_length=12)
