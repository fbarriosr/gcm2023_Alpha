# Generated by Django 3.1.7 on 2023-12-29 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20231229_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='date_of_birth',
        ),
    ]