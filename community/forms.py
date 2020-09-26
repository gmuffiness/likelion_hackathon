from django import forms
from .models import Post
import re

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','message', 'photo', 'tag_set', 'is_public']

    def clean_message(self):
        message = self.cleaned_data.get('message')
        return message