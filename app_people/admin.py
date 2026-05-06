from django.contrib import admin

from app_people import models

# Register your models here.

@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    pass
