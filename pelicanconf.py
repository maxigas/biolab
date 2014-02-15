#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'biofou'
SITENAME = u'Calafou Biolab'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Added lines to the default config

# Plugin configuration
# Source: https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites

PLUGINS = ['i18n_subsites']
PLUGIN_PATH = '/usr/local/lib/python2.7/pelican-plugins'

# mapping: language_code -> conf_overrides_dict
I18N_SUBSITES = {
    'en': {
        'SITENAME': 'Calafou Biolab',
        'LOCALE': 'en_GB',
        },
    'es': {
        'SITENAME': 'Calafou Biolab',
        'LOCALE': 'es_ES',
        },
    'cat': {
        'SITENAME': 'Calafou Biolab',
        'LOCALE': 'ca',
        },
    }

languages_lookup = {
    'en': 'English',
    'es': 'Spanish',
    'cat': 'Catalan',
    }

def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]


def my_ordered_items(dict):
    items = list(dict.items())
    # swap first and last using tuple unpacking
    items[0], items[-1] = items[-1], items[0]
    return items


JINJA_FILTERS = {
    'lookup_lang_name': lookup_lang_name,
    'my_ordered_items': my_ordered_items,
    }

STATIC_PATHS = ['images', 'files']

# Themes
# Source:
# http://docs.getpelican.com/en/3.3.0/settings.html#themes

THEME = "biotema"
