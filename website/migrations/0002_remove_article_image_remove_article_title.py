# Generated by Django 5.0.6 on 2024-05-17 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
    ]
