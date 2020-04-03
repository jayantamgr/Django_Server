from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import viewsets
from .models import Person, User, Profile
from Login.serializers import PersonSerializer, UserSerializer, CreateUserSerializer, ProfileSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from knox.models import AuthToken
import re
# Create your views here.

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """You can also validate data and change logic.
        This function only demonstrates to filter and see
        if provide user name is still available or not.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(username=request.data['user_name']).exists():
                return Response("User already exists")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonViewSet(viewsets.ViewSet):
    """ViewSet in Django is a class 
    based view consisting functions of 
    views like GET, POST etc.
    """
    queryset = Person.objects.all() # in class based views we need to query and return all the object instances of the model from the DB that we want to deeal with.
    def list(self, request):
        """GET request where it lists all the persons.
        """
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """POST request only for person model.
        """
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
    