from django.db import models

# Create your models here.

class CarList(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    chasisnumber = models.CharField(max_length=100,blank=True,null=True)
    price=models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    

class UsersModel(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    mobile=models.CharField(max_length=12)
    salary=models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    dob=models.DateTimeField(blank=True,null=True)
    