from django.contrib import admin
from .models import Event, Leader, EventInstance


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'leader', "level", 'language')

#
# @admin.register(Leader)
# class LeaderAdmin(admin.ModelAdmin):
#     list_display = ('phone')
admin.site.register(Leader)


@admin.register(EventInstance)
class EventInstanceAdmin(admin.ModelAdmin):
    list_display = ('cohort', 'status',  'attendee', 'id')
    list_filter = ('cohort', 'status')

    fieldsets = (
        (None, {
            'fields': ('cohort','id')
        }),
        ('Sign-ups', {
            'fields': ('status', 'attendee')
        }),
    )
