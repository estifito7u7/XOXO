from django.contrib import admin
from .models import User, Profile, UserLibrary
# Register your models here.

admin.site.register(User)
admin.site.register(UserLibrary)
admin.site.register(Profile)