# Generated by Django 3.1.7 on 2024-05-13 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0057_auto_20240511_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='torneo',
            name='ticket',
            field=models.IntegerField(default=7000),
        ),
    ]
