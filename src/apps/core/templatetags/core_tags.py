# -*- coding: utf-8 -*-

from logging import getLogger
import re

from django import template
from django.template.defaultfilters import safe, stringfilter
from django.utils.numberformat import format
from ..util.youtube import YoutubeVideo

log = getLogger('django')


register = template.Library()


@register.filter
@stringfilter
def br(text):
    '''
        Convierte dos barras inclinadas en un salto de línea
    '''
    try:
        text = text.replace('//', '<br>')
    except:
        text = text

    return safe(text)


@register.filter
@stringfilter
def strong(text):
    '''
        Convierte dos barras inclinadas en un salto de línea
    '''

    text = text.replace('//', '<strong>')
    return safe(text)


@register.filter
def floatdot(value, decimal_pos=7):
    '''
        Similar a floatformat, pero utiliza punto en vez de la coma
    '''
    value = str(value).replace(',', '.')
    return format(value, ".", decimal_pos)

floatdot.is_safe = True


@register.filter
@stringfilter
def format_thousands(val):
    '''
    Format a number so that it's thousands are separated by commas.

    1000000 > '1,000,000'
    10000 > '10,000'
    1000.00 > '10,000.00'
    '''
    return ','.join(re.findall('((?:\d+\.)?\d{1,3})', val[::-1]))[::-1]
format_thousands.is_safe = True


@register.filter
def floatcomma(value, decimal_pos=0):
    '''
        Similar a floatformat, pero utiliza punto en vez de la coma
    '''
    value = str(value).replace('.', ',')
    return format(value, ",", decimal_pos)

floatdot.is_safe = True


@register.filter
def get_range(value):
    '''
        Idéntico a xrange
    '''

    return xrange(value)


@register.filter
def get_item(dictionary, key):
    '''
        Obtiene un item del diccionario por nombre de atributo
    '''

    return dictionary.get(key, '')


@register.filter
def split(string, char='//'):
    '''
        Idéntico a split
    '''

    return string.split(char)


@register.filter
def tel(txt):
    ''' Extrae los caracteres númericos de un teléfono '''
    lista = re.findall('\d+', txt)
    telefono = ''.join(lista)
    return telefono


@register.filter
@stringfilter
def youtube_embed(url):
    '''
        Genera la url para incrustar videos de Youtube en base a la url normal.
    '''
    yv = YoutubeVideo(url)
    return yv.embed_url


@register.filter
@stringfilter
def youtube_id(url):
    '''
        Genera la url para incrustar videos de Youtube en base a la url normal.
    '''
    yv = YoutubeVideo(url)
    return yv.id


@register.filter
@stringfilter
def youtube_img(url, size):
    '''
        Genera la url de la iamgen miniatura de un video en youtube en base a
        la url normal y su tamaño.
    '''
    yv = YoutubeVideo(url)
    return yv.get_img(size)


@register.filter
@stringfilter
def br2(text):
    '''
        Convierte dos barras inclinadas en un salto de línea
    '''

    text = text.replace('//', '<br><i>')
    return safe(text)


@register.filter
@stringfilter
def format_fecha(text):
    '''  Da a la fechas tipo  10/02/2014 el siguiente formato  10.02.2014 '''
    text = text.replace('/', '.')
    return safe(text)


@register.filter
@stringfilter
def nobr(text):
    '''
        Convierte dos barras inclinadas en un salto de línea
    '''

    text = text.replace('//', '')
    return safe(text)


@register.filter
@stringfilter
def strong2(text):
    '''
        Convierte dos barras inclinadas en negrita
    '''
    try:
        texto = text.split('//')
        texto1 = texto[0] + '<strong>' + texto[1] + '</strong>'
        text = texto1
    except:
        text = text
    return safe(text)


@register.filter
@stringfilter
def span_(text):
    '''
        Convierte dos barras inclinadas en span
    '''
    try:
        texto = text.split('//')
        texto1 = texto[0] + '<span>' + texto[1] + '</span>'
        text = texto1
    except:
        text = text
    return safe(text)


@register.filter
@stringfilter
def strip_(text):
    '''
        Convierte dos barras inclinadas en span
    '''
    try:
        texto = text.split('//')
        texto1 = texto[0] + texto[1]
        text = texto1
    except:
        text = text
    return safe(text)


@register.filter
@stringfilter
def br_guion(text):
    '''
        Convierte dos barras inclinadas en un salto de línea
    '''
    try:
        text = text.replace('//', '-')
    except:
        text = text

    return safe(text)


@register.filter
@stringfilter
def span_2(text):
    '''
        Convierte dos barras inclinadas en span
    '''
    try:
        texto = text.split('//')
        texto1 = '<span>' + texto[0] + '</span>' + texto[1]
        text = texto1
    except:
        text = '<span>' + text + '</span>'
    return safe(text)
