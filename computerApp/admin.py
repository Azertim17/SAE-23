from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Machine, Personnel, Event

admin.site.register(Machine)
admin.site.register(Personnel)
admin.site.register(Event)