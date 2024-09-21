---
title: Docker Compose inline configuration file
date: 2024-09-21 14:10
author: arul
category: Docker
tags: docker-compose
slug: docker-compose-inline-configuration-file
disqus_identifier: docker-compose-inline-configuration-file
cover: assets/images/cover-image-for-inline-compose-config.png
color: gray
headline: How to use single yaml file for your docker application stack. No need to mount your configuration as volume or folder. Support for environmental interpolation. Support for binary file. One file, so easy to maintain.
status: published
---
You know I am the big fan of docker compose (fig 😸). I am the advanced user in compose and swarm. Deployed swarm based cluster for different product and its handles millions of request every day. 
## The requirement

Here is the example about how we can use a single YAML file for docker services and configuration. We don't need separate file or folder maintained in the repo. Just single `docker-compose.yml` file is enough. All the configuration is with in that as inline content. 

Lets dive into the topic. 

* We want to deploy a nginx proxy.
* Its has a configuration file.
* It has HTML file to serve.
* It has a image file to serve.

## Single YAML

How I can define the inline config file

```yaml
configs:
  nginx.conf:
    content: |
      your config file content
```


Refer this [doc](https://github.com/compose-spec/compose-spec/blob/231b09c30d339e950c0da17fe5bdc793366b8fde/08-configs.md){:target="_blank"} in GitHub. 

Here is the compose yaml file for nginx serve the html file content. 

```yaml
name: nginx-inline
services:
  nginx:
    image: nginx:1.27.1
    ports:
      - 8080:80
    configs:
      - source: index.html
        target: /usr/share/nginx/html/index.html
configs:
  index.html:
    content: |
      <!doctype html>
      <html>
        <head>
          <title>Hello nginx</title>
          <meta charset="utf-8" />
        </head>
        <body>
          <h1>
            Hello arulraj.net!
          </h1>
        </body>
      </html>
```

Bring up the system using `docker-compose up -d`. Then access [http://localhost:8080](http://localhost:8080)

Now you see the page like this. 

![[nginx-inline-example.png]]

The index.html loaded successfully. 


## Environmental interpolation

You can do the [environmental interpolation](https://docs.docker.com/reference/compose-file/interpolation/){:target="_blank"} in `docker-compose.yml` file in a usual way. 

* The good old `.env` file
* OR use `export` before ran `docker-compose up -d`

The following content has `WELCOME_MESSAGE` in the index.html

```yaml
configs:
  index.html:
    content: |
      <!doctype html>
      <html>
        <head>
          <title>Hello nginx</title>
          <meta charset="utf-8" />
        </head>
        <body>
          <h1>
            ${WELCOME_MESSAGE:-Hello, World!}
          </h1>
        </body>
      </html>
```


Then

```
export WELCOME_MESSAGE="Hello, Arul!"
docker-compose up -d
```

## Store environmental variable as config file

Expose the host machine environment variable inside the container as config file. 

```yaml
name: nginx-inline
services:
  nginx:
    image: nginx:1.21.1
    ports:
      - 8080:80
    configs:
      - source: path.txt
        target: /usr/share/nginx/html/path.txt
configs:
  path.txt:
    environment: "PATH"
```

Here we expose the host machine `PATH` env as `path.txt`

## Binary file

The binary file converted as `base64` and can be used. 

But this is not supported in compose spec as like kubernetes. 


Will update this post once its supported. 

