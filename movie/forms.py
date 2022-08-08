from django import forms
from .models import Actor, Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "a" in title:
            return title
        else: raise forms.ValidationError("This is not a valid title")
