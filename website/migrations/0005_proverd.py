# Generated by Django 5.0.6 on 2024-05-19 05:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_article_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proverd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200, verbose_name='Заголовок')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Содержание')),
                ('author', models.CharField(max_length=200, verbose_name='Автор рассказа')),
            ],
        ),
    ]
