# Generated by Django 3.2.5 on 2021-09-02 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='temp',
        ),
    ]
