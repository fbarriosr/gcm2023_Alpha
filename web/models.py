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
import os
from django.utils.text import slugify

def clean_filename(filename):
    """
    Limpia el nombre del archivo eliminando caracteres no permitidos.
    """
    # Separar el nombre del archivo de su extensión
    name, ext = os.path.splitext(filename)
    # Convertir el nombre a una forma válida
    name = slugify(name)
    # Recombinar el nombre limpio con su extensión original
    return f"{name}{ext}"

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
        # Verificar si el objeto ya existe (es una actualización)
        if self.pk and Galeria.objects.filter(pk=self.pk).exists():
            existing = Galeria.objects.get(pk=self.pk)

            # Solo sobrescribir `img` si no se ha proporcionado un nuevo archivo
            if not self.img:
                self.img = existing.img
            else:
                # Limpiar el nombre solo si el archivo es nuevo
                if self.img != existing.img:
                    self.img.name = clean_filename(self.img.name)
        else:
            # Si es un nuevo objeto, limpiar el nombre del archivo si existe
            if self.img:
                self.img.name = clean_filename(self.img.name)

        # Llamar al método save original
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
        # Verificar si el objeto ya existe (es una actualización)
        if self.pk and Links.objects.filter(pk=self.pk).exists():
            existing = Links.objects.get(pk=self.pk)

            # Solo sobrescribir `img` si no se ha proporcionado un nuevo archivo
            if not self.img:
                self.img = existing.img
            else:
                # Limpiar el nombre solo si el archivo es nuevo
                if self.img != existing.img:
                    self.img.name = clean_filename(self.img.name)
        else:
            # Si es un nuevo objeto, limpiar el nombre del archivo si existe
            if self.img:
                self.img.name = clean_filename(self.img.name)

        # Llamar al método save original
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
        # Verificar si el objeto ya existe (es una actualización)
        if self.pk and Paginas_Web.objects.filter(pk=self.pk).exists():
            existing = Paginas_Web.objects.get(pk=self.pk)

            # Solo sobrescribir `img` si no se ha proporcionado un nuevo archivo
            if not self.img:
                self.img = existing.img
            else:
                # Limpiar el nombre solo si el archivo es nuevo
                if self.img != existing.img:
                    self.img.name = clean_filename(self.img.name)

            # Solo sobrescribir `file` si no se ha proporcionado un nuevo archivo
            if not self.file:
                self.file = existing.file
            else:
                # Limpiar el nombre solo si el archivo es nuevo
                if self.file != existing.file:
                    self.file.name = clean_filename(self.file.name)
        else:
            # Si es un nuevo objeto, limpiar el nombre de archivo si existen
            if self.img:
                self.img.name = clean_filename(self.img.name)
            if self.file:
                self.file.name = clean_filename(self.file.name)

        # Llamar al método save original
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

    def save(self, *args, **kwargs):
        # Verificar si el objeto ya existe (es una actualización)
        if self.pk and Listado.objects.filter(pk=self.pk).exists():
            existing = Listado.objects.get(pk=self.pk)

            # Solo sobrescribir `img` si no se ha proporcionado un nuevo archivo
            if not self.img:
                self.img = existing.img
            else:
                # Limpiar el nombre solo si el archivo es nuevo
                if self.img != existing.img:
                    self.img.name = clean_filename(self.img.name)
        else:
            # Si es un nuevo objeto, limpiar el nombre del archivo si existe
            if self.img:
                self.img.name = clean_filename(self.img.name)

        # Llamar al método save original
        super(Listado, self).save(*args, **kwargs)




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
    def save(self, *args, **kwargs):
        # Verificar si el objeto ya existe (es una actualización)
        if self.pk and Card.objects.filter(pk=self.pk).exists():
            existing = Card.objects.get(pk=self.pk)

            # Solo sobrescribir `img` si no se ha proporcionado un nuevo archivo
            if not self.img:
                self.img = existing.img
            else:
                # Limpiar el nombre solo si el archivo es nuevo
                if self.img != existing.img:
                    self.img.name = clean_filename(self.img.name)
        else:
            # Si es un nuevo objeto, limpiar el nombre del archivo si existe
            if self.img:
                self.img.name = clean_filename(self.img.name)

        # Llamar al método save original
        super(Card, self).save(*args, **kwargs)



class CardsAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields = ["titulo"]
    list_display = ("titulo", "order", 'foto')
    list_per_page = 10  # No of records per page

    def foto(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="120px" />', obj.img.url)
        else:
            return "No se pudo previsualizar, no hay imagen"



