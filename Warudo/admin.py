from django.contrib import admin

# Register your models here.
from Warudo import models

admin.site.register(models.Profile)
admin.site.register(models.Cosplayer)
admin.site.register(models.Convention)
