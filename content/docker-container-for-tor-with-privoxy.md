---
title: Docker container for TOR with Privoxy
slug:   docker-container-for-tor-with-privoxy
date:   2015-05-09 16:11:12
tags:   docker, tor, proxy, privoxy, crawling
category:   docker
author: arul
lang:   en
status:   published
disqus_identifier:    /2015/05/docker-container-for-tor-with-privoxy.html
---

I released a docker container for TOR with Privoxy bundled together.
Earlier I wrote a script ([Tor
Installer](https://github.com/arulrajnet/operationalscripts/blob/master/tools/tor_installer.py))
to setup the TOR and Privoxy environment in a linux system. But docker
is the correct tool to setup these kind of environment.

Hope you know what is TOR and Privoxy.

Github Repo <https://github.com/arulrajnet/torprivoxy>

Docker Repo <https://registry.hub.docker.com/u/arulrajnet/torprivoxy>

## How to Use

You have to install docker first. To install in linux [follow
this](https://docs.docker.com/installation/ubuntulinux/#installing-docker-on-ubuntu)

``` bash
docker run -d \
-p 8118:8118 -p 9050:9050 -p 9051:9051 \
--name tor -i arulrajnet/torprivoxy:latest
```

Binding port 9050 and 9051 are optional. 9051 is the controlport of TOR
Network. Using that you can forcefully regenerate the TOR ip. Read more
about
[tor_ip_renew.py](https://gist.github.com/arulrajnet/9df385cdb70d8a945686)

## Docker Tags

There are two flavor of container

  -----------------------------------
  Tag      Base Image      Size
  -------- --------------- ----------
  latest   debian:wheezy   180 MB

  wheezy   debian:wheezy   180 MB

  jessie   debian:jessie   228.1 MB
  -----------------------------------

This is the very lean image for TOR with Privoxy currently available in
[docker hub](https://registry.hub.docker.com/u/arulrajnet/torprivoxy).

## Verify

How to cross check are you getting ip from Tor or not.

**Check your IP without TOR**

``` bash
curl http://curlmyip.com
```

**Check with TOR**

``` bash
curl -v --socks5-hostname localhost:9050 http://curlmyip.com
```

**Check with privoxy**

``` bash
export http_proxy=http://localhost:8118/
curl http://curlmyip.com
unset http_proxy

or

curl -x http://localhost:8118 -L http://curlmyip.com
```

## Debug

If the above step is not success you have to verify the log files.

``` bash
docker exec -it tor /bin/bash
```

All the log files in the `/tmp` folder of container.

**To restart TOR and Provoxy**

``` bash
supervisionctl
supervisor> status
supervisor> restart tor
supervisor> restart privoxy
```

## Global Proxy

You can set privoxy as a global proxy so that all your traffic goes via
TOR

### In Ubuntu

Open `/etc/environment`

``` bash
http_proxy="http://127.0.0.1:8118"
https_proxy="http://127.0.0.1:8118"
ftp_proxy="http://127.0.0.1:8118"
HTTP_PROXY="http://127.0.0.1:8118"
HTTPS_PROXY="http://127.0.0.1:8118"
FTP_PROXY="http://127.0.0.1:8118"
_JAVA_OPTIONS="-Dhttp.proxyHost=localhost -Dhttp.proxyPort=8118"
```

Add this at the EOF.

Then `source /etc/environment`

### In CentOS

Create file `/etc/profile.d/proxy.sh` Then put the below content and
save.

``` bash
http_proxy="http://127.0.0.1:8118"
https_proxy="http://127.0.0.1:8118"
ftp_proxy="http://127.0.0.1:8118"
HTTP_PROXY="http://127.0.0.1:8118"
HTTPS_PROXY="http://127.0.0.1:8118"
FTP_PROXY="http://127.0.0.1:8118"
_JAVA_OPTIONS=$_JAVA_OPTIONS" -Dhttp.proxyHost=localhost -Dhttp.proxyPort=8118"

export http_proxy https_proxy ftp_proxy HTTP_PROXY HTTPS_PROXY FTP_PROXY _JAVA_OPTIONS
```

Then `source /etc/profile.d/proxy.sh` OR you can set the same in
`.bashrc` or `.bash_profile`
