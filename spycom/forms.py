
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField()
    message=forms.Textarea()
    class Meta:
        model = Post
        fields = '__all__'