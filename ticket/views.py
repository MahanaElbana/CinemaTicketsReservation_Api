from ticket import serializers
from ticket.models import Geust
from django.shortcuts import render
from django.http.response import JsonResponse 
from rest_framework.decorators import api_view
from .serializers import MovieSerializer , GeustSerializer ,ReservationSerializer
from rest_framework.response import Response
from rest_framework import status ,filters
# 1 without REST_FRAMEWORK and no model as static data

def static_data_no_rest_no_model(request):
    guests = [
        {
            "id": 1,
            "name": "Omar",
            "mobile": "01220771294",
            
        },
        {
            "id": 2,
            "name": "reham",
            "mobile": "01220881294"
        },
        {
            "id": 3,
            "name": "ahmed",
            "mobile": "01220881294"
        },
        {
            "id": 4,
            "name": "ali",
            "mobile": "01220881294"
        },
        {
            "id": 5,
            "name": "ibrahem",
            "mobile": "01220881294"
        },
    ]

    return JsonResponse(guests ,safe=False)

# 2 without REST_FRAMEWORK and using model 
def no_rest_model(request):
    data = Geust.objects.all()
    response = {
            "guests":list(data.values('name','mobile')),
       }
    
    return JsonResponse(response)

#3-1 
@api_view(['GET','POS'])
def FBV_list(request):

    #GET
    if request.method == 'GET':
        gesuts = Geust.objects.all()
        serializers = GeustSerializer(gesuts , many = True)
        return Response(serializers.data) 

    #POST
    elif request.method == 'POST':
        serializers = GeustSerializer(data = request.data)   
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status = status.HTTP_201_CREATED)
        return Response(serializers.data ,status = status.HTTP_400_BAD_REQUEST)    

#3-1
@api_view(['GET','PUT','DELETE'])
def FBV(request , pk):
    try:
       gesuts = Geust.objects.get(pk = pk) 
    except Geust.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

    #GET
    if request.method == 'GET':
        serializers = GeustSerializer(gesuts )
        return Response(serializers.data) 

    #POST
    elif request.method == 'PUT':
        serializers = GeustSerializer(gesuts, data = request.data)   
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status = status.HTTP_200_OK)
        return Response(serializers.errors ,status = status.HTTP_400_BAD_REQUEST)  

    if request.method == 'DELETE':
        gesuts.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)