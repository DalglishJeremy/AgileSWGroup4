from django.forms import ModelForm, TextInput
from .models import City
from django import forms

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } 

class BaseballDateForm(forms.Form):
    date_field = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))