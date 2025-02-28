#!/usr/bin/env python
"""Pelican settings."""

import os
import sys


sys.path.append(os.curdir)

### Core Pelican Settings

AUTHOR = "Arul"
SITENAME = "Arul Blog"
SITESUBTITLE = "Thoughts, Stories and Ideas"
SITEURL = "http://localhost:8000"

# Where should Pelican look for content?
PATH = "content"
# These are relative to PATH, above
PAGE_PATHS = ["pages"]

DEFAULT_DATE = "fs"

DEFAULT_DATE_FORMAT = "%d %b %Y"

TIMEZONE = "Asia/Calcutta"

LOCALE = "en_US"

DEFAULT_LANG = "en"

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
LINKS = (
    ("Github", "https://github.com/arulrajnet"),
    ("Python.org", "https://python.org/"),
    ("Gist", "https://gist.github.com/arulrajnet"),
    ("Twitter", "https://twitter.com/arulrajnet"),
)

# Social widget
SOCIAL = (
    ("Facebook", "https://facebook.com/arulraj.net"),
    ("Twitter", "https://twitter.com/arulrajnet"),
    ("GitHub", "https://github.com/arulrajnet"),
    ("Feed", "https://feeds.feedburner.com/ArulBlog"),
)

# Pagination
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, "{base_name}/", "{base_name}/index.html"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)

# Static Path
STATIC_PATHS = ["assets"]

DEFAULT_METADATA = {"status": "draft"}

EXTRA_PATH_METADATA = {
    "assets/robots.txt": {"path": "robots.txt"},
    "assets/favicon.ico": {"path": "favicon.ico"},
    "assets/css/better_responsive_images.css": {
        "path": "css/better_responsive_images.css"
    },
    "assets/css/custom.css": {"path": "css/custom.css"},
}

# Post and Pages path
ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"
YEAR_ARCHIVE_URL = "{date:%Y}/"
YEAR_ARCHIVE_SAVE_AS = "{date:%Y}/index.html"
MONTH_ARCHIVE_URL = "{date:%Y}/{date:%m}/"
MONTH_ARCHIVE_SAVE_AS = "{date:%Y}/{date:%m}/index.html"

# Tags and Category path
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
CATEGORIES_URL = "category/"
CATEGORIES_SAVE_AS = "category/index.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"
TAGS_URL = "tag/"
TAGS_SAVE_AS = "tag/index.html"

# Author
AUTHOR_URL = "author/{slug}/"
AUTHOR_SAVE_AS = "author/{slug}/index.html"
AUTHORS_URL = "author/"
AUTHORS_SAVE_AS = "author/index.html"

# Archives
ARCHIVES_URL = "archive/"
ARCHIVES_SAVE_AS = "archive/index.html"

### Plugins

# better_figures_and_images is failed articles which have <object> tag with no "data" attributes. # noqa: E501
PLUGINS = [
    "asciidoc_reader",
    "pelican.plugins.image_process",
    "pelican.plugins.minify",
    "pelican.plugins.neighbors",
    "pelican.plugins.obsidian",
    "pelican.plugins.related_posts",
    "pelican.plugins.seo",
    "pelican.plugins.sitemap",
    "pelican.plugins.statistics",
    "pelican.plugins.webassets",
]

# Minify settings
CSS_MIN = True
JS_MIN = False
HTML_MIN = True
INLINE_CSS_MIN = True
INLINE_JS_MIN = True

# Sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# Markdown settings
# Refer - https://github.com/DataDog/Python-Markdown/tree/master/markdown/extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.smarty": {},
        "markdown.extensions.tables": {},
        # This is for enabling the TOC generation
        "markdown.extensions.toc": {
            "title": "Table of Contents",
            # empty marker to generate only header ids
            "marker": "[TOC]",
            "permalink": "false",
        },
    },
    "output_format": "html5",
}

# Comments
DISQUS_SITENAME = "arulrajnet"

# Analytics
GOOGLE_ANALYTICS = "UA-3546274-9"

# Setting for the better_figures_and_images plugin
RESPONSIVE_IMAGES = True

IMAGE_PROCESS = {
    "crisp": {
        "type": "responsive-image",
        "srcset": [
            ("1x", ["scale_in 800 600 True"]),
            ("2x", ["scale_in 1600 1200 True"]),
            ("4x", ["scale_in 3200 2400 True"]),
        ],
        "default": "1x",
    },
    "large-photo": {
        "type": "responsive-image",
        "sizes": (
            "(min-width: 1200px) 800px, "
            "(min-width: 992px) 650px, "
            "(min-width: 768px) 718px, "
            "100vw"
        ),
        "srcset": [
            ("600w", ["scale_in 600 450 True"]),
            ("800w", ["scale_in 800 600 True"]),
            ("1600w", ["scale_in 1600 1200 True"]),
        ],
        "default": "800w",
    },
}

try:
    import attila

    THEME = attila.get_path()
except ImportError:
    THEME = "attila"

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
        "linkedin": "arulrajnet",
    }
}

CSS_OVERRIDE = ["css/custom.css"]

MENUITEMS = (("Home", "/"),)

SHOW_ARTICLE_MODIFIED_TIME = False
SHOW_AUTHOR_BIO_IN_ARTICLE = False
SHOW_CATEGORIES_ON_MENU = False
SHOW_COMMENTS_COUNT_IN_ARTICLE_SUMMARY = False
SHOW_CREDITS = True
SHOW_FULL_ARTICLE_IN_SUMMARY = False
SHOW_PAGES_ON_MENU = True
SHOW_SITESUBTITLE_IN_HTML_TITLE = True
SHOW_TAGS_IN_ARTICLE_SUMMARY = False

### Attila : theme specific settings

from markdown import Markdown


# This is used in jinja2 filters
markdown = Markdown(
    extensions=[
        "markdown.extensions.codehilite",
        "markdown.extensions.extra",
        "markdown.extensions.meta",
        "markdown.extensions.smarty",
        "markdown.extensions.tables",
        "markdown.extensions.toc",
    ],
    extension_configs={
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.smarty": {},
        "markdown.extensions.tables": {},
        "markdown.extensions.toc": {
            "title": "Table of Contents",
            "marker": "[TOC]",
            "permalink": "false",
        },
    },
    output_format="html5",
)


def md(content, *args):
    """Markdown filter."""
    return markdown.convert(content)


import urllib


def quote_plus(value, *args):
    """URL encode filter."""
    return urllib.parse.quote_plus(value)


import urllib.parse


def urlencode(uri, **query):
    """URL encode filter."""
    parts = list(urllib.parse.urlparse(uri))
    q = urllib.parse.parse_qs(parts[4])
    q.update(query)
    parts[4] = urllib.parse.urlencode(q)
    return urllib.parse.urlunparse(parts)


import random


def filter_shuffle(seq):
    """Shuffle filter."""
    try:
        result = list(seq)
        random.shuffle(result)
        return result
    except:
        return seq


import os


def basename(path):
    """Basename filter."""
    return os.path.basename(path)


def dirname(path):
    """Dirname filter."""
    return os.path.dirname(path)


JINJA_FILTERS = {
    "basename": basename,
    "dirname": dirname,
    "max": max,
    "md": md,
    "quote_plus": quote_plus,
    "shuffle": filter_shuffle,
    "urlencode": urlencode,
}

# Jinja config - Pelican 4
JINJA_ENVIRONMENT = {
    "extensions": [
        "jinja2.ext.loopcontrols",
        "jinja2.ext.i18n",
        "jinja2.ext.do",
    ]
}
