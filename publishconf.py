#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://neurita.github.io'
RELATIVE_URLS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = u'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = u'feeds/%s.atom.xml'
#TRANSLATION_FEED_ATOM = None

FEED_ALL_RSS = u'feeds/all.rss.xml'
CATEGORY_FEED_RSS = u'feeds/%s.rss.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

PLUGINS.extend([
                'optimize_images',
               ])
