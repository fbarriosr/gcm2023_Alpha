# Generated by Django 3.1.7 on 2024-01-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0021_auto_20231229_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='torneo',
            name='list_inscritos',
            field=models.FileField(blank=True, max_length=254, upload_to='torneos/inscritos/', verbose_name='Listado de Inscritos'),
        ),
    ]
