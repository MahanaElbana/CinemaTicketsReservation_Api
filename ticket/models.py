from django.db import connection, models
from rest_framework.authentication import TokenAuthentication

# Create your models here.

### -------------auto generate Token ---------------- ###
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save

from django.dispatch import receiver
from django.conf import settings
### --------------------------------------------- ###

class Movie(models.Model):
    hall = models.CharField(max_length = 10)
    movie = models.CharField(max_length = 10)
    data = models.DateField()
    
    def __str__(self):
        return self.movie

class Geust(models.Model):
    name = models.CharField(max_length = 10)
    mobile = models.CharField(max_length = 10)
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    movie = models.ForeignKey(
        Movie, related_name = "reservation", on_delete=models.CASCADE)
    geust = models.ForeignKey(
        Geust, related_name = "reservation", on_delete=models.CASCADE)

### -------------auto generate Token ---------------- ###    
@receiver(post_save ,sender=settings.AUTH_USER_MODEL)
def TokenCreated(sender ,instance ,created ,**kwargs):
    #print(sender ,instance ,created , kwargs)
    if created:
        token = Token.objects.create(user=instance)
        print(token.key)   

## Django123   ==> password for superUser 
##! def create_user(sender ,**kwargs):
##!     print(kwargs)
##!     if kwargs['created']:
##!           Token.objects.create(user=kwargs['instance'])
##!           
##! post_save.connect(create_user , sender = settings.AUTH_USER_MODEL)          