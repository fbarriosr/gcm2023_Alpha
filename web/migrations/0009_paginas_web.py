# Generated by Django 3.1.7 on 2024-04-10 16:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20240410_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paginas_Web',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='Paginas_Web/')),
                ('titulo', models.CharField(blank=True, max_length=200, null=True)),
                ('contenido', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, max_length=254, upload_to='Paginas_Web/files/')),
            ],
            options={
                'verbose_name': 'Paginas_Web',
                'verbose_name_plural': 'Paginas_Webs',
                'ordering': ['titulo'],
            },
        ),
    ]
