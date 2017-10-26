# -*- coding: utf-8 -*-
from django.conf import settings
from django.template import TemplateSyntaxError
from rtg_portal.context_processors import whitelabel_processor


def get_setting(key):
    try:
        return getattr(settings, key)
    except AttributeError as e:
        raise TemplateSyntaxError(e.message)


def get_db_setting(key):
    try:
    	config = whitelabel_processor()
    	print config
        return getattr(config, key)
    except AttributeError as e:
        raise TemplateSyntaxError(e.message)
