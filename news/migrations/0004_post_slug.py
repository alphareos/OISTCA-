# Generated by Django 3.2.5 on 2021-10-05 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
