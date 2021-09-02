from django.contrib import admin
#from django.contrib.admin.sites import site
from .models import Geust ,Movie ,Reservation
# Register your models here.

admin.site.register(Movie)
admin.site.register(Geust)
admin.site.register(Reservation)