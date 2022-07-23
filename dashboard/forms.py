from django import forms
from . models import *
import django.forms.widgets

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description',]


class DateInput(forms.DateInput):
    input_type:'date'

class HomeWorkForm(forms.ModelForm):
    class Meta:
        model = HomeWork
        widgets = {
    'due': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
}
        fields = ['subject', 'title','description', 'due','is_finished']