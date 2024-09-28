---
title: Jetty Server Doesn't honor X-Forwarded-Host
date: 2024-09-28 11:28
author: arul
category:
tags:
slug: jetty-server-doesnt-honor-x-forwarded-host
disqus_identifier: jetty-server-doesnt-honor-x-forwarded-host
cover:
color: gray
headline:
status: draft
---


```
 X-Forwarded-Host: shanssonew.secureedge.view.com
 Referer: https://shanssonew.secureedge.view.com/home
 Host: shanssonew.secureedge.view.com:9443
```

The code 

```
Response.status(302).location(uri).build()
```


Working code

```
Response.status(302).header("location",uri).build()
```