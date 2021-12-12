from django.shortcuts import render, redirect
import django.contrib.auth

from .models import Post
from .forms.publish_post import PublishPostForm


# Create your views here.
def main_page(request):
    posts = Post.objects.filter(is_public=True, is_deleted=False).order_by('-create_date', '-id').all()
    publish_post_form = PublishPostForm()
    context = {'title': "Hello World (context)",
               'posts': posts,
               'publish_post_form': publish_post_form,
               }
    return render(request, 'mainpage.html', context)


def publish_post_page(request):
    if request.method == "POST":
        form = PublishPostForm(request.POST, request.FILES)
        if form.is_valid():            
            form.save(user=request.user)
            next_page = request.GET.get('next', '/')
            return redirect(next_page)
    else:
        form = PublishPostForm()

    context = {
        'publish_post_form': form
    }
    return render(request, 'publish_post_form.html', context)