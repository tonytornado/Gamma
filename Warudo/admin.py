from django.contrib import admin

# Register your models here.
from Warudo import models


@admin.register(models.LocalCity, models.LocalState)
class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Profile)
admin.site.register(models.Cosplayer)
admin.site.register(models.Convention)
