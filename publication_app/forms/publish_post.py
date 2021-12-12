import django.contrib.auth
from django.forms import ModelForm
from django import forms

from ..models import Post


class PublishPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'is_public')    

    def save(self, user=None, commit=True):
        post = super(PublishPostForm, self).save(commit=False)
        post.author = user
        if commit:
            post.save()
        return post
