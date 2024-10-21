# Generated by Django 3.1.7 on 2023-12-04 00:21

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0004_auto_20231204_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torneo',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='titulo', unique_for_date=models.DateField()),
        ),
    ]