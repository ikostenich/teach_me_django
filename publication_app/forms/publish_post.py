import django.contrib.auth
import re

from django.forms import ModelForm
from django import forms

from ..models import Post
from tags_app.models import Tag


class PublishPostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'is_public')


    @staticmethod
    def _extract_hashtags(text):
        regex = "#(\w+)"
        hashtag_list = re.findall(regex, text)
        return hashtag_list

    def save(self, user=None, commit=True):
        post = super(PublishPostForm, self).save(commit=False)
        post.author = user
        hashtags = self._extract_hashtags(post.text)
        if commit:
            post.save()
        for hashtag in hashtags:
            try:
                tag_object = Tag.objects.get(tag_label=hashtag)
            except Tag.DoesNotExist:            
                tag_object = Tag(tag_label=hashtag)
                tag_object.save()
            post.tags.add(tag_object)
        return post
