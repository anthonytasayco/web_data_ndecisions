# -*- coding: utf-8 -*-

from django import template
from ..models import SEO

register = template.Library()


@register.inclusion_tag('seo/metatags.html', takes_context=True)
def metatags(context):
    path = context['request'].path
    title = context.get('meta_title')
    description = context.get('meta_description')
    og_title = context.get('og_title')
    og_description = context.get('og_description')
    robots = None
    url_canonica = None

    try:
        seo_object = SEO.objects.get(url=path)
        title = seo_object.meta_title
        description = seo_object.meta_description
        og_title = seo_object.og_title
        og_description = seo_object.og_description
        robots = seo_object.meta_robots
        url_canonica = seo_object.url_canonica
    except SEO.DoesNotExist:
        pass

    return {
        'title': title,
        'description': description,
        'og_title': og_title,
        'og_description': og_description,
        'robots': robots,
        'url_canonica': url_canonica
    }
