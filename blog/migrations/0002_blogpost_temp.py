# Generated by Django 3.2.5 on 2021-09-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='temp',
            field=models.TextField(blank=True, null=True),
        ),
    ]