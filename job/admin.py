from django.contrib import admin

# Register your models here.
from .models import Category, Jobs, Post

admin.site.register(Jobs)
admin.site.register(Category)
admin.site.register(Post)