from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class VehicleModel(models.Model):

    colors = [
        ('White','White'),
        ('Black','Black'),
        ('Green','Green'),        
        ('Red','Red'),
        ('Blue','Blue'),
        ('Silver','Silver'),
        ('Grey','Grey'),    
        ('Yellow','Yellow'),        
    
    ]

    make = [
        ('Alfa Romeo','Alfa Romeo'),
        ('Audi','Audi'),
        ('BMW','BMW'),
        ('Chevrolet','Chevrolet'),
        ('Ford','Ford'),
        ('Honda','Honda'),
        ('Hyundai','Hyundai'),
        ('Jaguar','Jaguar'),
        ('Jeep','Jeep'),
        ('Kia','Kia'),
        ('Land Rover','Land Rover'),
        ('Lexus','Lexus'),
        ('Mercedes Benz','Mercedes Benz'),
        ('Mini cooper','Mini cooper'),
        ('Mitsubishi','Mitsubishi'),
        ('Subaru','Subaru'),
        ('Suzuki','Suzuki'),
        ('Renault','Renault'),
        ('Toyota','Toyota'),
        ('Volkswagen','Volkswagen'),
        ('Volvo','Volvo'),
        
    ]

    theStatus = [
        ('Drive In','Drive In'),
        ('Washing in Progress','Washing in Progress'),
        ('Car wash Finished','Car wash Finished'),        
    ]

    TheUser = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    TheDateEntered = models.DateTimeField(auto_now_add=True)
    TheVehicleMake = models.CharField(choices=make, max_length=50)
    TheDriverName = models.CharField(max_length=50, default="")
    TheColor = models.CharField(choices=colors, max_length=50)
    TheRegistrations = models.CharField(max_length=12, null=True, default="")
    ThePhoneNumber = models.CharField(max_length=15)
    #TheStatus = models.CharField(choices=theStatus, max_length=50, null=True, default="None")
    
    def __str__(self):
        return self.TheVehicleMake

