from django.db import models
from django.utils import timezone
from Login.models import defaultModel, User, Profile, Person


import uuid
from PIL import Image
# Create your models here.

class Story(defaultModel):
    """A hitchhiker will add a story of
    his/her hitchhinking experiences in the
    form a story or blog.
    """
    place = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    fun_type = models.CharField(max_length=50)
    why_special = models.TextField()
    recommendations = models.TextField()
    for_all_ages = models.BooleanField()
    age_group = models.CharField(max_length=200)
    for_ladies = models.BooleanField()
    add_story = models.TextField()
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete = models.CASCADE)

    def __str__(self):
        return self.country

class Images(defaultModel):
    """Any user will upload images in the 
    user story will store in this model.
    """
    picture = models.ImageField()
    story_id = models.ForeignKey(Story, on_delete = models.CASCADE)
    description = models.TextField(null=True)

class Album(defaultModel):
    """Any album created for images will have the 
    data in this model.
    """
    album_name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete = models.CASCADE)

    def __str__(self):
        return self.album_name

class AlbumImages(defaultModel):
    """Images stored in any album will be stored
    in this model. 
    """
    image = models.ImageField()
    description = models.TextField(null=True)
    album_id = models.ForeignKey(Album, on_delete = models.CASCADE)


