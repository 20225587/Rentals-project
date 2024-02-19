from django.db import models

# Create your models here.
class room (models.Model):
    roomname = models.CharField(max_length=20,null=False,blank=True)
    roomtype= models.CharField(max_length=15,default='Single')
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.roomname