#!/usr/bin/env python

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys


sys.path.append(os.curdir)
from pelicanconf import *


# Generate feed while publish
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/category/{slug}.atom.xml"
TAG_FEED_ATOM = "feeds/tag/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = "feeds/author/{slug}.atom.xml"

# Relative url
RELATIVE_URLS = False

SITEURL = "https://www.arulraj.net"
S3_BUCKET_NAME = "www.arulraj.net"
