Installing Oracle JDK / JRE in CentOS Ubuntu
############################################
:date: 2014-06-06 13:18
:author: arul
:category: Linux
:tags: centos, java, Linux, ubuntu, how to
:slug: installing-oracle-jdk-jre-in-centos-ubuntu
:status: published

**How to install Java in VM**

|image0|

In earlier days (while SUN), Installing JRE / JDK in a VM is very easy
process just like extracting a file and use it. Now wget-ing the source
file itself a bit long process. After that you have use few commands to
set this newly installed Java as default Java. So I have came up with
list of steps to make installing java easier in CentOS and Ubuntu.

**Downloading JDK...?**

In VM's usually you get terminal not GUI. So I followed command way in
this tutorial. You have to add cookies to download java via wget
command.

For CentOS

| [bash]
|  [root@localhost]# wget --no-cookies --no-check-certificate --header
  "Cookie:
  gpw\_e24=http%3A%2F%2Fwww.oracle.com%2F;oraclelicense=accept-securebackup-cookie"
  http://download.oracle.com/otn-pub/java/jdk/7u55-b13/jdk-7u55-linux-x64.rpm
|  [/bash]

For Ubuntu

| [bash]
|  [ubuntu@localhost]# wget --no-cookies --no-check-certificate --header
  "Cookie:
  gpw\_e24=http%3A%2F%2Fwww.oracle.com%2F;oraclelicense=accept-securebackup-cookie"
  http://download.oracle.com/otn-pub/java/jdk/7u55-b13/jdk-7u55-linux-x64.tar.gz
|  [/bash]

**Installing and Setting...?**

For CentOS

| [bash]
|  [root@localhost]# rpm -Uvh jdk-7u55-linux-x64.rpm
|  [root@localhost]# alternatives --install /usr/bin/javaws javaws
  /usr/java/latest/bin/javaws 2
|  [root@localhost]# alternatives --install /usr/bin/java java
  /usr/java/latest/bin/java 2
|  [root@localhost]# alternatives --install /usr/bin/javac javac
  /usr/java/latest/bin/javac 2
|  [/bash]

For Ubuntu

| [bash]
|  [ubuntu@localhost]# sudo mkdir -p /usr/java/jdk1.7.0\_55
|  [ubuntu@localhost]# sudo tar -xzvf jdk-7u55-linux-x64.tar.gz -C
  /usr/java/
|  [ubuntu@localhost]# sudo ln -s /usr/java/jdk1.7.0\_55
  /usr/java/latest
|  [ubuntu@localhost]# sudo ln -s /usr/java/latest /usr/java/default
|  [ubuntu@localhost]# sudo update-alternatives --install
  /usr/bin/javaws javaws /usr/java/latest/bin/javaws 2
|  [ubuntu@localhost]# sudo update-alternatives --install /usr/bin/java
  java /usr/java/latest/bin/java 2
|  [ubuntu@localhost]# sudo update-alternatives --install /usr/bin/javac
  javac /usr/java/latest/bin/javac 2
|  [/bash]

For ubuntu there is a PPA released by webupd8team. But that is not
working since 16th March.

PPA way

| [bash]
|  [ubuntu@localhost ~]# sudo add-apt-repository ppa:webupd8team/java
|  [ubuntu@localhost ~]# sudo apt-get update
|  [ubuntu@localhost ~]# sudo apt-get install oracle-java7-installer
|  [/bash]

**Installing JRE...?**

To install JRE the downloading links only different. The other commands
are same. Here I had some direct links for different versions of JDK and
JRE

JDK 1.7 ( 64 Bit ) :

http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.rpm

http://download.oracle.com/otn-pub/java/jdk/7u55-b13/jdk-7u55-linux-x64.rpm

http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.tar.gz

http://download.oracle.com/otn-pub/java/jdk/7u55-b13/jdk-7u55-linux-x64.tar.gz

JRE 1.7 ( 64 Bit ) :

http://download.oracle.com/otn-pub/java/jdk/7u55-b13/server-jre-7u55-linux-x64.tar.gz

http://download.oracle.com/otn-pub/java/jdk/7u51-b13/server-jre-7u51-linux-x64.tar.gz

http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jre-7u51-linux-x64.rpm

http://download.oracle.com/otn-pub/java/jdk/7u55-b13/jre-7u55-linux-x64.tar.gz

http://download.oracle.com/otn-pub/java/jdk/7u55-b13/jre-7u55-linux-x64.rpm

.. |image0| image:: http://2.bp.blogspot.com/-7e9P9JpkCKg/U5ITbc1zw3I/AAAAAAAAVz8/-NrvH8mXWyU/s320/download.jpg
   :target: http://2.bp.blogspot.com/-7e9P9JpkCKg/U5ITbc1zw3I/AAAAAAAAVz8/-NrvH8mXWyU/s1600/download.jpg
