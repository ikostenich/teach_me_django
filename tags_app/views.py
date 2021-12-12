from django.shortcuts import render

from .models import Tag
from .forms.tags import TagsForm
from .forms.tags_publications import TagsPublicationsForm
from publication_app.models import Post


def tags_page(request):
    tags = Tag.objects.all().order_by('create_date')
    tags_form = TagsForm()
    context = {
        'tags': tags,
        'tags_form': tags_form,
        }
    return render(request, 'tags.html', context)


def tag_posts(request, tag_label=None):
    tag = Tag.objects.get(tag_label=tag_label)
    publications = Post.objects.filter(tags__in=[tag]).all()
    tags_publication_form = TagsPublicationsForm()
    context = {
        'tag': tag,
        'publications': publications,
        'tags_publication_form': tags_publication_form,
        }
    return render(request, 'tags_publications.html', context)
