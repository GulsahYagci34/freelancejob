from django import forms
from .models import Mission,Location,Category


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ["title","category","location","detail","budget"]

       