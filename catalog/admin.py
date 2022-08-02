from django.contrib import admin
from .models import Event, Leader, Language, Level


admin.site.register(Language)
admin.site.register(Level)


@admin.register(Event)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'leader')


@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone', 'email')
