from django.contrib import admin
from .models import Event, Leader, Language, Level, Cohort, Member

admin.site.register(Language)
admin.site.register(Level)

# admin.site.register(Cohort)
@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    list_display = ("event", "leader")

# admin.site.register(Member)
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", 'email')


@admin.register(Event)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')


@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone', 'email')
