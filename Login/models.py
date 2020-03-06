from django.db import models
from django.utils import timezone



import uuid
from PIL import Image
# Create your models here.

class defaultModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.updated_at = timezone.now()
        return super(defaultModel, self).save(*args, **kwargs)

class User(defaultModel):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.username   

class Person(defaultModel):
    salutation_choices = [
        ('Mr.', 'Mister'),
        ('Ms.', 'Miss'),
        ('Mrs.', 'Mistress')
        ]
    salutation = models.CharField(max_length=4, choices=salutation_choices, default=None)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    birthdate = models.CharField(max_length=15)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

class Address(defaultModel):
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=15, null=False)
    state = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=20, null=False)
    postcode = models.IntegerField(null=False)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return "{:s},  {:s},  {:s} ".format(self.country, self.state, self.city)

    class Meta:
        ordering = ['country']    

class Profile(defaultModel):
    profileImage = models.ImageField()
    frequentTraveller = models.BooleanField(default=False)
    hasBlog = models.URLField(null=True)
    occupation = models.CharField(max_length=30, null=True)
    motivation = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.profileImage   

