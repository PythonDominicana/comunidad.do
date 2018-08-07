from django import forms
from .models import Event, Region


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 'description',
            'url', 'image', 'start_date',
            'end_date', 'address', 'country',
            'city', 'user', 'region']
        widgets = {
            'user': forms.HiddenInput()}


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['name']
