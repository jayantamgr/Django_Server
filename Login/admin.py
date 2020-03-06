from django.contrib import admin
from .models import Person, Address, User, Profile
# Register your models here.
admin.site.register(Person)
admin.site.register(Address)
admin.site.register(User)
admin.site.register(Profile)