from django.contrib import admin
from Warudo.models import Profile, Cosplayer, Address

# Register your models here.

admin.site.register(Profile)
# admin.site.register(models.Cosplayer)
admin.site.register(Address)


@admin.register(Cosplayer)
class CosAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("Name",)}
