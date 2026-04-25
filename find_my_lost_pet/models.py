from django.db import models


# Create your models here.

class CustomUser(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name + " - " + self.email
    
class LostPet(models.Model):
    profile_picture = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    bounty_for_information = models.BooleanField()  
    latitude = models.FloatField()    
    longitude = models.FloatField()    
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class LostPetPicture(models.Model):
    picture_name = models.CharField(max_length=200)
    lost_pet = models.ForeignKey(LostPet,on_delete=models.CASCADE) 
    