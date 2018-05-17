# Generated by Django 2.0.4 on 2018-05-13 01:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('text', ckeditor.fields.RichTextField()),
                ('title_es', models.CharField(max_length=25, verbose_name='Titulo')),
                ('text_es', ckeditor.fields.RichTextField(verbose_name='Texto')),
            ],
            options={
                'verbose_name_plural': 'Activities',
                'verbose_name': 'Activities',
            },
        ),
    ]