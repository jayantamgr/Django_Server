from django.db import models
from django.utils import timezone
from Login.models import defaultModel, User, Profile, Person


import uuid
from PIL import Image
# Create your models here.

class Story(defaultModel):
    place = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    fun_type = models.CharField(max_length=50)
    why_special = models.TextField()
    recommendations = models.TextField()
    forAllAges = models.BooleanField()
    age_group = models.CharField(max_length=200)
    forLadies = models.BooleanField()
    addStory = models.TextField()
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete = models.CASCADE)

    def __str__(self):
        return self.country

class Images(defaultModel):
    picture = models.ImageField()
    story_id = models.ForeignKey(Story, on_delete = models.CASCADE)
    description = models.TextField(null=True)

class Album(defaultModel):
    album_name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete = models.CASCADE)

    def __str__(self):
        return self.album_name

class AlbumImages(defaultModel):
    image = models.ImageField()
    description = models.TextField(null=True)
    album_id = models.ForeignKey(Album, on_delete = models.CASCADE)


