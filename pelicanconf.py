#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Luis J. Salvatierra'
SITENAME = u'Neurita'
SITEURL = 'https://neurita.github.io'
THEME = 'pelican-themes/pelipress'
DISPLAY_PAGES_ON_MENU = True

PATH = 'content'
ALBUM_PATH = 'images'
THUMBNAIL_OUTPUT_PATH = 'images/thumbnails'
THUMBNAIL_OUTPUT_FORMAT = 'JPEG'
THUMBNAIL_DEFAULT_SIZE = '192x192'
THUMBNAIL_DEFAULT_QUALITY = 80
#ALBUM_SAVE_AS
#ALBUM_URL


TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%Y/%m/%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
'''
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)
'''
# Social widget
'''
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
'''
DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MENUBRAND = [(u'Neurita','https://neurita.github.io'),]
