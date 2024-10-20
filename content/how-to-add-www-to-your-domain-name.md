---
title: How to add www to your domain name
date: 2010-03-08 04:36:00
author: arul
category: Programming
tags: Browser,php,how-to,hosting
slug: how-to-add-www-to-your-domain-name
disqus_identifier: /2010/03/how-to-add-www-to-your-domain-name.html
status: published
---

**How to add www to your domain name**

[![image0](http://3.bp.blogspot.com/_X5tq9y9xv2s/S5TOlrA6HBI/AAAAAAAAAMo/46plgLZv_mw/s400/htaccess.gif)](http://3.bp.blogspot.com/_X5tq9y9xv2s/S5TOlrA6HBI/AAAAAAAAAMo/46plgLZv_mw/s1600-h/htaccess.gif)

Before going to the htaccess . You need to answer my question, The
question is

**Do you think arulraj.net and www.arulraj.net both are different domain
name or same ..?**

ya. we (humans) know both are points the same web page. But the search
engine robots assume this both are different one. As a result duplicate
results in the search results. To avoid this problem you need to develop
search engine friendly web pages.

Now the topic,

**How to add www in front of your domain name ..?**

For this you are aware of
[htaccess](http://en.wikipedia.org/wiki/Htaccess) file and where it is
located.

htaccess - Hypertext Access

The file located in root directory of your domain name .

For example : */home/\<username\>/public_html/\<domain dir
name\>/.htaccess*

That above structure in Bluehost.Now add this line to your .htaccess
file

``` text
RewriteEngine On
RewriteBase /
RewriteCond %{HTTP\_HOST} ^sharedaa\\.com$ [NC]
RewriteRule ^(.*)$ http://www.sharedaa.com/$1 [R=301,L]
```

Now anyone type sharedaa.com in browser it is automatically redirect to
www.sharedaa.com

How to redirect to index page if the page is not available ..?

One of your page is indexed in search engine. You remove the page, at
this time you want to redirect to home page. how to do this.Add the
below line to your htaccess file.

``` text
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
```

The final .htaccess file will be

``` text
# Use PHP5CGI as default
AddHandler application/x-httpd-php5 .php

# BEGIN
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteCond %{HTTP_HOST} ^sharedaa\.com$ [NC]
RewriteRule ^(.\*)$ http://www.sharedaa.com/$1 [R=301,L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>

# END
```

**How to add www to your wordpress blog ..?**

Go to Setting \--\> General setting page and in the Blog Address text
box enter your domain name with www . for example
<http://www.sharedaa.com>

[![image1](http://1.bp.blogspot.com/_X5tq9y9xv2s/S5TVR_LfRuI/AAAAAAAAAMw/sOJ7-_iVg1Q/s400/wordpress-www.jpg)](http://1.bp.blogspot.com/_X5tq9y9xv2s/S5TVR_LfRuI/AAAAAAAAAMw/sOJ7-_iVg1Q/s1600-h/wordpress-www.jpg)

Reference : <http://www.thesitewizard.com/apache/index.shtml>
