# Generated by Django 3.1.7 on 2024-04-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0039_auto_20240415_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='elclub',
            name='img',
            field=models.ImageField(blank=True, upload_to='ElClub/'),
        ),
    ]
