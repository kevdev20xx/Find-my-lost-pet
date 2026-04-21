from django.db import models


# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    
class LostPet(models.Model):
    profile_picture = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    bounty_for_information = models.BooleanField()  
    latitude = models.FloatField()    
    longitude = models.FloatField()    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class LostPetPicture(models.Model):
    picture_name = models.CharField(max_length=200)
    lost_pet = models.ForeignKey(LostPet,on_delete=models.CASCADE) 
    