from django.db import models

# Create your models here.


class Movie(models.Model):
    hall = models.CharField(max_length = 10)
    movie = models.CharField(max_length = 10)
    data = models.DateField()


class Geust(models.Model):
    name = models.CharField(max_length = 10)
    mobile = models.CharField(max_length = 10)


class Reservation(models.Model):
    movie = models.ForeignKey(
        Movie, related_name = "reservation", on_delete=models.CASCADE)
    geust = models.ForeignKey(
        Geust, related_name = "reservation", on_delete=models.CASCADE)
