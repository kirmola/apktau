from django.contrib import admin

from .models import *

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Apps)
class AppsAdmin(admin.ModelAdmin):
    pass

