from .models import Person, Address, User, Profile
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'salutation', 'first_name', 'last_name', 'age', 'birthdate']

class CreateUserSerializer(serializers.Serializer):
    UserModel = User.objects.all()
    PersonModel = Person.objects.all()

    class Meta:
        fields = ('UserModel', 'PersonModel')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        if validated_data['username'] and validated_data['passowrd'] and validated_data['password_match']is not None:
            if User.objects.filter(username=validated_data['username']).exists():
                return Response("User already exists")
            if validated_data['password'] != validated_data['password_match']:
                return Response('Passwords doesnt match')
            if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", validated_data['password']):    
                return Response('Password must have atleast a upper and lower case letter along with a number and a special character')
            user = User.objects.create(
                email=validated_data['email'],
                username=validated_data['username'],
                password = make_password(validated_data['password'])
                )     

            user_id = User.objects.latest('id')
            person = Person.objects.create(
                salutation = validated_data['salutation'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
                age = validated_data['age'],
                birthdate = validated_data['birthdate'],
                user_id = user_id
            )

            return user, person

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profileImage', 'frequentTraveller', 'hasBlog', 'occupation', 'motivation']