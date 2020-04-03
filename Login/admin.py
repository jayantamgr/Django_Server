from django.contrib import admin
from .models import Person, Address, User, Profile
# Register your models here.

"""Registering the models here
for Django admin.

Admin can have a view and can manage data 
from the django admin site of the project
only if we register our models here.
"""
admin.site.register(Person)
admin.site.register(Address)
admin.site.register(User)
admin.site.register(Profile)