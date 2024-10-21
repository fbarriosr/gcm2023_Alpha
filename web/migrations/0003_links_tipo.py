# Generated by Django 3.1.7 on 2023-12-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20231214_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='tipo',
            field=models.CharField(choices=[('F', 'FEDERACION Y/O ASOCIACIÓN'), ('NR', 'NOTICIAS Y REVISTAS'), ('T', 'TIENDA'), ('TR', 'TOUR'), ('R', 'REGLAS'), ('NA', 'NO APLICA')], default='NA', max_length=20),
        ),
    ]
