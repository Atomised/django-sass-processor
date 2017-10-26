# -*- coding: utf-8 -*-
from django.conf import settings
from django.template import TemplateSyntaxError
from rtg_portal.context_processors import whitelabel_processor
from admin_portal.models import Whitelabel
from django.forms.models import model_to_dict


def get_setting(key):
    try:
        return getattr(settings, key)
    except AttributeError as e:
        raise TemplateSyntaxError(e.message)


def get_db_setting(whl):
    try:
        # and any associated whitelabel
        whitelabel = Whitelabel.objects.filter(slug=whl).order_by('id')    
        # if whitelabel, load config
        if whitelabel.count() != 0:
            # if key:
            #     print getattr(whitelabel[0], key)
            #     return getattr(whitelabel[0], key)
            # else:
            print model_to_dict(whitelabel[0], fields=[field.name for field in whitelabel[0]._meta.fields]) 
            return model_to_dict(whitelabel[0], fields=[field.name for field in whitelabel[0]._meta.fields])
        
    except AttributeError as e:
        raise TemplateSyntaxError(e.message)
