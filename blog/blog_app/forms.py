from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(max_length=100)


from django import forms
from .models import Blog

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'content']
