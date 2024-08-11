PixelServ using Nginx
#####################

:title: PixelServ using Nginx
:slug: pixelserv-using-nginx
:date: 2015-11-21 11:31:49
:tags: proxy, adblock, nginx
:category: proxy
:author: arul
:lang: en
:disqus_identifier: /2015/11/pixelserv-using-nginx.html


Hope you know about `pixelserv <http://proxytunnel.sourceforge.net/pixelserv.php>`__. It is a webserver which will always response 1x1 transparent gif image for all kind of requests. Mainly used in adblocking and proxy environmental.

In this setup I am going to serve 1x1 pixel using nginx server.

**Install nginx**

.. code-block:: bash

  sudo apt-get install nginx -y

**Configuration**

changing ``/etc/nginx/nginx.conf`` as below

.. code-block:: json

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

**Check**

.. code-block:: bash

  sudo service nginx restart
  curl http://localhost/

You will get binary GIF blob in terminal.

.. figure:: /assets/images/nginx-pixelserv.png
    :align: center
    :alt: pixelserv using nginx

.. NGINX pixelserv

**Using Docker**

docker-compose.yml for that is

.. code-block:: yml

  pixelserv:
    image: nginx:1.9.6
    ports:
      - 80:80
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    hostname: pixelserv
