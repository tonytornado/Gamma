from django.contrib import admin

# Register your models here.
from Accounts import models

admin.site.register(models.User)
