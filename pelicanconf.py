#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)

### Core Pelican Settings

AUTHOR = u'Arul'
SITENAME = u'Arul Blog'
# SITESUBTITLE = ''
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

DISPLAY_CATEGORIES_ON_MENU = False

FAVICON_FILENAME = "favicon.ico"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GITHUB_URL = 'https://github.com/arulrajnet/'

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
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Static Path
STATIC_PATHS = ['assets']

DEFAULT_METADATA = {
    # 'status': 'draft',
}

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/css/better_responsive_images.css': {'path': 'css/better_responsive_images.css'},
    'assets/css/myblog.css': {'path': 'css/myblog.css'},
}

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

# Code Block

# PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}

# Comments
DISQUS_SITENAME = "arulrajnet"

# Analytics
GOOGLE_ANALYTICS = "UA-3546274-9"

# Search
SEARCH_BOX = False

THEME = 'attila'

### Theme specific settings

AUTHORS_BIO = {
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

## End - pelican-clean-blog

# Twitter
TWITTER_USERNAME = "arulrajnet"
TWITTER_WIDGET_ID = 518216345154895874
TWITTER_TWEET_BUTTON = False
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 5
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'

# Facebook
FACEBOOK_LIKE = True

# Google Plus
GOOGLE_PLUS_ID = 108329785817736505170
#ArulrajNet

# QR Code
QR_CODE = False

# Feed Burner
FEED_FEEDBURNER = 'ArulBlog'

### Plugins

PLUGIN_PATHS = [
  'pelican-plugins',
]

# better_figures_and_images is failed articles which have <object> tag with no "data" attributes.
PLUGINS = [
  'asciidoc_reader',
  'assets',
  'neighbors',
  'post_stats',
  'related_posts',
  'sitemap',
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

# Read time - Medium like
X_MIN_READ = False

# Setting for the better_figures_and_images plugin
RESPONSIVE_IMAGES = True
