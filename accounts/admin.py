from django.contrib import admin

# Register your models here.

from .models import *  # imports all models

admin.site.register(Profile)
