from django.forms import ModelForm

from ..models import Tag

class TagsForm(ModelForm):

    class Meta:
        model = Tag
        fields = ('tag_label',)
