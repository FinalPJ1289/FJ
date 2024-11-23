from django import forms
from .models import *

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset = Category.objects.all(),
        widget = forms.Select,
        required = True
    )

    class Meta:
        model = Post
        fields = ['title', 'body', 'category']