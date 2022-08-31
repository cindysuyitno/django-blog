from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','text',)

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data['title']
        if len(title)>6:
            raise forms.ValidationError('Enter valid title')
        else: return title

class FormNew(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        a = Post(title=self.cleaned_data['title'], text=self.cleaned_data['text'])
        return a
