# -*- coding: utf-8 -*-
from logging import getLogger
from django.forms import ModelForm
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Contacto
from .util import get_info
global STATIC_URL
STATIC_URL = settings.STATIC_URL

log = getLogger('django')


class ContactoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Contacto
        fields = ('nombre', 'apellido', 'telefono', 'email',
                  'servicio')

    def enviaEmail(self):
        htmly = get_template('emails/email_contacto.html')
        info = get_info()
        c_d = self.cleaned_data
        c_d['info'] = info
        c_d['STATIC_URL'] = STATIC_URL
        d = Context(c_d)
        html_content = htmly.render(d)
        asunto = u'Ingeres: Contacto'
        mail = 'Ingeres<{}>'.format(settings.DEFAULT_FROM_EMAIL)
        emails_destino = info.email_form.split(',')
        msg = EmailMessage(asunto, html_content, mail, emails_destino)
        msg.content_subtype = "html"
        msg.send()
