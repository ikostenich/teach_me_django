# Generated by Django 3.2.9 on 2021-12-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags_app', '0001_initial'),
        ('publication_app', '0008_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='tags_app.Tag'),
        ),
    ]
