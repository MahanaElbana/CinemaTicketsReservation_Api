from django.urls import path 
from .views import mixins_list

urlpatterns = [
   # path('mixin-api/', mixins_list.as_view()),
    path('mixin-api/', mixins_list.as_view()),
]