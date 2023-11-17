from django.forms import ModelForm

from tinymce.widgets import TinyMCE

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ("slug",)
        widgets = {"body": TinyMCE()}
