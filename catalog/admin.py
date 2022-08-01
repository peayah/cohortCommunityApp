from django.contrib import admin
from .models import Event, Leader, Language, Level

# Register your models here.
admin.site.register(Event)
admin.site.register(Leader)
admin.site.register(Language)
admin.site.register(Level)
