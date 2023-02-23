
from django import forms
from projects.models import Project


class ContactUsForm(forms.Form):
    nom = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'