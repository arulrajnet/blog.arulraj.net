---
title: CentOS Networking FAQ
date: 2009-07-14 07:57:00
author: arul
category: Linux
tags: Linux,static-ip
slug: centos-networking-faq
disqus_identifier: /2009/07/centos-networking-faq.html
status: published
---

[![image0](http://3.bp.blogspot.com/_Tq9uaJI0Xww/SlyToWJ_bHI/AAAAAAAAFFM/U3akGuy-MxU/s400/centos-logo.png){.align-middle}](http://3.bp.blogspot.com/_Tq9uaJI0Xww/SlyToWJ_bHI/AAAAAAAAFFM/U3akGuy-MxU/s1600-h/centos-logo.png)

**How to set static ip..?**

``` shell
[root@localhost ~]# cat /etc/sysconfig/network-scripts/ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.1.13
NETMASK=255.255.255.0
TYPE=Ethernet
[root@localhost ~]#
```

Edit your `/etc/sysconfig/network-scripts/ifcfg-eth0` file like this.
Then restart your network.

**How to restart the network..?**

The command for stop the network is `/etc/init.d/network stop`

To start the network `/etc/init.d/network start`

OR

``` bash
[root@localhost ~]# /etc/init.d/network restart
Shutting down interface eth0:                              [  OK  ]
Shutting down loopback interface:                          [  OK  ]
Bringing up loopback interface:                            [  OK  ]
Bringing up interface eth0:                                [  OK  ]
[root@localhost ~]#
```

**How to stop and start the firewall..?**

To stop `/etc/init.d/iptables stop`

To start `/etc/init.d/iptables start`

OR

``` bash
[root@localhost ~]# /etc/init.d/iptables restart
Flushing firewall rules:                                   [  OK  ]
Setting chains to policy ACCEPT: filter                    [  OK  ]
Unloading iptables modules:                                [  OK  ]
Applying iptables firewall rules:                          [  OK  ]
Loading additional iptables modules: ip_conntrack_netbios_n[  OK ]
[root@localhost ~]#
```

**How to view my networking information..?**

command for to view all the networking info \"ifconfig\"

``` bash
[root@localhost ~]# ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 00:16:3E:A0:00:06
inet addr:192.168.1.13  Bcast:192.168.1.255  Mask:255.255.255.0
inet6 addr: fe80::216:3eff:fea0:6/64 Scope:Link
UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
RX packets:1046 errors:0 dropped:0 overruns:0 frame:0
TX packets:297 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:1000
RX bytes:81732 (79.8 KiB)  TX bytes:37712 (36.8 KiB)
Interrupt:5 Base address:0x2000
[root@localhost ~]#
```

**How to add nameserver..?**

Add your nameserver (dns) /etc/resolv.conf like this.Here Airtel dns ip
is used.

``` bash
[root@localhost ~]# cat /etc/resolv.conf
; generated by /sbin/dhclient-script
nameserver 203.145.184.13
search localdomain
[root@localhost ~]#
```

**How to add Gateway and Hostname..?**

open the file `/etc/sysconfig/network`. Then add your gateway ip. For
the hostname change the HOSTNAME line by default this line is
localhost.localdomain. Then restart your network.

``` bash
[root@localhost ~]# cat /etc/sysconfig/network
NETWORKING=yes
NETWORKING_IPV6=no
HOSTNAME=yourdomain.com
GATEWAY=192.168.1.1
[root@localhost ~]#
```

OR

`route add -net 0.0.0.0 gw 192.168.1.1`

**How to add a service..?**

Copy your service shell script file to /etc/init.d folder. To add a
service.

`[root@localhost ~]# chkconfig -- add servicename`

To startup the service at the boot time.

`[root@localhost ~]# chkconfig --level 5 servicename on`
