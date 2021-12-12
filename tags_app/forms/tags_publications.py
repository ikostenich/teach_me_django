from django.forms import ModelForm

from publication_app.models import Post

class TagsPublicationsForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'is_public')
