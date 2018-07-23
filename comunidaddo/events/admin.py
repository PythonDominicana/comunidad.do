from django.contrib import admin
from django import forms
from .models import Event, Region


class EventAdminForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = [
        'slug', 'created', 'last_updated',
        'title', 'description', 'url', 'image',
        'start_date', 'end_date', 'publish',
        'publish_date', 'address', 'country', 'city']
    readonly_fields = [
        'slug', 'created', 'last_updated',
        'title', 'description', 'url', 'image',
        'start_date', 'end_date', 'publish',
        'publish_date', 'address', 'country', 'city']


class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'last_updated']


admin.site.register(Region, RegionAdmin)
admin.site.register(Event, EventAdmin)
