from django.contrib import admin
from website import models
# Register your models here.

admin.site.register(models.command)
admin.site.register(models.person)