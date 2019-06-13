from django.contrib.auth.models import User
from django.db import models

#extended-user model

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image',blank=True)
    phone = models.CharField(max_length=11)
    IBAN = models.CharField(max_length=24)
    about = models.TextField(max_length=500,verbose_name="Özet Bilgi")
    abilities = models.TextField(max_length=300,verbose_name="Yetenekler")