from rest_framework import serializers
from ticket.models import Movie ,Geust ,Reservation

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'        


class  GeustSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Geust 
        fields = ['pk','reservation' ,'name' ,'mobile']   