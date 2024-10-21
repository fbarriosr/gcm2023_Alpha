# Generated by Django 3.1.7 on 2023-12-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20231229_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='eCivil',
            field=models.CharField(choices=[('S', 'SOLTERO'), ('C', 'CASADO'), ('V', 'VIUDO'), ('D', 'DIVORCIADO'), ('CCIVL', 'CONVIVIENTE CIVIL'), ('NI', 'NO INFORMAR')], default='NI', max_length=30, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(blank=True, max_length=12, verbose_name='Rut'),
        ),
    ]