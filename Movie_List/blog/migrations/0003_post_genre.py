# Generated by Django 5.0.6 on 2024-06-25 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_releasedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(default='Thriller, Biopic, Drama, War', max_length=50),
            preserve_default=False,
        ),
    ]
