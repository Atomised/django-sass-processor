# -*- coding: utf-8 -*-
from django.conf import settings
from django.template import TemplateSyntaxError
from rtg_portal.context_processors import whitelabel_processor
from admin_portal.models import Whitelabel


def get_setting(key):
    try:
        return getattr(settings, key)
    except AttributeError as e:
        raise TemplateSyntaxError(e.message)


def get_db_setting(whl, key):
    try:
        # and any associated whitelabel
        whitelabel = Whitelabel.objects.filter(slug=whl).order_by('id')    
        # if whitelabel, load config
        if whitelabel.count() != 0:
            print getattr(whitelabel[0])
            return getattr(whitelabel[0])
        
    except AttributeError as e:
        raise TemplateSyntaxError(e.message)
