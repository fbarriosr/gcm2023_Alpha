# Generated by Django 3.1.7 on 2023-12-04 00:13

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='titulo<django.db.models.fields.DateField>'),
        ),
    ]
