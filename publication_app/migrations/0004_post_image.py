# Generated by Django 3.2.9 on 2021-12-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0003_post_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
