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
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(username=request.data['username']).exists():
                return Response("User already exists")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonViewSet(viewsets.ViewSet):
    queryset = Person.objects.all()
    def list(self, request):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            if Person.objects.filter(first_name=request.data['first_name']).exists():
                return Response("User already exists")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class createUserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_vaild():
            user = serializer.save()
            person = serializer.save()
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)
            })


        """
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(username=request.data['username']).exists():
                return Response("User already exists")
            if request.data['password'] != request.data['password_match']:
                return Response('Passwords doesnt match')
            if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", request.data['password']):    
                return Response('Password must have atleast a upper and lower case letter along with a number and a special character')
            user = User.objects.create(
                email=request.data['email'],
                username=request.data['username'],
                password = make_password(request.data['password'])
                )       
            user.save()
            
            user_id = User.objects.latest('id')
            person = Person.objects.create(
                salutation = request.data['salutation'],
                first_name = request.data['first_name'],
                last_name = request.data['last_name'],
                age = request.data['age'],
                birthdate = request.data['birthdate'],
                user_id = user_id
            )
            person.save()
            
            return Response(status=status.HTTP_200_OK)
        """

class ProfileViewSet(viewsets.ViewSet):
    query_set = Profile.objects.all()
    
    