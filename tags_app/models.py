from django.db import models

class Tag(models.Model):
    tag_label = models.CharField(max_length=255, null=False, blank=False, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.tag_label}'