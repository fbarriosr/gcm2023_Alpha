# Generated by Django 3.1.7 on 2023-12-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0012_auto_20231204_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='monto',
            field=models.IntegerField(default=0, verbose_name='Monto Pagado'),
        ),
    ]