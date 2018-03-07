# -*- coding: utf-8 -*-
from django.db import models
# from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from urllib.parse import urlparse
from django.conf import settings
from apps.core.models import AuditableModel, SlugModel, PositionModel
from ckeditor.fields import RichTextField
from geoposition.fields import GeopositionField
from filebrowser.fields import FileBrowseField
from uuslug import uuslug

# Create your models here.


# HOME
class Home(models.Model):
    titulo_servicios = models.CharField('Título servicios',
                                        max_length=100, blank=True)
    titulo_somos = models.CharField('Título somos', max_length=100,
                                    blank=True)
    texto_somos = RichTextField('Texto somos', blank=True)
    img_somos = FileBrowseField('Imagen', max_length=200,
                                directory='home',
                                extensions=['.jpg', '.png', '.gif'],
                                blank=True,
                                help_text='Tamaño Recomendado: 585x410')
    boton_somos = models.CharField('Título boton somos',
                                   blank=True,
                                   max_length=300)
    titulo_clientes = models.CharField('Título clientes',
                                       blank=True,
                                       max_length=300)
    boton_clientes = models.CharField('Texto boton clientes',
                                      blank=True,
                                      max_length=300)

    class Meta:
        verbose_name = u'Home'
        verbose_name_plural = u'Home'

    def __unicode__(self):
        return u'Home'

    # def get_clientes(self):
    #     try:
    #         listado = self.clientes.order_by('position')
    #     except:
    #         listado = []
    #     return listado


class SeccionCliente(models.Model):
    texto = RichTextField('Texto', blank=True)
    boton = models.CharField('Texto botón', max_length=100,
                             blank=True)
    enlace = models.CharField('Enlace boton', max_length=300,
                              blank=True)

    class Meta:
        verbose_name = u'Sección clientes'
        verbose_name_plural = u'Sección clientes'

    def __unicode__(self):
        return u'Sección clientes'


class Cliente(PositionModel, SlugModel):
    # nombre = models.CharField('Nombre', max_length=200, blank=True)
    imagen = FileBrowseField('Imagen', max_length=200,
                             directory='cliente',
                             extensions=['.jpg', '.png', '.gif'],
                             blank=True,
                             help_text='Tamaño Recomendado: 172x125')
    texto_hover = models.CharField('Texto hover', max_length=100, blank=True,
                                   default='MIRA LO QUE HICIMOS')
    ubicacion = models.CharField('Ubicación', blank=True, max_length=300)
    titulo = models.CharField('Título', blank=True, max_length=200)
    subtitulo = models.CharField('Subtítulo', blank=True, max_length=200)

    class Meta:
        verbose_name = u'Cliente'
        verbose_name_plural = u'Clientes'

    def __unicode__(self):
        return u'cliente'

    def get_absolute_url(self):
        return reverse('web:cliente_detalle',
                       kwargs={'slug': self.slug})


class HomeBanner(PositionModel):
    texto = models.CharField("Texto", max_length=100, blank=True)
    texto_boton = models.CharField("Texto de botón", null=True,
                                   blank=True, max_length=100)
    enlace_boton = models.CharField('Enlace del botón', blank=True,
                                    max_length=100)
    imagen = FileBrowseField('Imagen:', max_length=200,
                             directory='home_banners',
                             extensions=['.jpg', '.png', '.gif'],
                             help_text='Tamaño Recomendado: 1920x570')

    class Meta:
        verbose_name = u'Banner de Home'
        verbose_name_plural = u'Banners de Home'
        ordering = ['position']

    def __unicode__(self):
        return unicode(self.position)


class Testimonio(PositionModel):
    titulo = models.CharField('Título', max_length=200, blank=True)
    texto = RichTextField('Texto', blank=True)
    autor = models.CharField('Autor', max_length=100, blank=True)
    imagen = FileBrowseField('Imagen:', max_length=200,
                             directory='testimonios',
                             extensions=['.jpg', '.png', '.gif'],
                             help_text='Tamaño Recomendado: 128x128')
    active = models.BooleanField('Mostrar', default=True)

    class Meta:
        verbose_name = u'Testimonio'
        verbose_name_plural = u'Testimonios'
        ordering = ['position']

    def __unicode__(self):
        return self.autor


class Banners(models.Model):
    CHOICES = (
        ('SO', u'SOMOS'),
        ('CLI', u'CLIENTES'),
        ('TES', u'TESTIMONIOS'),
        ('CO', u'CONTACTO'),
        ('SE', u'SERVICIOS'),
    )
    pestana = models.CharField("Pestaña",
                               max_length=30, choices=CHOICES, default='SO')
    titulo = models.CharField("Título", max_length=200)
    fondo = FileBrowseField('Fondo:', max_length=200,
                            directory='banners_img',
                            extensions=['.jpg', '.png', '.gif'],
                            help_text='Tamaño Recomendado: 1080x132',
                            blank=True)

    class Meta:
        verbose_name = u'Banners'
        verbose_name_plural = u'Banners'
        # ordering = ['position']

    def __unicode__(self):
        return self.titulo


class InfoSite(AuditableModel):
    email_form = models.CharField('Email de Formulario de Contacto',
                                  blank=True,
                                  help_text='Separar correos con comas',
                                  max_length=200)
    twitter = models.URLField('Twitter', blank=True)
    facebook = models.URLField('Facebook', blank=True)
    site = models.CharField("URL del sitio", max_length=60, blank=True,
                            help_text='Ingrese la url actual del sitio sin el slash final')
    ga = models.CharField('Google Analytics', max_length=24, blank=True,
       help_text='''Opcional: Inserte el código que google analitycs le
       proporciona con el formato: UA-XXXXX-X''')

    def __unicode__(self):
        return u'Información del Sitio'

    class Meta:
        verbose_name_plural = u'Información del Sitio'

    # def save(self, *args, **kwargs):
    #     site = Site.objects.get(id=settings.SITE_ID)
    #     site.domain = urlparse(self.site).netloc
    #     site.name = settings.PROJECT_NAME
    #     site.save()
    #     super(InfoSite, self).save(*args, **kwargs)


class Telefono(PositionModel):
    info = models.ForeignKey(InfoSite, related_name='info_tel')
    telefono = models.CharField('Teléfono', max_length=120, blank=True)

    class Meta:
        verbose_name = u'Teléfono'
        verbose_name_plural = u'Teléfonos'

    def __unicode__(self):
        return self.telefono

    def tele(self):
        if '/' in self.telefono:
            telef = self.telefono.split(' / ')
        else:
            telef = [self.telefono, ]

        return telef


class Email(PositionModel):
    info = models.ForeignKey(InfoSite, related_name='info_email')
    email = models.CharField('Email', max_length=120)

    class Meta:
        verbose_name = u'Email'
        verbose_name_plural = u'Emails'

    def __unicode__(self):
        return self.email


class Direccion(PositionModel):
    info = models.ForeignKey(InfoSite, related_name='info_direccion')
    direccion = models.CharField('Email', max_length=300)

    class Meta:
        verbose_name = u'ubicacion'
        verbose_name_plural = u'ubicaciones'

    def __unicode__(self):
        return self.direccion


class Contacto(models.Model):
    nombre = models.CharField('Nombres', max_length=200, blank=True)
    apellido = models.CharField('Apellidos', max_length=200, blank=True)
    email = models.EmailField('Email', blank=True)
    telefono = models.CharField('Teléfono', max_length=20, blank=True)
    # mensaje = RichTextField("Mensaje")
    fecha = models.DateField('Fecha', auto_now_add=True)
    servicio = models.CharField('Tipo de servicio', max_length=200, blank=True)

    class Meta:
        verbose_name = u'Contacto'
        verbose_name_plural = u'Contactos'

    def __unicode__(self):
        return self.nombre


class SeccionContacto(models.Model):
    titulo = models.CharField('Título', blank=True, max_length=200)
    texto = RichTextField('Texto', blank=True)
    imagen = FileBrowseField("imagen",
                             max_length=200,
                             directory='contacto',
                             extensions=['.jpg', '.png', '.gif'],
                             help_text=u'Tamaño recomendado:160x45',
                             blank=True)

    class Meta:
        verbose_name = u'Sección Contacto'
        verbose_name_plural = u'Sección Contacto'

    def __unicode__(self):
        return self.titulo


class SeccionServicios(models.Model):
    texto = RichTextField('Texto', blank=True)
    boton = models.CharField('Texto botón', max_length=100,
                             blank=True)
    enlace = models.CharField('Enlace boton', max_length=300,
                              blank=True)

    class Meta:
        verbose_name = u'Sección servicios'
        verbose_name_plural = u'Sección servicios'

    def __unicode__(self):
        return u'Sección servicios'


class Servicio(PositionModel, AuditableModel, SlugModel):
    servicio = models.ManyToManyField('self', related_name='servicios',
                                      blank=True)
    # nombre = models.CharField('Nombre', max_length=120, blank=True)
    texto = RichTextField('Texto', blank=True)
    imagen = FileBrowseField("Imagen", max_length=200,
                             directory='servicios',
                             extensions=['.jpg', '.png', '.gif'],
                             help_text='Tamaño Recomendado: 767x460',
                             blank=True)
    icono = FileBrowseField("Imagen ícono", max_length=200,
                            directory='servicios_icono',
                            extensions=['.jpg', '.png', '.gif'],
                            help_text='Tamaño Recomendado: 51x51',
                            blank=True)
    icono2 = FileBrowseField("Imagen ícono hover", max_length=200,
                             directory='servicios_icono2',
                             extensions=['.jpg', '.png', '.gif'],
                             help_text='Tamaño Recomendado: 70x70',
                             blank=True)

    class Meta:
        verbose_name = u'Servicio'
        verbose_name_plural = u'Servicios'
        ordering = ['position', ]

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('web:servicio_detalle',
                       kwargs={'slug': self.slug})


class Somos(models.Model):
    introduccion = RichTextField('Introduccion', blank=True)
    texto = RichTextField('Texto', blank=True)
    imagen = FileBrowseField("imagen",
                             max_length=200,
                             directory='somos',
                             extensions=['.jpg', '.png', '.gif'],
                             help_text=u'Tamaño recomendado:470x430',
                             blank=True)
    boton = models.CharField('Texto botón', max_length=100, blank=True)
    enlace = models.CharField('Enlace botón', max_length=200, blank=True)
    texto_redes = models.CharField('Texto redes sociales', blank=True,
                                   max_length=200)

    class Meta:
        verbose_name = u'Somos'
        verbose_name_plural = u'Somos'

    def __unicode__(self):
        return u'Somos'
