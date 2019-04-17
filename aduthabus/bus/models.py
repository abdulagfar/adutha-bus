from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class AdminModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    admin_username=models.CharField(max_length=50,primary_key=True)
# Create your models here.
class bus_timetable(models.Model):
    bus_name=models.CharField(max_length=45)
    bus_no=models.CharField(max_length=45)
    st_1=models.CharField(max_length=45)
    t_1=models.TimeField()
    st_2=models.CharField(max_length=45,blank=True,null=True)
    t_2=models.TimeField(blank=True,null=True)
    st_3=models.CharField(max_length=45,blank=True,null=True)
    t_3=models.TimeField(blank=True,null=True)
    st_4=models.CharField(max_length=45,blank=True,null=True)
    t_4=models.TimeField(blank=True,null=True)
    st_5=models.CharField(max_length=45,blank=True,null=True)
    t_5=models.TimeField(blank=True,null=True)
    st_6=models.CharField(max_length=45,blank=True,null=True)
    t_6=models.TimeField(blank=True,null=True)