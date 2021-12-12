from django.db import models
import django.contrib.auth

from tags_app.models import Tag


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(blank=False, null=False, default=False)
    is_public = models.BooleanField(default=True)
    author = models.ForeignKey(django.contrib.auth.get_user_model(), on_delete=models.CASCADE, null=False, blank=False)
    tags = models.ManyToManyField(Tag)
 