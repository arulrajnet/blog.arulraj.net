---
title: How to set the static ip address in ubuntu..?
date: 2009-03-04 09:35
author: arul
category: Linux
tags:
  - Linux
  - static
  - ip
  - ubuntu
slug: how-to-set-the-static-ip-address-in-ubuntu
disqus_identifier: /2009/03/how-to-set-the-static-ip-address-in-ubuntu.html
status: published
---

edit your /etc/network/interfaces file to

``` text
auto eth0
iface eth0 inet static
address 192.168.0.50
netmask 255.255.255.0
network 192.168.0.0
broadcast 192.168.0.255
gateway 192.168.0.1
```

after that rebooting your network by excecuting the below command...

``` bash
[root@localhost ~]# /etc/init.d/networking restart
```
