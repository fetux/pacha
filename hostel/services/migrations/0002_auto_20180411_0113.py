# Generated by Django 2.0.4 on 2018-04-11 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(),
        ),
    ]
