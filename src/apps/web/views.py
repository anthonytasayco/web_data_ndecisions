# -*- coding: utf-8 -*-
from logging import getLogger
from django.shortcuts import render, get_object_or_404, redirect
# external apps
# local apps
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .models import (Home, HomeBanner, Somos, Testimonio,
                     Banners, Cliente,
                     SeccionCliente, Servicio, SeccionServicios,
                     SeccionContacto)
from .forms import ContactoForm
from django.views.decorators.csrf import ensure_csrf_cookie
from .util import get_info
log = getLogger('django')


def home(request):
    meta_title = u"Ingeres"
    log.info('VIEW: HOME')
    info = get_info()
    home, created = Home.objects.get_or_create(pk=1)
    banners = HomeBanner.objects.order_by('position')
    clientes = Cliente.objects.order_by('position')

    return render(request, 'web/home.html', locals())


def somos(request):
    meta_title = u"Somos | Ingeres"
    log.info('VIEW: Somos')
    info = get_info()
    somos, created = Somos.objects.get_or_create(pk=1)
    tab = "SO"
    banner, created = Banners.objects.get_or_create(pestana='SO')

    return render(request, 'web/somos.html', locals())


def gracias(request):
    meta_title = u"Gracias | Ingeres"
    log.info('VIEW:GRACIAS')
    info = get_info()

    return render(request, 'web/gracias.html', locals())


def page_404(request):
    meta_title = u"Error 404 | Ingeres"
    ruta = request.path
    log.error(u'Error 404: {0}'.format(ruta))
    info = get_info()
    response = render(request, 'web/error.html', locals())
    response.status_code = 404

    return response


def page_500(request):
    meta_title = u"Error 500 | Ingeres"
    ruta = request.path
    log.error(u'Error 500: {0}'.format(ruta))
    info = get_info()
    response = render(request, 'web/error.html', locals())
    response.status_code = 500

    return response


def contacto(request):
    meta_title = u"Contacto | Ingeres"
    log.info('VIEW:Contacto')
    info = get_info()
    tab = "CO"
    banner, created = Banners.objects.get_or_create(pestana='CO')
    servicios = Servicio.objects.order_by('position')
    seccion, created = SeccionContacto.objects.get_or_create(pk=1)
    form = ContactoForm()

    if request.method == 'POST':
        print(request.POST, '<::: POST')
        form = ContactoForm(request.POST)
        if form.is_valid():
            print("Soy valido")
            form.save()
            if info.email_form:
                form.enviaEmail()
            return redirect('web:gracias')
        else:
            print(form.errors, ":::: ERRORS")
            log.error("Error al enviar el formulario")
    else:
        form = ContactoForm()

    return render(request, 'web/contacto.html', locals())


def clientes(request):
    meta_title = u"Clientes | Ingeres"
    log.info('VIEW: Clientes')
    info = get_info()
    seccion, created = SeccionCliente.objects.get_or_create(pk=1)
    clientes = Cliente.objects.order_by('position')
    tab = "CLI"
    banner, created = Banners.objects.get_or_create(pestana='CLI')

    # Paginador

    cantidad = len(clientes)
    clientes_POR_PAGINA = 12
    paginator = Paginator(clientes, clientes_POR_PAGINA)
    page = request.GET.get('p', 1)
    total = paginator.num_pages

    pag = int(page)
    sig = 0
    ant = 0
    if pag < int(total):
        sig = pag + 1
    if pag > 1:
        ant = pag - 1
    try:
        clientes = paginator.page(pag)
    except PageNotAnInteger:
        clientes = paginator.page(1)
    except EmptyPage:
        clientes = paginator.page(paginator.num_pages)

    return render(request, 'web/clientes.html', locals())


def cliente_detalle(request, slug=None):
    cliente = get_object_or_404(Cliente, slug=slug)
    meta_title = str(cliente.nombre) + '| Clientes | Ingeres'
    tab = "CLI"
    banner, created = Banners.objects.get_or_create(pestana='CLI')
    relacionados = Cliente.objects.order_by('?').exclude(slug=slug)[:4]

    return render(request, 'web/clientes-detalle.html', locals())


def testimonios(request):
    meta_title = u"Testimonios | Ingeres"
    log.info('VIEW: Testimonios')
    info = get_info()
    testimonios = Testimonio.objects.order_by('position')
    tab = "TES"
    banner, created = Banners.objects.get_or_create(pestana='TES')

    # Paginador

    cantidad = len(testimonios)
    testimonios_POR_PAGINA = 4
    paginator = Paginator(testimonios, testimonios_POR_PAGINA)
    page = request.GET.get('p', 1)
    total = paginator.num_pages

    pag = int(page)
    sig = 0
    ant = 0
    if pag < int(total):
        sig = pag + 1
    if pag > 1:
        ant = pag - 1
    try:
        testimonios = paginator.page(pag)
    except PageNotAnInteger:
        testimonios = paginator.page(1)
    except EmptyPage:
        testimonios = paginator.page(paginator.num_pages)

    return render(request, 'web/testimonio.html', locals())


def servicios(request):
    meta_title = u"Servicios | Ingeres"
    log.info('VIEW: Servicios')
    info = get_info()
    seccion, created = SeccionServicios.objects.get_or_create(pk=1)
    servicios = Servicio.objects.order_by('position').filter(active=True)
    tab = "SE"
    banner, created = Banners.objects.get_or_create(pestana='SE')

    return render(request, 'web/servicios-listado.html', locals())


def servicio_detalle(request, slug=None):
    servicio = get_object_or_404(Servicio, slug=slug)
    meta_title = str(servicio.nombre) + '| Servicios | Ingeres'
    tab = "SE"
    banner, created = Banners.objects.get_or_create(pestana='SE')
    servicio = Servicio.objects.get(slug=slug)
    relacionados = servicio.servicio.all()[:4]

    return render(request, 'web/servicios-detalle.html', locals())
