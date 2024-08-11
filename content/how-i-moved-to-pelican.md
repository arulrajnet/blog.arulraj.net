---
title: How I moved to pelican

slug:   how-i-moved-to-pelican
date:   2015-05-29 09:41:20
tags:   pelican, blog, static hosting
category:   Python
author: arul
lang:   en
summary:
status:   draft
disqus_identifier:    python-how-i-moved-to-pelican
---

\### Publishing

<http://pbpython.com/pelican-config.html>

\$ pip install s3cmd \$ s3cmd \--configure

\$ s3cmd sync ./output/ s3://pbpython.com/ \--acl-public
\--delete-removed \--guess-mime-type
