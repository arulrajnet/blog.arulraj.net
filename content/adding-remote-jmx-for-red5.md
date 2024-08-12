---
title: Adding Remote JMX for Red5
date: 2009-11-13 07:24
author: arul
category: Red5
tags: Flash,java,Linux,Programming
slug: adding-remote-jmx-for-red5
disqus_identifier: /2009/11/adding-remote-jmx-for-red5.html
status: published
---

**How to Add JMX for Red5 Server**

Here we are going to know, How to managing red5 server remotely using
JMX.

**what is red5 server ..?**

![image0](http://red5.googlecode.com/svn/doc/trunk/FinalLogo.png)

[Red5](http://code.google.com/p/red5/) is an Open Source Flash Server
written in Java that supports:

-   Streaming Video (FLV, F4V, MP4)
-   Streaming Audio (MP3, F4A, M4A)
-   Recording Client Streams (FLV only)
-   Shared Objects
-   Live Stream Publishing
-   Remoting

This is developed by Reverse Engineering of [Adobe Flash Media
server](http://www.adobe.com/products/flashmediaserver/).  Red5 under
the GNU Lesser General Public License. You can Modify and redistribute
this software.

**What is JMX \...?**

[JMX](http://en.wikipedia.org/wiki/JMX) stands for **J**ava
**M**anagement e\*\*X\*\*tension . JMX is written in java technology
used to monitor and manage a java application or objects.

The configuration of jmx agent in red5.properties file. the properties
are

**red5.properties**

``` properties
# JMX
jmx.rmi.port.registry=9999
jmx.rmi.port.remoteobjects=
jmx.rmi.host=0.0.0.0
jmx.rmi.ssl=false
```

`jmx.rmi.port.registry` - the RMI registry port

`jmx.rmi.host` - the host value by default 0.0.0.0 . if the host is
127.0.0.1 you can\'t access from remote. Normally this is your machine
ip address.

you must open the firwall for the port 9999. then only you access from
remote. For more information [see](http://bit.ly/1ACRRY)

you can visualize the jvm by using this software
[visualvm](https://visualvm.dev.java.net)

After install this Add the remote Host and Add remote JMX connection by
adding

`service:jmx:rmi://192.168.2.6:9999/jndi/rmi://192.168.2.6:9999/red5`

192.168.2.6 - ip address of red5

the default user name for jmx is \"red5user\" and password is
\"changeme\". you can change this bu changing the *access.properties*
and *password.properties* in red5 conf folder.

[![image1](http://1.bp.blogspot.com/_X5tq9y9xv2s/Sv1dgjLbZBI/AAAAAAAAAGA/PNEjXLK4M_U/s400/visual_vm.jpg)](http://1.bp.blogspot.com/_X5tq9y9xv2s/Sv1dgjLbZBI/AAAAAAAAAGA/PNEjXLK4M_U/s1600-h/visual_vm.jpg)
