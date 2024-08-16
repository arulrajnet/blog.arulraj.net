#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)

### Core Pelican Settings

AUTHOR = u'Arul'
SITENAME = u'Arul Blog'
SITESUBTITLE = u'Thoughts, Stories and Ideas'
SITEURL = 'http://localhost:8000'

# Where should Pelican look for content?
PATH = ('content')
# These are relative to PATH, above
# ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']

DEFAULT_DATE = 'fs'

DEFAULT_DATE_FORMAT = '%d %b %Y'

TIMEZONE = 'Asia/Calcutta'

LOCALE = ('en_US')

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ATOM = None
FEED_RSS = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github', 'https://github.com/arulrajnet'),
         ('Python.org', 'https://python.org/'),
         ('Gist', 'https://gist.github.com/arulrajnet'),
         ('Twitter', 'https://twitter.com/arulrajnet'),)

# Social widget
SOCIAL = (('Facebook', 'https://facebook.com/arulraj.net'),
          ('Twitter', 'https://twitter.com/arulrajnet'),
          ('GitHub', 'https://github.com/arulrajnet'),
          ('Feed', 'https://feeds.feedburner.com/ArulBlog'),
          )

# Pagination
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
  (1, '{base_name}/', '{base_name}/index.html'),
  (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Static Path
STATIC_PATHS = ['assets']

DEFAULT_METADATA = {
  'status': 'draft'
}

EXTRA_PATH_METADATA = {
  'assets/robots.txt': {'path': 'robots.txt'},
  'assets/favicon.ico': {'path': 'favicon.ico'},
  'assets/css/better_responsive_images.css': {'path': 'css/better_responsive_images.css'},
  'assets/css/myblog.css': {'path': 'css/myblog.css'},
}

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_URL = '{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_URL = '{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_URL = 'category/'
CATEGORIES_SAVE_AS = 'category/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'

# Author
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = 'author/'
AUTHORS_SAVE_AS = 'author/index.html'

#Archives
ARCHIVES_URL = 'archive/'
ARCHIVES_SAVE_AS = 'archive/index.html'

# Code Block

# PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}

### Plugins

PLUGIN_PATHS = [
  'pelican-plugins',
]

# better_figures_and_images is failed articles which have <object> tag with no "data" attributes.
PLUGINS = [
  'asciidoc_reader',
  'assets',
  'obsidian',
  'pelican.plugins.neighbors',
  'pelican.plugins.related_posts',
  'pelican.plugins.seo',
  'pelican.plugins.sitemap',
  'post_stats',
]

# Sitemap
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

# Comments
DISQUS_SITENAME = "arulrajnet"

# Analytics
GOOGLE_ANALYTICS = "UA-3546274-9"

# Setting for the better_figures_and_images plugin
RESPONSIVE_IMAGES = True

THEME = 'attila'

### Attila : Theme specific settings

AUTHOR_META = {
  "arul": {
    "name": "Arulraj V",
    "cover": "https://images.unsplash.com/photo-1519217651866-847339e674d4?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80",
    "image": "https://www.gravatar.com/avatar/dead1c3ffb26a27d8b5e30e1c30e46e6?s=600",
    "location": "Chennai",
    "bio": "• Architect • DevOps • Full Stack Developer • Aspiring Entrepreneur •",
    "twitter": "arulrajnet",
    "facebook": "arulraj.net",
    "github": "arulrajnet",
    "linkedin": "arulrajnet"
  }
}

MENUITEMS = (('Home', '/'),)

SHOW_ARTICLE_MODIFIED_TIME = False
SHOW_AUTHOR_BIO_IN_ARTICLE = False
SHOW_CATEGORIES_ON_MENU = False
SHOW_COMMENTS_COUNT_IN_ARTICLE_SUMMARY = True
SHOW_CREDITS = True
SHOW_FULL_ARTICLE_IN_SUMMARY = False
SHOW_PAGES_ON_MENU = True
SHOW_SITESUBTITLE_IN_HTML_TITLE = True
SHOW_TAGS_IN_ARTICLE_SUMMARY = False

### Attila : theme specific settings

from markdown import Markdown
markdown = Markdown(extensions=['markdown.extensions.extra'])

def md(content, *args):
  return markdown.convert(content)

import urllib

def quote_plus(value, *args):
  return urllib.parse.quote_plus(value)

import urllib.parse
def urlencode(uri, **query):
  parts = list(urllib.parse.urlparse(uri))
  q = urllib.parse.parse_qs(parts[4])
  q.update(query)
  parts[4] = urllib.parse.urlencode(q)
  return urllib.parse.urlunparse(parts)

import random
def filter_shuffle(seq):
  try:
    result = list(seq)
    random.shuffle(result)
    return result
  except:
    return seq

JINJA_FILTERS = {
  'md': md,
  'quote_plus': quote_plus,
  'urlencode': urlencode,
  'shuffle': filter_shuffle,
  'max': max
}

# Jinja config - Pelican 4
JINJA_ENVIRONMENT = {
  'extensions' :[
    'jinja2.ext.loopcontrols',
    'jinja2.ext.i18n',
    'jinja2.ext.do',
  ]
}
