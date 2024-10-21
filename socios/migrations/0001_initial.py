# Generated by Django 3.1.7 on 2023-12-03 23:30

import autoslug.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='noticias/')),
                ('fecha', models.DateField()),
                ('resumen', models.CharField(max_length=200)),
                ('info', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='titulo')),
                ('is_active', models.BooleanField(default=False, verbose_name='Activo')),
                ('is_aprobado', models.BooleanField(default=False, verbose_name='Aprobado')),
                ('is_pendiente', models.BooleanField(default=True, verbose_name='Pendiente')),
                ('img1', models.ImageField(blank=True, upload_to='noticias/')),
                ('img2', models.ImageField(blank=True, upload_to='noticias/')),
                ('img3', models.ImageField(blank=True, upload_to='noticias/')),
                ('img4', models.ImageField(blank=True, upload_to='noticias/')),
                ('img5', models.ImageField(blank=True, upload_to='noticias/')),
                ('direccion', models.CharField(blank=True, max_length=200)),
                ('region', models.CharField(choices=[('I', 'Región de Tarapacá  '), ('II', 'Región de Antofagasta  '), ('III', 'Región de Atacama  '), ('IV', 'Región de Coquimbo  '), ('V', 'Región de Valparaíso    '), ('VI', 'Región del Libertador General Bernardo O’Higgins    '), ('VII', 'Región del Maule    '), ('VIII', 'Región del Bio-bío  '), ('IX', 'Región de La Araucanía  '), ('X', 'Región de Los Lagos '), ('XI', 'Región Aysén del General Carlos Ibáñez del Campo '), ('XII', 'Región de Magallanes y Antártica Chilena   '), ('XIII', 'Región Metropolitana de Santiago    '), ('XIV', 'Región de Los Ríos '), ('XV', 'Región de Arica y Parinacota   '), ('XVI', 'Región de Ñuble ')], default='XIII', max_length=50, verbose_name='Region')),
                ('comentario', models.TextField(default='Sin comentario')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('direccion', models.CharField(max_length=200, verbose_name='Direccion')),
                ('region', models.CharField(choices=[('I', 'Región de Tarapacá  '), ('II', 'Región de Antofagasta  '), ('III', 'Región de Atacama  '), ('IV', 'Región de Coquimbo  '), ('V', 'Región de Valparaíso    '), ('VI', 'Región del Libertador General Bernardo O’Higgins    '), ('VII', 'Región del Maule    '), ('VIII', 'Región del Bio-bío  '), ('IX', 'Región de La Araucanía  '), ('X', 'Región de Los Lagos '), ('XI', 'Región Aysén del General Carlos Ibáñez del Campo '), ('XII', 'Región de Magallanes y Antártica Chilena   '), ('XIII', 'Región Metropolitana de Santiago    '), ('XIV', 'Región de Los Ríos '), ('XV', 'Región de Arica y Parinacota   '), ('XVI', 'Región de Ñuble ')], default='XIII', max_length=50, verbose_name='Region')),
                ('descripcion', models.TextField(blank=True)),
                ('img', models.ImageField(upload_to='torneo/')),
                ('fecha', models.DateField()),
                ('cupos', models.IntegerField(default=100)),
                ('inscritos', models.IntegerField(default=0)),
                ('activo', models.BooleanField(default=True)),
                ('proximo', models.BooleanField(default=False)),
                ('abierto', models.BooleanField(default=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='titulo')),
            ],
            options={
                'verbose_name': 'Torneo',
                'verbose_name_plural': 'Torneos',
                'ordering': ['-fecha'],
            },
        ),
    ]