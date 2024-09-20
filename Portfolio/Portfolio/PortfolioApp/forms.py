from django import forms
from .models import sample

class contactform(forms.ModelForm):
    class Meta:
        model = sample
        fields = ["Name","Email","Message"]
