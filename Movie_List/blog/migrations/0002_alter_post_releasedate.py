# Generated by Django 5.0.6 on 2024-06-25 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='releaseDate',
            field=models.DateField(),
        ),
    ]