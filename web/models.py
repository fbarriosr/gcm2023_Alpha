# from django.db import models

# Create your models here.

from django.db import models
from django.contrib import admin
from search_admin_autocomplete.admin import SearchAutoCompleteAdmin
from admin_auto_filters.filters import AutocompleteFilter
from autoslug import AutoSlugField
from django.utils import timezone
import uuid
from usuarios.models import Usuario
from .choices import *
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html


# Create your models here.
class UsuarioFilter(AutocompleteFilter):
    title = 'Usuario' # display title
    field_name = 'usuario' # name of the foreign key field

# PLANTILLA PARA A GALERIA EN HOME
class Galeria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=200, blank=False, null=False)
    img = models.ImageField(upload_to="galeria/")
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galerias"
        ordering = ["order"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Utilizar la función global para limpiar los nombres de archivos
        if self.img:
            self.img.name = clean_filename(self.img.name)
        super(Galeria, self).save(*args, **kwargs)



class GaleriaAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields = ["titulo"]
    list_display = ("titulo", "order", 'foto')
    list_per_page = 10  # No of records per page
    def foto(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="120px" />', obj.img.url)
        else:
            return "No se pudo previsualizar, no hay imagen"

# PLANTILLA PARA LOS LINKS EN HOME
class Links(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=200, blank=False, null=False)
    parrafo = models.TextField()
    img = models.ImageField(upload_to="links/")
    tipo = models.CharField(max_length=20, choices=tipo_link, default="NA")  
    url = models.CharField(max_length=500, blank=False, default='#')
    order = models.IntegerField(default=0)
    banner = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
        ordering = ["-banner","tipo","order"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Utilizar la función global para limpiar los nombres de archivos
        if self.img:
            self.img.name = clean_filename(self.img.name)
        super(Links, self).save(*args, **kwargs)

class LinksAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields = ["titulo"]
    list_display = ("titulo","banner",'tipo', "order",'foto')
    list_per_page = 10  # No of records per page
    def foto(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="120px" />', obj.img.url)
        else:
            return "No se pudo previsualizar, no hay imagen"

# CONTENIDO PRINCIPAL DE HISTORIA, ETC

class Paginas_Web(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=20, choices= webs, default="H") 
    img = models.ImageField(upload_to="Paginas_Web/")
    titulo = models.CharField(max_length=200, blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="Paginas_Web/files/", max_length=254, blank=True)
    tituloPestana = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Paginas_Web"
        verbose_name_plural = "Paginas_Webs"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo
    def save(self, *args, **kwargs):
        # Utilizar la función global para limpiar los nombres de archivos
        if self.img:
            self.img.name = clean_filename(self.img.name)
        super(Paginas_Web, self).save(*args, **kwargs)


class Paginas_WebAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields = ["titulo"]
    list_display = ("tipo",'titulo', 'foto')
    list_per_page = 10
    def foto(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="120px" />', obj.img.url)
        else:
            return "No se pudo previsualizar, no hay imagen"


# CLASIFICA A QUE PERTENECEN LAS LISTAS DE IMAGENES DEL MODELO 'LISTA'
class Tipo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="Tipo"
    )
    descripcion = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ["order"]

    def __str__(self):
        return str(self.tipo)


class TiposAdmin(ImportExportModelAdmin,SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields = ["tipo"]
    list_display = ("tipo", "order")
    list_per_page = 10


# ADMINISTRA EL LISTADO DE IMAGENES DE PRESIDENTES, COMITE, ETC...
class Listado (models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo            = models.ForeignKey(Tipo, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Tipo')
    titulo          = models.CharField(max_length=200, blank= False, null = False)
    grupo            = models.CharField(max_length=20, choices=grupo, default="M") 
    img             = models.ImageField(upload_to='listado/')
    order           = models.IntegerField(default=0)
    actual          = models.BooleanField(default= False)


    class Meta:
        verbose_name = "Listado"
        verbose_name_plural = "Listados"
        ordering = ["grupo", "tipo"]

    def __str__(self):
        return self.titulo



class ListadosAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):

    search_fields   = ['titulo']
    list_display    =('titulo', 'grupo', 'tipo', 'actual', 'foto')
    list_per_page   = 10 # No of records per page
    def foto(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="120px" />', obj.img.url)
        else:
            return "No se pudo previsualizar, no hay imagen"


# ADMINISTRA LOS CARDS DE TORNEO
class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="Titulo"
    )
    direccion = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="Direccion"
    )
    comuna = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="Comuna"
    )
    region = models.CharField(
        max_length=50, blank=False, null=False, verbose_name="Region"
    )
    descripcion = models.TextField()
    img = models.ImageField(upload_to="cards/")
    fecha = models.DateField()
    cupos = models.IntegerField()
    inscritos = models.IntegerField(default=0)
    activo = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"
        ordering = ["order"]

    def __str__(self):
        return self.titulo


class CardsAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields = ["titulo"]
    list_display = ("titulo", "order", 'foto')
    list_per_page = 10  # No of records per page

    def foto(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="120px" />', obj.img.url)
        else:
            return "No se pudo previsualizar, no hay imagen"



