# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import (home, somos, gracias,
                     contacto, servicios,
                     servicio_detalle, clientes,
                     cliente_detalle, testimonios)

app_name = 'web'

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^somos/$', somos, name='somos'),
    url(r'^gracias/$', gracias, name='gracias'),
    url(r'^contacto/$', contacto, name='contacto'),
    url(r'^somos/$', somos, name='somos'),
    url(r'^testimonios/$', testimonios, name='testimonios'),
    url(r'^servicios/$', servicios, name='servicios'),
    url(r'^servicio/(?P<slug>[\w-]+)/$', servicio_detalle, name='servicio_detalle'),
    url(r'^clientes/$', clientes, name='clientes'),
    url(r'^cliente/(?P<slug>[\w-]+)/$', cliente_detalle, name='cliente_detalle'),
]
