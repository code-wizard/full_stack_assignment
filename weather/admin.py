from django.contrib import admin
from weather import models
# Register your models here.


@admin.register(models.KhTmax)
class KhTmaxAdmin(admin.ModelAdmin):
    pass


@admin.register(models.KhTmin)
class KhTminAdmin(admin.ModelAdmin):
    pass


@admin.register(models.KhRainFall)
class KhRainfallAdmin(admin.ModelAdmin):
    pass