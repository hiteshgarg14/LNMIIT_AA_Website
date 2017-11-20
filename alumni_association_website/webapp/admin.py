from django.contrib import admin
from webapp.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'presenter', 'presenter_position' ,'status')
    list_filter = ('status', 'datetime')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status']

admin.site.register(Event, EventAdmin)
