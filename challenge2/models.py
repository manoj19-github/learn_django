from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator,MaxValueValidator
def alphanumeric(value):
    if not str(value).isalnum():
        raise ValidationError("Only alphanumeric and numbers are allowed")
    return value
class ShowroomModel(models.Model):
    name=models.CharField(max_length=40)
    location=models.CharField(max_length=100)
    website=models.URLField(max_length=100)
    
    def __str__(self):
        return self.name
 
class CarList(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    chasisnumber = models.CharField(max_length=100,blank=True,null=True,validators=[alphanumeric])
    price=models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    showroom=models.ForeignKey(ShowroomModel,on_delete=models.CASCADE,related_name="cars",null=True)
    def __str__(self):
        return self.name

   

class UsersModel(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    mobile=models.CharField(max_length=12)
    salary=models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    dob=models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.firstName.join([" ",self.lastName])

class ReviewModel(models.Model):
    rating = models.IntegerField(validators=[MaxValueValidator,MinValueValidator])
    comments = models.CharField(max_length=200,null=True)
    car = models.ForeignKey(CarList,on_delete=models.CASCADE,related_name="Reviews",null=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "The rating of "+self.car.name+" :----- "+str(self.rating)

