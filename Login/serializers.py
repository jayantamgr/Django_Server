from .models import Person, Address, User, Profile
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    """This is a model serializer for the User object.
    Model serializer is a short cut to declare a serialzer 
    in which you can provide directly the fields below that you
    want serialize the incoming data as specified below.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PersonSerializer(serializers.ModelSerializer):
    """The person model serializer.
    """
    class Meta:
        model = Person
        fields = ['id', 'salutation', 'first_name', 'last_name', 'age', 'birthdate']

class CreateUserSerializer(serializers.Serializer):
    """This serializer is the User form serializer.
    When the user will fill up the entire form and post it, at first thee data 
    will reach here. 
    """
    UserModel = User.objects.all()      # instantiating User model
    PersonModel = Person.objects.all()  # instantiating Person model 

    class Meta:
        fields = ('UserModel', 'PersonModel') # We would want all data to serialize for both models
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        """Creates the user and user's person details.
        First: It validates the username if the given username still available.
        Second: Validates password using regex is password atleast contains an 
        Upper case, a Lower case, a number and a special character.

        PARAMETERS
        ----------
        validated_data: dict
            A dictionary or JSON with all the data provided by the user.
        """
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
    """Model Serializer for profile.
    TODO: 
        Needs data validation. 
    """
    class Meta:
        model = Profile
        fields = ['profileImage', 'frequentTraveller', 'hasBlog', 'occupation', 'motivation']