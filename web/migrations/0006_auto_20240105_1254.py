# Generated by Django 3.1.7 on 2024-01-05 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20240105_1159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='links',
            options={'ordering': ['-banner', 'tipo', 'order'], 'verbose_name': 'Link', 'verbose_name_plural': 'Links'},
        ),
    ]
