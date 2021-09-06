#from rest_framework import authentication ,permissions

from rest_framework import serializers, status
from rest_framework import permissions

from .permission import  Readalmost, UpdateOwnRating
from .models import Rating ,Meal
from .serializer import MealSerializer ,RatingSerializer,UserSerializer

from rest_framework import  viewsets 
from rest_framework import filters
from rest_framework.status import HTTP_202_ACCEPTED
####---------
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated ,IsAuthenticatedOrReadOnly
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
###----------
from django.contrib.auth.models import User
from rest_framework.response import Response 
from rest_framework.decorators import action
##! //////------------
from rest_framework.authtoken.models import Token


class Meal_list_pk(viewsets.ModelViewSet):
    queryset =  Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [Readalmost,IsAuthenticated]
    
    authentication_classes = [TokenAuthentication]
    #permission_classes =[IsAuthenticated]
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title","description"]
    
    @action(detail=True, methods=['post'])
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data :

            '''-- create and update --''' 
            meal = Meal.objects.get(id = pk)
            #username = request.data['username']
            stars = request.data['stars']
            #user =User.objects.get(username =username)
            user = request.user
            print(user)
            try:

              '''--update--'''
              rating = Rating.objects.get(meal=meal.id ,user=user.id )
              rating.stars = stars
              rating.save()
              serializers = RatingSerializer(rating ,many =False)
              jsonData = {
                  'update rating ':serializers.data
              }
              return  Response(jsonData ,status= status.HTTP_200_OK)

            except:
              ''' create '''
              rating = Rating.objects.create(meal=meal ,user=user ,stars =stars)
              serializers = RatingSerializer(rating ,many =False)
              jsonData = {
                  'created rating':serializers.data
              }
              return  Response(jsonData ,status= status.HTTP_202_ACCEPTED)

                    
        else :
          json ={'oops!':'star is not provided !'}
          return Response(json)


class Rating_list_pk(viewsets.ModelViewSet):
    #permission_classes = [UpdateOwnRating]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset =  Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["id","stars"]
    ''' the following permissions is always exist in the code'''
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        return Response({'you is not authenticated':'ya man sheflak barka akhed fyaha'})
    def create(self, request, *args, **kwargs):
        return Response({'you is not authenticated':'ya man sheflak barka akhed fyaha'})
### how to obtain token from authentication 
class LoginViewSet(viewsets.ViewSet):
   
    def create(self ,request):
        print(request)
        return ObtainAuthToken().as_view()(request =  request._request)
   
class createUserViewSet(viewsets.ViewSet):
    
    def create(self ,request):
       username= request.data['username']
       password =request.data['password'] 
       
       try:            
         user = User.objects.create(
           username= username,
           password =password
           )
         token , created= Token.objects.get_or_create(user=user)
         tokenKey = token.key
         print(created)
         serializers = UserSerializer(user ,many=False)
         return Response({'token': f'{tokenKey}','username':serializers.data})
       except:
           return Response({'user is created before':'register another user'})  

'''
https://www.programcreek.com/python/example/71197/rest_framework.permissions.SAFE_METHODS

''' 