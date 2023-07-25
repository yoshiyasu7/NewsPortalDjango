from django import forms

from .views import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=255)

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            'category',
        ]
