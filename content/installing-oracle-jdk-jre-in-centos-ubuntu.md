---
title: Installing Oracle JDK / JRE in CentOS Ubuntu
date:   2014-06-06 13:18:12
tags:   centos, java, Linux, ubuntu, how-to
slug:   installing-oracle-jdk-jre-in-centos-ubuntu
category:   Linux
author: arul
lang:   en
status:   published
summary:   Installing oracle / SUN JDK and JRE in ubuntu and CentOS
disqus_identifier:    /2014/06/installing-oracle-jdk-jre-in-centos-ubuntu.html
---

[![image0](http://2.bp.blogspot.com/-7e9P9JpkCKg/U5ITbc1zw3I/AAAAAAAAVz8/-NrvH8mXWyU/s320/download.jpg)](http://2.bp.blogspot.com/-7e9P9JpkCKg/U5ITbc1zw3I/AAAAAAAAVz8/-NrvH8mXWyU/s1600/download.jpg)

In earlier days (while SUN), Installing JRE / JDK in a VM is very easy
process just like extracting a file and use it. Now wget-ing the source
file itself a bit long process. After that you have use few commands to
set this newly installed Java as default Java. So I have came up with
list of steps to make installing java easier in CentOS and Ubuntu.

## Downloading JDK\...?

In VM\'s usually you get terminal not GUI. So I followed command way in
this tutorial. You have to add cookies to download java via wget
command.

### For CentOS

``` bash
wget --no-cookies --no-check-certificate \
--header "Cookie:gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;oraclelicense=accept-securebackup-cookie" \
http://download.oracle.com/otn-pub/java/jdk/7u55-b13/jdk-7u55-linux-x64.rpm
```

### For Ubuntu

``` bash
wget --no-cookies --no-check-certificate \
--header "Cookie:gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;oraclelicense=accept-securebackup-cookie" \
http://download.oracle.com/otn-pub/java/jdk/7u55-b13/jdk-7u55-linux-x64.tar.gz
```

I wrote a python script to download the Oracle Java jdk / jre from
terminal.

That script in <https://gist.github.com/arulrajnet/7b261203499375bd0759>

**How to Use**

``` bash
wget --no-check-certificate https://gist.github.com/arulrajnet/7b261203499375bd0759/raw/download_java.py
chmod +x download_java.py
python download_java.py
```

It will ask for the type of package you want to download and version of
package want to download. Finally the selected file will be downloaded
in the current directory

[![download_java.py](http://1.bp.blogspot.com/-eo7_9M3j3A8/VU4kPpVeykI/AAAAAAAAWPM/ohiVIUXjUHo/s640/download_java.png)](http://1.bp.blogspot.com/-eo7_9M3j3A8/VU4kPpVeykI/AAAAAAAAWPM/ohiVIUXjUHo/s1600/download_java.png)

## Installing and Setting\...?

In the installation to make this java as default one in the system wide.

### For CentOS

``` bash
rpm -Uvh jdk-7u55-linux-x64.rpm
alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws 2
alternatives --install /usr/bin/java java /usr/java/latest/bin/java 2
alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac 2
```

### For Ubuntu

``` bash
sudo mkdir -p /usr/java/jdk1.7.0_55
sudo tar -xzvf jdk-7u55-linux-x64.tar.gz -C /usr/java/
sudo ln -s /usr/java/jdk1.7.0_55/usr/java/latest
sudo ln -s /usr/java/latest /usr/java/default
sudo update-alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws 2
sudo update-alternatives --install /usr/bin/java java /usr/java/latest/bin/java 2
sudo update-alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac 2
```

For ubuntu there is a PPA released by webupd8team.

**PPA way**

``` bash
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java7-installer
```

Note: But that is not working since 16th March. Hope they fixed now.

## Installing JRE\...?

To install JRE the downloading links only different. The other commands
are same. Here I had some direct links for different versions of JDK and
JRE

**JRE 1.7 ( 64 Bit )**

<http://download.oracle.com/otn-pub/java/jdk/7u55-b13/server-jre-7u55-linux-x64.tar.gz>

<http://download.oracle.com/otn-pub/java/jdk/7u51-b13/server-jre-7u51-linux-x64.tar.gz>

<http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jre-7u51-linux-x64.rpm>

<http://download.oracle.com/otn-pub/java/jdk/7u55-b13/jre-7u55-linux-x64.tar.gz>

<http://download.oracle.com/otn-pub/java/jdk/7u55-b13/jre-7u55-linux-x64.rpm>

**JDK 1.7 ( 64 Bit )**

<http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.rpm>

<http://download.oracle.com/otn-pub/java/jdk/7u55-b13/jdk-7u55-linux-x64.rpm>

<http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.tar.gz>

<http://download.oracle.com/otn-pub/java/jdk/7u55-b13/jdk-7u55-linux-x64.tar.gz>
