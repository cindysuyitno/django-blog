from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title)<5:
            raise forms.ValidationError('Please enter a valid title')
        else: return title