from dataclasses import fields
from pyexpat import model
from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm

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


class DashBoardForm(forms.Form):
    text = forms.CharField(max_length=100,label="Enter Your Seach ")

class TodoForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'is_finished']

class ConversionForm(forms.Form):
    CHOICES=[('length','Length'),('mass','Mass')]
    measurement = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)


class ConversionLengthForm(forms.Form):
    CHOICES = [('yeard','Yeard'),('foot','Foot')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter the Number'}
    ))
    measure1 =  forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )

    measure2 =  forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )

class ConversionMassForm(forms.Form):
    CHOICES = [('pound','Pound'),('kilogram','Kilogram')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter the Number'}
    ))
    measure1 =  forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )

    measure2 =  forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )
    


class UserRegistationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']