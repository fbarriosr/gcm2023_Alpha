# Generated by Django 3.1.7 on 2024-03-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0017_auto_20240305_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='condicion',
            field=models.CharField(blank=True, choices=[('R', 'RETIRO'), ('A', 'ACTIVO'), ('NI', 'NO INFORMAR')], default='NI', max_length=20),
        ),
    ]