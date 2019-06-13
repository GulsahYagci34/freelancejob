from django import forms
from .models import Category,Location,Mission

class CategoryForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)


class LocationForm(forms.ModelForm):
    location = forms.ModelChoiceField(queryset=Location.objects.all(),required=False)


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ["title","category","location","mission","budget"]


