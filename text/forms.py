from django import forms
from . models import Person

class Personform(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['firstname','lastname','email','address']