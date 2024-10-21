import uuid
from django.db import models
from django.contrib import admin
from search_admin_autocomplete.admin import SearchAutoCompleteAdmin
from admin_auto_filters.filters import AutocompleteFilter
from autoslug import AutoSlugField
from django.utils import timezone
from usuarios.models import Usuario
from .choices import *
from usuarios.choices import *
from import_export.admin import ImportExportModelAdmin
from djmoney.models.fields import MoneyField
from django.utils.html import format_html
from .utils import clean_filename

def slugify_two_fields(self):
        return "{}_{}-{}-{}".format(self.titulo, self.fecha.day, self.fecha.month, self.fecha.year)

# CONTENIDO PRINCIPAL DE HISTORIA, ETC

class Parametro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=20, default="A")
    valor = models.CharField(max_length=200, blank=True, null=True)
   
    class Meta:
        verbose_name = "Parametro"
        verbose_name_plural = "Parametros"
        ordering = ["tipo"]

    def __str__(self):
        return self.tipo


class ParametroAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields = ["tipo"]
    list_display = ("tipo",'valor')
    list_per_page = 10


class CardsInicio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=20, choices= cards, default="A")
    img = models.ImageField(upload_to="CardsInicio/")
    titulo = models.CharField(max_length=200, blank=True, null=True)
   
    class Meta:
        verbose_name = "CardInicio"
        verbose_name_plural = "CardsInicio"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Utilizar la función global para limpiar los nombres de archivos
        if self.img:
            self.img.name = clean_filename(self.img.name)
        super(CardsInicio, self).save(*args, **kwargs)


class CardsInicioAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields = ["titulo"]
    list_display = ("tipo",'titulo', 'foto')
    list_per_page = 10


    def foto(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="120px" />', obj.img.url)
        else:
            return "No se pudo previsualizar, no hay imagen"

class Paginas_Socio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=20, choices= websSocio, default="B")
    img = models.ImageField(upload_to="Paginas_Socio/")
    titulo = models.CharField(max_length=200, blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="Paginas_Socio/files/", max_length=254, blank=True)
    tituloPestana = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Paginas_Socio"
        verbose_name_plural = "Paginas_Socios"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Si el objeto ya existe (es una actualización)
        if self.pk:
            existing = Paginas_Socio.objects.get(pk=self.pk)

            # Solo sobrescribir file si se ha proporcionado un nuevo archivo
            if not self.file:
                self.file = existing.file
            else:
                # Limpiar el nombre solo si el archivo es nuevo
                if self.archivo != existing.archivo:
                    self.archivo.name = clean_filename(self.archivo.name)

            # Solo sobrescribir imagen si se ha proporcionado una nueva imagen
            if not self.img:
                self.img = existing.img
            else:
                # Limpiar el nombre solo si la imagen es nueva
                if self.img != existing.img:
                    self.img.name = clean_filename(self.img.name)

        else:
            # Si es un nuevo objeto, limpiar el nombre de archivo e imagen si existen
            if self.file:
                self.file.name = clean_filename(self.file.name)
            if self.img:
                self.img.name = clean_filename(self.img.name)

        super(Paginas_Socio, self).save(*args, **kwargs)


class Paginas_SocioAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields = ["titulo"]
    list_display = ("tipo",'titulo','foto')
    list_per_page = 10
    def foto(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="120px" />', obj.img.url)
        else:
            return "No se pudo previsualizar, no hay imagen"

class Multimedia (models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo          = models.CharField(max_length = 200, blank = False, null = False)
    fecha           = models.DateField(null=False)
    img             = models.FileField(upload_to='multimedia')
    slug            = AutoSlugField(populate_from=slugify_two_fields,  unique_with=['titulo','fecha'])
    is_active       = models.BooleanField('Activo',default = True)
    class Meta:
        verbose_name = "Multimedia"
        verbose_name_plural = "Multimedias"
        ordering = ["-fecha"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Utilizar la función global para limpiar los nombres de archivos
        if self.img:
            self.img.name = clean_filename(self.img.name)
        super(Multimedia, self).save(*args, **kwargs)

class MultimediaImg(models.Model):
    multimedia = models.ForeignKey(Multimedia, default=None, on_delete=models.CASCADE)
    img  = models.FileField(upload_to = 'multimedia/')
    class Meta:
        verbose_name = "MultimediaImg"
        verbose_name_plural = "MultimediasImg"
        ordering = ["img"]
    def __str__(self):
        return self.multimedia.titulo

    # Función para obtener la URL de la imagen en el admin
    def preview_img(self):
        if self.img and hasattr(self.img, 'url'):
            return format_html('<img src="{}" width="120px" />', self.img.url)
        return "No se pudo previsualizar, no hay imagen"

class MultimediaImgAdmin(admin.StackedInline):
    model = MultimediaImg
    readonly_fields = ['preview_img']
    fields = ['img', 'preview_img']  # Mostrar la imagen y su preview en el admin
    extra = 0  # Para no mostrar formularios adicionales vacíos



class MultimediaAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields = ["titulo"]
    inlines = [MultimediaImgAdmin]
    list_display = ( "fecha", "titulo", 'is_active', 'foto')
    list_per_page = 10  # No of records per page
    list_filter = ('is_active',)
    def foto(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="120px" />', obj.img.url)
        else:
            return "No se pudo previsualizar, no hay imagen"

class Image(models.Model):
    image = models.ImageField(upload_to='noticias/')

class Noticia (models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo          = models.CharField(max_length = 200, blank = False, null = False)
    fecha           = models.DateField()
    direccion       = models.CharField(max_length = 200, blank = True, null = False)
    region          = models.CharField(max_length=50,choices= regiones, default= 'XIII', verbose_name="Region")
    resumen         = models.CharField(max_length = 200, blank = False, null = False)
    info            = models.TextField()
    img             = models.ImageField(upload_to='noticias/',null = False, verbose_name='Imagen Principal')
    slug            = AutoSlugField(populate_from=slugify_two_fields,  unique_with=['titulo','fecha'])
    is_active       = models.BooleanField('Activo',default = True)
    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ["-fecha"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Utilizar la función global para limpiar los nombres de archivos
        if self.img:
            self.img.name = clean_filename(self.img.name)
        super(Noticia, self).save(*args, **kwargs)

class NoticiaImg(models.Model):
    noticia = models.ForeignKey(Noticia, default=None, on_delete=models.CASCADE)
    img  = models.FileField(upload_to = 'noticias/')
    class Meta:
        verbose_name = "NoticiaImg"
        verbose_name_plural = "NoticiasImg"
        ordering = ["img"]
    def __str__(self):
        return self.noticia.titulo
    # Previsualización de la imagen
    def preview_img(self):
        if self.img and hasattr(self.img, 'url'):
            return format_html('<img src="{}" width="120px" />', self.img.url)
        return "No se pudo previsualizar, no hay imagen"


class NoticiaImgAdmin(admin.StackedInline):
    model = NoticiaImg
    readonly_fields = ['preview_img']  # Campo de solo lectura para previsualizar la imagen
    fields = ['img', 'preview_img']  # Mostrar imagen y su preview en el admin
    extra = 0  # No mostrar formularios vacíos adicionales


class NoticiaAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields = ["titulo"]
    inlines = [NoticiaImgAdmin]
    list_display = ( "fecha", "titulo", "resumen", 'is_active', 'foto')
    list_per_page = 10  # No of records per page
    list_filter = ('is_active',)

    def foto(self, obj):
        return format_html( '<img src ={} width="60px" />', obj.img.url  )

# ADMINISTRA LOS CARDS DE TORNEO
class Torneo (models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo          = models.CharField(max_length=200, blank=False, null= False, verbose_name="Titulo")
    fecha           = models.DateField(null=False)
    direccion       = models.CharField(max_length=200, blank=False, null= False, verbose_name="Direccion")
    region          = models.CharField(max_length=50,choices= regiones, default= 'XIII', verbose_name="Region")
    cupos           = models.IntegerField(default=100)
    activo          = models.BooleanField(default=True)
    actual          = models.BooleanField(default=False)
    abierto         = models.BooleanField(default=True)
    slug            = AutoSlugField(populate_from=slugify_two_fields,  unique_with=['titulo','fecha'])
    bases           = models.FileField(upload_to="torneos/bases/", max_length=254, blank=True)
    list_salidas    = models.FileField(upload_to="torneos/salidas/", max_length=254, blank=True, verbose_name="Listado de Salidas")
    resultados      = models.FileField(upload_to="torneos/resultados/", max_length=254, blank=True)
    premiacion      = models.FileField(upload_to="torneos/premiacion/", max_length=254, blank=True)
    galeria         = models.CharField(max_length=300, default='No Disponible', verbose_name="Url Galeria")
    ticket          = models.IntegerField(default=7000, verbose_name='Ticket Campeonato')
    recargo         = models.IntegerField(default=5000, verbose_name='Recargo Socio')
    ticket_inv      = models.IntegerField(default=8000, verbose_name='Recargo Invitado')
    ticket_bus      = models.IntegerField(default=10000, verbose_name='Ticket Bus')
    
    def __str__(self):
        return self.titulo + str(self.fecha)

    class Meta:
        verbose_name    = 'Torneo'
        verbose_name_plural = 'Torneos'
        ordering    = ['-fecha']

    def save(self, *args, **kwargs):
        # Si el objeto ya existe (es una actualización)
        if self.pk:
            existing = Torneo.objects.get(pk=self.pk)

            # Solo sobrescribir bases si se ha proporcionado un nuevo archivo
            if not self.bases:
                self.bases = existing.bases
            else:
                # Limpiar el nombre solo si el archivo es nuevo
                if self.bases != existing.bases:
                    self.bases.name = clean_filename(self.bases.name)

            # Solo sobrescribir list_salidas si se ha proporcionado un nuevo archivo
            if not self.list_salidas:
                self.list_salidas = existing.list_salidas
            else:
                # Limpiar el nombre solo si el archivo es nuevo
                if self.list_salidas != existing.list_salidas:
                    self.list_salidas.name = clean_filename(self.list_salidas.name)

            # Solo sobrescribir resultados si se ha proporcionado un nuevo archivo
            if not self.resultados:
                self.resultados = existing.resultados
            else:
                # Limpiar el nombre solo si el archivo es nuevo
                if self.resultados != existing.resultados:
                    self.resultados.name = clean_filename(self.resultados.name)

            # Solo sobrescribir premiacion si se ha proporcionado un nuevo archivo
            if not self.premiacion:
                self.premiacion = existing.premiacion
            else:
                # Limpiar el nombre solo si el archivo es nuevo
                if self.premiacion != existing.premiacion:
                    self.premiacion.name = clean_filename(self.premiacion.name)
        else:
            # Si es un nuevo objeto, limpiar el nombre de archivo si existen
            if self.bases:
                self.bases.name = clean_filename(self.bases.name)
            if self.list_salidas:
                self.list_salidas.name = clean_filename(self.list_salidas.name)
            if self.resultados:
                self.resultados.name = clean_filename(self.resultados.name)
            if self.premiacion:
                self.premiacion.name = clean_filename(self.premiacion.name)

        super(Torneo, self).save(*args, **kwargs)

class TorneoAdmin (ImportExportModelAdmin,SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields   = ['titulo']
    list_display    = ('id','slug','titulo','fecha','region','activo','abierto','actual','cupos','ticket' )
    list_per_page   = 10 # No of records per page
    list_filter = ('activo','actual','abierto')


class Solicitud (models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario         = models.ForeignKey(Usuario,on_delete=models.CASCADE, null=True, verbose_name="Usuario") 
    torneo          = models.ForeignKey(Torneo,on_delete=models.CASCADE, null=True, verbose_name="Torneo")
    fecha           = models.DateTimeField(null=False)
    busCGM          = models.BooleanField(default=False)
    auto            = models.BooleanField(default=False, verbose_name= "Estacionamiento")
    patente         = models.CharField(max_length=12, blank= True , verbose_name="Patente")
    carro           = models.BooleanField(default=False)
    acompanantes    = models.TextField(blank=True, verbose_name='¿Con quién va?')   
    indice          = models.CharField(max_length=12, blank= True ,default='' , verbose_name="Indice")
    deuda_socio     = models.PositiveIntegerField(default=0, verbose_name="Deuda Socio")
    cancela_deuda_socio  = models.BooleanField(default=False)
    recargo         = models.PositiveIntegerField(default=0, verbose_name="Recargo Socio")
    recargo_invitado = models.PositiveIntegerField(default=0, verbose_name="Recargo Invitado")
    recargo_bus     = models.PositiveIntegerField(default=0, verbose_name="Recargo Bus")
    cuota           = models.PositiveIntegerField(default=0,  verbose_name="Cuota de Campeonato")
    monto           = models.PositiveIntegerField(default=0,  verbose_name="Monto Pagado")
    detalle_cuotas_pagadas = models.TextField(default='[]', verbose_name='Detalle cuotas Pendientes')   
    class Meta:
        verbose_name    = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        ordering    = ['-fecha']
class SolicitudAdmin (SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields   = ['usuario__rut']
    list_display    = ('usuario','torneo','fecha','busCGM','carro','cancela_deuda_socio' ,'monto' )
    list_per_page   = 10 # No of records per page
    list_filter = ('torneo', 'fecha')
    autocomplete_fields = ['usuario','torneo']

# PLANTILLA PARA LOS LINKS DE EL CLUB EN HOME DEL SOCIO
class ElClub(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo  = models.CharField(max_length=200, blank=False, null=False)
    archivo = models.FileField(upload_to="ElClub/", max_length=254, blank=True)
    img     = models.ImageField(upload_to='ElClub/',blank = True)
    order = models.IntegerField(default=0)


    class Meta:
        verbose_name = "ElClub"
        verbose_name_plural = "ElClubs"
        ordering = ["order"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Si el objeto ya existe (es una actualización)
        if self.pk:
            existing = ElClub.objects.get(pk=self.pk)

            # Solo sobrescribir archivo si se ha proporcionado un nuevo archivo
            if not self.archivo:
                self.archivo = existing.archivo
            else:
                # Limpiar el nombre solo si el archivo es nuevo
                if self.archivo != existing.archivo:
                    self.archivo.name = clean_filename(self.archivo.name)

            # Solo sobrescribir imagen si se ha proporcionado una nueva imagen
            if not self.img:
                self.img = existing.img
            else:
                # Limpiar el nombre solo si la imagen es nueva
                if self.img != existing.img:
                    self.img.name = clean_filename(self.img.name)

        else:
            # Si es un nuevo objeto, limpiar el nombre de archivo e imagen si existen
            if self.archivo:
                self.archivo.name = clean_filename(self.archivo.name)
            if self.img:
                self.img.name = clean_filename(self.img.name)

        super(ElClub, self).save(*args, **kwargs)

class ElClubAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields = ["titulo"]
    list_display = ("titulo", "order", 'foto')
    list_per_page = 10  # No of records per page
    def foto(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="120px" />', obj.img.url)
        else:
            return "No se pudo previsualizar, no hay imagen"

# LA ESTRUCTURA DE LAS CUOTAS ANUALES DE LOS SOCIOS DEL CLUB CGM
class CuotaAnual(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    año             = models.PositiveIntegerField(verbose_name="Año cuotas")
    monto_cuota     = models.PositiveIntegerField(default=0)  # monto fijo anual aplicable a cada cuota del mes de dicho año.
    periodo         = models.CharField(max_length=50, verbose_name="Periodo") # ejemplo 2024-2025
    cargo           = models.PositiveIntegerField(blank=True, null=True)  # monto extra por atraso, castigo..
    
    descuento       = models.PositiveIntegerField(blank=True, null=True) # descuento que se podria aplicar a la cuota
    PERIODO_CHOICES         = [(num, mes) for num, mes in mes_num_texto.items()]
    descuento_activo        = models.BooleanField(default=False,verbose_name="activo")
    periodo_des_inicio      = models.IntegerField(choices=PERIODO_CHOICES, default=3)
    periodo_des_fin         = models.IntegerField(choices=PERIODO_CHOICES, default=3)
    order           = models.IntegerField(default=0)

    class Meta:
        verbose_name = "CuotaAnual"
        verbose_name_plural = "CuotasAnuales"
        ordering = ["order"]

    def __str__(self):
        return str(self.año)

class CuotasAnualesAdmin(ImportExportModelAdmin, SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields = ["año"]
    list_display = ("año", "monto_cuota", "periodo", "order")
    list_per_page = 10


# LA ESTRUCTURA DE LAS CUOTAS DE LOS SOCIOS DEL CLUB CGM
class Cuota(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mes                     = models.IntegerField()
    numero_cuota            = models.IntegerField(null=True) 
    año                     = models.ForeignKey(CuotaAnual, blank=True, null=True, on_delete=models.CASCADE)  # monto fijo anual aplicable a cada cuota del mes de dicho año.
    usuario                 = models.ForeignKey(Usuario, blank=False, null=False, on_delete=models.CASCADE, verbose_name="socio club")
    monto_pago              = models.PositiveIntegerField(blank=True, null=True, verbose_name="Monto total a pagar")  # monto_pago = monto_cuota - monto_descuento + monto_cargo
    fecha_pago              = models.DateField(blank=True, null=True, verbose_name="Fecha de pago")
    estado_pago             = models.CharField(max_length=1, choices=estado_cuota, default="P", verbose_name="Estado de la cuota")
    order                   = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Cuota"
        verbose_name_plural = "Cuotas"
        ordering = ['usuario__rut',"año",'numero_cuota']

    def nombre_mes(self):
        return timezone.datetime(self.año.año, self.mes, 1).strftime("%B")

    nombre_mes.short_description = "Mes"

    def valor_cuota_mensual(self):
        return self.año.monto_cuota
    
    # def monto_pago_calculado(self):
    #     monto_descuento = self.descuento.monto_descuento if self.descuento else 0
    #     monto_cargo = self.cargo.monto_cargo if self.cargo else 0
    #     return self.valor_cuota_mensual() - monto_descuento + monto_cargo

    # def save(self, *args, **kwargs):
    #     self.monto_pago = self.monto_pago_calculado()
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.usuario.primer_nombre} - {self.año.año} - Mes {self.mes}"


class CuotasAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    list_display = ('usuario','año' , 'numero_cuota', 'estado_pago')
    autocomplete_fields = ['usuario']
    list_filter = ('estado_pago','año','numero_cuota')
    list_per_page = 12
    search_fields = ["usuario__rut"]
    list_editable = ('estado_pago',)
