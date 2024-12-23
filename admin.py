from django.contrib import admin
from .models import *

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email')
    search_fields = ('name', 'position', 'email') 
    list_filter = ('position',)
    ordering = ('name',) 
    fieldsets = (
        (None, {'fields': ('name', 'position', 'email')}),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name', 'description')  
    list_filter = ('start_date', 'end_date')
    ordering = ('-start_date',) 
    fieldsets = (
        (None, {'fields': ('name', 'description')}),
        ('Dates', {'fields': ('start_date', 'end_date')}),
    )


class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 1


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'project', 'role', 'hours_worked', 'date_assigned')
    search_fields = ('employee__name', 'project__name', 'role')
    list_filter = ('role', 'date_assigned')
    ordering = ('-date_assigned',) 
    autocomplete_fields = ('employee', 'project') 


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    search_fields = ('name', 'members__name')
    filter_horizontal = ('members',)
    inlines = [ParticipationInline] 
