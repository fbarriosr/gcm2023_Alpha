# Generated by Django 3.1.7 on 2024-04-15 10:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0037_auto_20240411_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardsInicio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('A', 'Actual'), ('P', 'Proximo')], default='A', max_length=20)),
                ('img', models.ImageField(upload_to='Paginas_Socio/')),
                ('titulo', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'CardInicio',
                'verbose_name_plural': 'CardsInicio',
                'ordering': ['titulo'],
            },
        ),
        migrations.AlterField(
            model_name='paginas_socio',
            name='tipo',
            field=models.CharField(choices=[('B', 'Bus'), ('E', 'Estacionamiento'), ('Cump', 'Cumpleaños'), ('C', 'Cuotas'), ('S', 'Salida'), ('R', 'Ranking'), ('CALEN', 'Calendario'), ('Noti', 'Noticias'), ('Multi', 'Multimedia')], default='B', max_length=20),
        ),
    ]
