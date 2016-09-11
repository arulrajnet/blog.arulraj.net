#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

### Core Pelican Settings

AUTHOR = u'Arul'
SITENAME = u'Arul Blog'
SITEURL = 'http://localhost:8000'

PATH = 'content'

DEFAULT_DATE_FORMAT = '%d %b %Y'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = u'en'

DISPLAY_CATEGORIES_ON_MENU = False

FAVICON_FILENAME = "favicon.ico"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github', 'http://github.com/arulrajnet'),
         ('Python.org', 'http://python.org/'),
         ('Gist', 'http://gist.github.com/arulrajnet'),
         ('Twitter', 'http://twitter.com/arulrajnet'),)

# Social widget
SOCIAL = (('Facebook', 'http://facebook.com/arulraj.net'),
          ('Twitter', 'http://twitter.com/arulrajnet'),
          ('Google Plus', 'https://plus.google.com/+ArulrajNet'),
          ('Feed', 'http://feeds.feedburner.com/ArulBlog'),
          )

# Pagination
DEFAULT_PAGINATION = 10
# PAGINATION_PATTERNS = (
#     (1, '{base_name}/', '{base_name}/index.html'),
#     (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
# )

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
    'assets/css/better_responsive_images.css': {'path': 'css/custom.css'},
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
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Code Block

# PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}

# Comments
DISQUS_SITENAME = "arulrajnet"

# Analytics
GOOGLE_ANALYTICS = "UA-3546274-9"

# Search
SEARCH_BOX = False

### Theme specific settings

## Start - pelican-clean-blog - https://github.com/gilsondev/pelican-clean-blog
COLOR_SCHEME_CSS = 'github_jekyll.css'
# Copied from https://github.com/mingp/pelican-clean-blog-theme/blob/master/static/css/clean-blog.css
CSS_OVERRIDE = 'assets/css/myblog.css'

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

PLUGINS = [
  'sitemap', 
  'neighbors', 
  'related_posts', 
  'post_stats',
  'assets',
  'better_figures_and_images',
]

# Sitemap
SITEMAP = {
    'format': 'xml',
    'changefreqs': {
            'pages': 'daily',
            'posts': 'daily',
    }
}

# Read time - Medium like
X_MIN_READ = False

# Setting for the better_figures_and_images plugin
RESPONSIVE_IMAGES = True

# This is not working
CUSTOM_CSS = '/css/custom.css'
