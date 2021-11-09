from django.contrib import admin
from smooth_api.main.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass
