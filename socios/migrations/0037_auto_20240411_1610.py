# Generated by Django 3.1.7 on 2024-04-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0036_auto_20240410_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginas_socio',
            name='tipo',
            field=models.CharField(choices=[('B', 'Bus'), ('E', 'Estacionamiento'), ('Cump', 'Cumpleaños'), ('C', 'Cuotas'), ('S', 'Salida'), ('R', 'Ranking')], default='B', max_length=20),
        ),
        migrations.AddField(
            model_name='paginas_socio',
            name='tituloPestana',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
