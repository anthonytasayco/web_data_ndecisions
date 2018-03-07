# -*- coding: utf-8 -*-
# Stdlib imports

# Core django imports
from django.conf import settings
from django.contrib import admin
# Third party app imports
from singlemodeladmin import SingleModelAdmin
from filebrowser.settings import ADMIN_THUMBNAIL
from apps.core.actions import export_as_csv_action
from .models import (Home, SeccionCliente, SeccionServicios,
                     Cliente, HomeBanner, Testimonio,
                     Banners, InfoSite, Telefono, Email,
                     Direccion, Contacto, SeccionContacto,
                     Servicio, Somos)


@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    model = Banners
    list_display = ['titulo', 'miniatura', 'pestana']

    def miniatura(self, obj):
        if obj.fondo and obj.fondo.filetype == "Image":
            return u'<img src="%s" />' % obj.fondo.version_generate(
                ADMIN_THUMBNAIL).url
        else:
            return ""

    miniatura.allow_tags = True
    miniatura.short_description = u"Imagen"


@admin.register(HomeBanner)
class BannerHomeAdmin(admin.ModelAdmin):
    model = HomeBanner
    list_display = ['miniatura', 'position']
    ordering = ['position']
    list_editable = ['position']

    def miniatura(self, obj):
        if obj.imagen and obj.imagen.filetype == "Image":
            return u'<img src="%s" />' % obj.imagen.version_generate(
                ADMIN_THUMBNAIL).url
        else:
            return ""

    miniatura.allow_tags = True
    miniatura.short_description = u"Imagen"


@admin.register(Testimonio)
class TestimonioAdmin(admin.ModelAdmin):
    list_display = ['autor', 'miniatura', 'position']
    ordering = ['position']
    list_editable = ['position']

    def miniatura(self, obj):
        if obj.imagen and obj.imagen.filetype == "Image":
            return u'<img src="%s" />' % obj.imagen.version_generate(
                ADMIN_THUMBNAIL).url
        else:
            return ""

    miniatura.allow_tags = True
    miniatura.short_description = u"Imagen"


@admin.register(Home)
class HomeAdmin(SingleModelAdmin):
    pass


@admin.register(Somos)
class SomosAdmin(SingleModelAdmin):
    pass


@admin.register(SeccionContacto)
class SeccionContactoAdmin(SingleModelAdmin):
    pass


class EmailInline(admin.StackedInline):
    model = Email
    extra = 0


class TelefonoInline(admin.StackedInline):
    model = Telefono
    extra = 0


class DireccionInline(admin.StackedInline):
    model = Direccion
    extra = 0


@admin.register(InfoSite)
class InfoSiteAdmin(SingleModelAdmin):
    fieldsets = (
        ('Información de contacto', {'fields': ('email_form', )}),
        ('Social', {'fields': ('twitter', 'facebook')}),
        ('Información del sitio', {'fields': ('site', 'ga')}),
    )
    inlines = [EmailInline, TelefonoInline, DireccionInline]

    def has_add_permission(self, request):
        info = InfoSite.objects.all()
        if info:
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    ordering = ['-fecha']
    list_display = ['nombre', 'apellido', 'telefono', 'email', 'fecha']
    search_fields = ('nombre', 'apellido', 'email', 'fecha')
    list_per_page = 25
    actions = [export_as_csv_action()]


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'miniatura', 'position', 'active']
    ordering = ['position']
    list_editable = ['position', 'active']

    def miniatura(self, obj):
        if obj.imagen and obj.imagen.filetype == "Image":
            return u'<img src="%s" />' % obj.imagen.version_generate(
                ADMIN_THUMBNAIL).url
        else:
            return ""

    miniatura.allow_tags = True
    miniatura.short_description = u"Imagen"


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'miniatura', 'position']
    ordering = ['position']
    list_editable = ['position']

    def miniatura(self, obj):
        if obj.imagen and obj.imagen.filetype == "Image":
            return u'<img src="%s" />' % obj.imagen.version_generate(
                ADMIN_THUMBNAIL).url
        else:
            return ""

    miniatura.allow_tags = True
    miniatura.short_description = u"Imagen"


@admin.register(SeccionCliente)
class SeccionClienteAdmin(SingleModelAdmin):
    pass


@admin.register(SeccionServicios)
class SeccionServiciosAdmin(SingleModelAdmin):
    pass
