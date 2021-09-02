from django.contrib import admin

# Register your models here.
from .models import Category, Jobs

admin.site.register(Jobs)
admin.site.register(Category)