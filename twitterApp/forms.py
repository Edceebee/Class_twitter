from django import forms

from .models import TwitterPost


class PostForm(forms.ModelForm):
    class Meta:
        model = TwitterPost
        fields = ('name', 'body',)
