from django.contrib import admin
from .models import Meal , Rating
# Register your models here.

class ReatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'meal','user','stars']
    list_filter = ['meal','user']



class MealAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description','number_of_rating','avarage_rating']
    list_filter = ['title', 'description']   
    search_fields = ['title', 'description']  

admin.site.register(Meal ,MealAdmin)
admin.site.register(Rating ,ReatingAdmin)