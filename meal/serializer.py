from django.contrib.auth.models import User
from rest_framework import serializers
from meal.models import Meal , Rating 

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id','title','description','number_of_rating','avarage_rating')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'meal','user','stars')       

# i make serializer for User .
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','password')       
        extra_kwargs = {'password': {'write_only': True ,'required':True}}
        

'''
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True ,'Required':True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
'''
