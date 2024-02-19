from django.db import models

#from django.contrib.auth import User

class user(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30, blank=True)
    Area = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    
    def __str__(self):
        return self.firstname
