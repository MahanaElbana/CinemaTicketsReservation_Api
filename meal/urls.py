from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter 
from .views import Meal_list_pk , Rating_list_pk ,LoginViewSet ,createUserViewSet

routers = DefaultRouter()
routers.register('eating', Meal_list_pk)  
routers.register('rating', Rating_list_pk) 
routers.register('Login', LoginViewSet ,basename="login")  
routers.register('create', createUserViewSet ,basename="create")  

urlpatterns = [
    path('goto/', include(routers.urls))
]
    