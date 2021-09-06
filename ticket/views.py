import rest_framework
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView #####
from .models import Geust, Movie, Reservation #####
from django.shortcuts import render #####
from django.http.response import JsonResponse  #####
from rest_framework.decorators import api_view  #####
from .serializers import MovieSerializer, GeustSerializer, ReservationSerializer  #####
from rest_framework.response import Response #####
from rest_framework import status, filters  , generics, mixins ,viewsets 

# -------------- permissions -----  authentication ---------- #
#from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
#from rest_framework.authentication import BaseAuthentication 

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

    return JsonResponse(guests, safe=False)

# 2 without REST_FRAMEWORK and using model


def no_rest_model(request):
    data = Geust.objects.all()
    response = {
        "guests": list(data.values('name', 'mobile')),
    }

    return JsonResponse(response)

# 3-1


@api_view(['GET','POS'])
def FBV_list(request):

    # GET
    if request.method == 'GET':
        gesuts = Geust.objects.all()
        serialize = GeustSerializer(gesuts, many=True)
        return Response(serialize.data)

    # POST
    elif request.method == 'POST':
        serializers = GeustSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)

# 3-1


@api_view(['GET', 'PUT', 'DELETE'])
def FBV(request, pk):
    try:
        gesuts = Geust.objects.get(pk=pk)
    except Geust.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET
    if request.method == 'GET':
        serializers = GeustSerializer(gesuts)
        return Response(serializers.data)

    # POST
    elif request.method == 'PUT':
        serializers = GeustSerializer(gesuts, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        gesuts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 4-1


class CBV_list(APIView):
    def get(self, request):
        guests = Geust.objects.all()
        serializers = GeustSerializer(guests, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = GeustSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# 4_2]


class CBV(APIView):

    def get_object(self, pk):
        try:
            return Geust.objects.get(pk=pk)
        except Geust.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # GET
    def get(self, request, pk):
        guest = self.get_object(pk)
        serializers = GeustSerializer(guest)
        return Response(serializers.data)

    # POST
    def put(self, request, pk):
        guest = self.get_object(pk)
        serializers = GeustSerializer(guest, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 5-1  Mixin => do not repeate
class mixins_list(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
 queryset = Geust.objects.all()
 serializer_class =GeustSerializer
 
 def get(self ,request):
     return self.list(request)

 def post(self ,request):
      return self.create(request)

# 5-2  Mixin => do not repeate
class mixins_pk(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
 queryset = Geust.objects.all()
 serializer_class =GeustSerializer

 def get(self ,request ,pk):
     return self.retrieve(request)

 def put(self ,request ,pk):
      return self.update(request)

 def delete(self ,request ,pk):
      return self.destroy(request)   

#6_1
class generics_list(generics.ListCreateAPIView):
    queryset =  Geust.objects.all()
    serializer_class = GeustSerializer
    # الاثونتكيشن علي مستوي الفيو 
    #authentication_classes = [authentication.BasicAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    #Token b1dc2ac53ab232220c597c2938ee1d39f7423eb
    

#6_2
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Geust.objects.all()
    serializer_class = GeustSerializer

#7_1_2
class views_list_pk(viewsets.ModelViewSet):
    queryset =  Geust.objects.all()
    serializer_class = GeustSerializer

class views_list_pk_movies(viewsets.ModelViewSet):
    queryset =  Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backend = [filters.SearchFilter]
    search_fields = ["movie"]

class views_list_pk_reservation(viewsets.ModelViewSet):
    queryset =  Reservation.objects.all()
    serializer_class = ReservationSerializer

#8]-find_movi
@api_view(['GET'])
def find_movi(request):
    movies = Movie.objects.filter(
        hall = request.data['hall'],
        movie = request.data['movie']
    )
    serializers = MovieSerializer(movies ,many= True)
    return Response(serializers.data)

#[9]-add_reservation
@api_view(['POST'])
def add_reservation(request):
    movie = Movie.objects.get(
        movie = request.data['movie'],
        hall = request.data['hall']
    )
    guest = Geust()
    guest.name = request.data['name']
    guest.mobile = request.data['mobile']
    guest.save()

    reserv = Reservation()
    reserv.geust = guest
    reserv.movie = guest
    reserv.save()

    serializer = ReservationSerializer(reserv ,many = True)
    return Response(serializer.data)    





# python -m django --version    
#pip install --upgrade django==3.9.5
#python -m django --version
#Pagination
#PyJWT
#graphql
#uuid