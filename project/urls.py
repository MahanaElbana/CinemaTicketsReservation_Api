"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path ,include
from ticket import views
from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token
# --------  static files --------
from django.conf import settings
from django.conf.urls.static import static
# --------  static files --------
routers = DefaultRouter()
routers.register("guest", views.views_list_pk)  # tries
routers.register("movie", views.views_list_pk_movies)  # tries
routers.register("reservation", views.views_list_pk_reservation)  # tries

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1 without REST_FRAMEWORK and no model as static data
    path('django/staticDataNoRestNoModel/',
         views.static_data_no_rest_no_model),

    # 2
    path('django/datafrommodelnorest/', views.no_rest_model),

    # 3-1
    path('rest_fremwork/FBV_list/',views.FBV_list),
    # 3-2
    path('rest_fremwork/FBV/<int:pk>', views.FBV),

    #! ////////----------
    #path('ioio/', post_list),
    # path('io/',Post_list_CBV.as_view()),

    # 4-1
    path('rest_fremwork/CBV_list/',views.CBV_list.as_view(), name="cbv list model"),
    path('rest_fremwork/CBV/<int:pk>', views.CBV.as_view(), name="cbv model"),

    # 5
    path('rest_fremwork/mixin_list/', views.mixins_list.as_view()),
    ### Another method
    path('api/', include('ticket.urls')),
    path('rest_fremwork/Mixin/<int:pk>', views.mixins_pk.as_view()),

    # generics_list
    path('rest_fremwork/generics_list/', views.generics_list.as_view()),
    path('rest_fremwork/generics_pk/<int:pk>', views.generics_pk.as_view()),

    # 7viewsets
    path('rest_fremwork/viewsets/', include(routers.urls)),

    #8-find
    path('rest_fremwork/findMovie/', views.find_movi),
    #9-add_reservation
    path('rest_fremwork/addreservation/', views.add_reservation),
    



    path('mealapi/', include('meal.urls')),

    ##----- restfram
    path('api-auth/', include('rest_framework.urls')),

    ## token 
    path('api-token-auth/', obtain_auth_token),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
