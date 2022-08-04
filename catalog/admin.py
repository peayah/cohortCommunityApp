from django.contrib import admin
from .models import Event, Leader, Language, Level, EventInstance

admin.site.register(Language)
admin.site.register(Level)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')


@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone', 'email')


@admin.register(EventInstance)
class EventInstanceAdmin(admin.ModelAdmin):
    list_display = ('cohort', 'status', 'attendee', 'id')
    list_filter = ('cohort', 'status')

    fieldsets = (
        (None, {
            'fields': ('cohort','id')
        }),
        ('Sign-ups', {
            'fields': ('status', 'attendee')
        }),
    )
