---
title: PixelServ using Nginx
date: 2015-11-21 11:31:49
tags: proxy,adblock,nginx
slug: pixelserv-using-nginx
category: proxy
author: arul
lang: en
disqus_identifier: /2015/11/pixelserv-using-nginx.html
status: published
---

Hope you know about
[pixelserv](http://proxytunnel.sourceforge.net/pixelserv.php). It is a
webserver which will always response 1x1 transparent gif image for all
kind of requests. Mainly used in adblocking and proxy environmental.

In this setup I am going to serve 1x1 pixel using nginx server.

**Install nginx**

``` bash
sudo apt-get install nginx -y
```

**Configuration**

changing `/etc/nginx/nginx.conf` as below

``` json
user nginx;
worker_processes 4;

error_log  /dev/stdout;
pid        /var/run/nginx.pid;

events { worker_connections 1024; }

http {

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

      access_log  /dev/stdout;
      sendfile        on;
      keepalive_timeout  65;

      server {
        listen 80 default_server;
        listen [::]:80 default_server ipv6only=on;

        # Make site accessible from http://localhost/
        server_name _;

        location / {
          empty_gif;
        }
      }
}
```

**Check**

``` bash
sudo service nginx restart
curl http://localhost/
```

You will get binary GIF blob in terminal.

<figure class="align-center">
<img src="/assets/images/nginx-pixelserv.png"
alt="/assets/images/nginx-pixelserv.png" />
</figure>

**Using Docker**

docker-compose.yml for that is

``` yml
pixelserv:
  image: nginx:1.9.6
  ports:
    - 80:80
  volumes:
    - ./nginx.conf:/etc/nginx/nginx.conf
  hostname: pixelserv
```
