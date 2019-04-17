from django.contrib import admin
from .models import AdminModel, bus_timetable
# Register your models here.

admin.site.register(bus_timetable)
admin.site.register(AdminModel)
