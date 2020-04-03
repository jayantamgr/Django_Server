from django.db import models
from django.utils import timezone
import uuid
from PIL import Image
# Create your models here.

class defaultModel(models.Model):
    """The default object or data model where
    all the other objects, data model or columns 
    will inherit this model so that all the tables
    in the database will have:
        1. Primary key: "id",
        2. Time stamp, "created_at" when user creates for first time. 
        3. Time stamp, "updated_at" when user updates the same. 
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.updated_at = timezone.now()
        return super(defaultModel, self).save(*args, **kwargs)

class User(defaultModel):
    """The user model belonging to user form consists 
    of user_name for the user to create one, user email 
    and select a password.
    """
    user_name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.user_name   

class Person(defaultModel):
    """In the user form, a user can provide the fields specified 
    in this class. Here the user_id is the foreign_key of the model
    "User". This object defines the personal details of the user
    """
    salutation_choices = [
        ('Mr.', 'Mister'),
        ('Ms.', 'Miss'),
        ('Mrs.', 'Mistress')
        ]
    salutation = models.CharField(max_length=4, choices=salutation_choices, default=None)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    birth_date = models.CharField(max_length=15)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

class Address(defaultModel):
    """This model defines the postal address of the User.
    Relation is person_id from the model, "Person"
    """
    address_1 = models.CharField(max_length=30)
    address_2 = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=15, null=False)
    state = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=20, null=False)
    post_code = models.IntegerField(null=False)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return "{:s},  {:s},  {:s} ".format(self.country, self.state, self.city) # show the admin for each row with country, state and city

    class Meta:
        ordering = ['country']  # Order all address by country.   

class Profile(defaultModel):
    """The user has a profile, he can upload the profile image
    and specify other details specified in this model. 
    """
    profile_Image = models.ImageField()
    frequent_traveller = models.BooleanField(default=False)     # frequent_traveller means if user travels frequently for vacation.
    has_blog = models.URLField(null=True)                       # has_blog means if the user is a blogger.
    occupation = models.CharField(max_length=30, null=True)
    motivation = models.TextField()                             # what is the motivation of being a traveller or hitchhiker or just being on this social application
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.profileImage   

