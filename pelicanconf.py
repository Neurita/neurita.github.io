#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DEBUG = False

SITEURL = 'https://neurita.github.io'
AUTHOR = u'Neurita developers'
SITENAME = u'<span style="color:blue;">Neurita</span>'
THEME = 'pelican-themes/pelican-elegant'
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
DEFAULT_DATE_FORMAT = '%b %d, %Y' #'%Y/%m/%d'

# Feed generation is usually not desired when developing
if DEBUG:
    SITEURL = 'http://localhost:8000'
    FEED_ALL_ATOM = None
    CATEGORY_FEED_ATOM = None
    TRANSLATION_FEED_ATOM = None
    AUTHOR_FEED_ATOM = None
    AUTHOR_FEED_RSS = None
else:
    # Feed generation is usually not desired when developing
    FEED_ALL_ATOM = u'feeds/all.atom.xml'
    CATEGORY_FEED_ATOM = u'feeds/%s.atom.xml'
    #TRANSLATION_FEED_ATOM = None

    FEED_ALL_RSS = u'feeds/all.rss.xml'
    CATEGORY_FEED_RSS = u'feeds/%s.rss.xml'

# Blogroll
LINKS =  (('Neurita', 'http://www.neurita.com/'),
          ('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'))


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MENUBRAND = [(u'Neurita','https://neurita.github.io'),]

# pelican-elegant settings
# check: https://github.com/talha131/onCrashReboot/blob/master/content/Elegant%20-%20Pelican%20Theme/configuration-variables.md
import os.path as op

DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'
SITEMAP_SAVE_AS = 'sitemap.xml'
USE_SHORTCUT_ICONS = True

TAG_SAVE_AS      = ''
AUTHOR_SAVE_AS   = ''
CATEGORY_SAVE_AS = ''

STATIC_PATHS     = ['theme/images', 'images', 'extra/*']
FEATURED_IMAGE   = './theme/images/neurita_logo.png'
# EXTRA_PATH_METADATA = {
#      'extra/robots.txt': {'path': 'robots.txt'},
#      'extra/favicon.ico': {'path': 'favicon.ico'},
#      'extra/htaccess': {'path': '.htaccess'}
# }

PLUGIN_PATHS     = [op.join(op.dirname(op.realpath(__file__)), 'pelican-plugins')]
PLUGINS          = ['optimize_images',
                    'thumbnailer',
                    'sitemap',
                    'extract_toc',
                    'tipue_search',
                    'neighbors',
                    'assets',
                    'gravatar',
                    'github_activity',
                    'share_post',
                    'ipynb',
                    'latex',
                    'summary',
                    'liquid_tags.img',
                    'series',
                    'render_math',
                    ]

# from markdown.extensions.codehilite import CodeHiliteExtension
# from markdown.extensions.toc import TocExtension
# MD_EXTENSIONS = [
#     CodeHiliteExtension(css_class='highlight'),
#     TocExtension(permalink=True),
#     'markdown.extensions.extra',
#     'headerid'
# ]
MD_EXTENSIONS    = ['codehilite(css_class=highlight)',
                    'extra',
                    'smarty',
                    'headerid',
                    'toc(permalink=true)']

MARKUP = ('rst', 'md', 'ipynb')

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404', 'sitemap'))

OUTPUT_SOURCES = 'True'
OUTPUT_SOURCES_EXTENSION = '.txt'

# Elegant Labels
DISQUS_SITENAME      = 'neurita'
ABOUT_ME_LABEL       = u'About us' #u'We are <span itemprop="name"> Neurita</span>.'
MY_PROJECTS_LABEL    = u'Projects'
SOCIAL_PROFILE_LABEL = u'Stay in Touch'
RELATED_POSTS_LABEL  = 'Keep Reading'
SHARE_POST_INTRO     = 'Like this post? Share on:'
COMMENTS_INTRO       = u'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'

TYPOGRIFY = True

SLUGIFY_SOURCE = 'basename'

# Social
SOCIAL = (
        ('Twitter', 'http://twitter.com/neuritabcc'),
        ('Github', 'http://github.com/neurita'),
        ('Email', 'mailto:info@neurita.com'),
          )

# Social widget
# SOCIAL = (('Twitter', 'twitter-square', 'https://twitter.com/neuritabcc'),
#           ('GitHub', 'github', 'https://github.com/neurita'))
#
TWITTER_USERNAME = 'neuritabcc'
GITHUB_URL = 'https://github.com/neurita'
GITHUB_ACTIVITY_FEED = 'https://github.com/neurita.atom'
GITHUB_ACTIVITY_MAX_ENTRIES = 5


# Legal
SITE_LICENSE = u'<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">This blog</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://www.neurita.com" property="cc:attributionName" rel="cc:attributionURL">Neurita developers</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.'

# SEO
SITE_DESCRIPTION = u'We are Neurita BCC\u2015 a software engineering group. This is our official blog.'


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Landing Page
PROJECTS = [
        {
            'name': 'Boyle',
            'url':  'https://github.com/Neurita/boyle',
            'description': 'Medical Image Conversion and Input/Output Tools.'
            'Tools to manage DICOM and NifTI files.'},
        {
            'name': 'Galvani',
            'url': 'https://github.com/Neurita/galvani',
            'description': 'Brain Functional MRI Analysis Tools.'
            'Old and new functional connectivity analysis algorithms.'},

        {
            'name': 'Darwin',
            'url': 'https://github.com/Neurita/darwin',
            'description': 'Classification pipelines and Machine Learning Tools.'
            'An interface for Scikit-Learn (and others in the future) pipelines and algorithms training.'},
        {
            'name': 'Galton',
            'url': 'https://github.com/Neurita/galton',
            'description': 'Univariate Voxel Analysis and Correlations Tools.'
            ' Helpers for statistical univariate analyses.'},
        {
            'name': 'Cajal',
            'url': 'https://github.com/Neurita/cajal',
            'description': 'Visualization Tools for brain MRI.'
            'Visualization tools based on matplotlib, soon on Bokeh and PySurfer.'},
        ]

LANDING_PAGE_ABOUT = {'title': 'We develop medical research and data analytics tools.',
        'details': """<div itemscope itemtype="http://schema.org/Person">

       <p>
       Our origin is the <a href='http://www.ehu.eus/ccwintco' target="_blank">Computational
       Intelligence Group (GIC)</a> and we are also founders of the
       <a href='http://pyss.org/' target="_blank">Python San Sebastián Society (ACPySS)</a>.</p>
       <p>
       We work on software solutions for
       medical imaging, clinical data and data analytics. We collaborate with
       local and European research medical groups to offer solutions to help in
       their research. We program mostly on Python and C++11, but sometimes we
       also use R.</p>
       <p>We try to improve the research collaboration in our area
       and leverage the free software movement. We develop and contribute to open source projects.
       We believe that software still has many slots to fill in the medical field
       and machine learning will play a very disruptive role.
       We are actively looking for new collaborations and opportunities as well as startup and research fundings.</p>
       <p>
       <a href="mailto:info@neurita.com" title="Email address" itemprop="email"><i class="fa fa-envelope share-post-links"></i></a>
       <a href="https://twitter.com/neuritabcc" class="twitter-follow-button" data-show-count="true">Follow @neuritabcc</a>
       <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>
       <iframe src="https://ghbtns.com/github-btn.html?user=neurita&type=follow&count=true" allowtransparency="true" frameborder="0" scrolling="0" width="165" height="20"></iframe>
       </p>
       </div>"""}
