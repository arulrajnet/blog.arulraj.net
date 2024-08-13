---
title: Automount vmware shared folder in ubuntu
date:   2013-09-16 13:19
author: arul
category:   Virtualization
tags:   fix, ubuntu, vmware, linux, how-to
slug:   automount-vmware-shared-folder-in-ubuntu
status:   published
disqus_identifier:    /2013/09/automount-vmware-shared-folder-in-ubuntu.html
---

**How to fix shared folder automount problem in vmware ..?**

I am using vmware player for last several years. But I am not tested
their shared folder features. To share your host os folder with vm you
have to install \"vmware tools\" on guest os. Installing vmware tools is
very simple.

**Checking vmware module :**

``` bash
sudo lsmod | grep vmhgfs
```

It should return some values something like shown on image.

[![lsmode](http://1.bp.blogspot.com/-scGjIUU5lA4/UjdQ4ODFgPI/AAAAAAAAVYA/M6Dqv5mdewQ/s320/lsmode.PNG)](http://1.bp.blogspot.com/-scGjIUU5lA4/UjdQ4ODFgPI/AAAAAAAAVYA/M6Dqv5mdewQ/s1600/lsmode.PNG)
List modules

If not you have to install vmware tools.

**Installing vmware tools :**

-   Goto Player → Manage → Install vmware Tools . Now Vmware Tools is
    mounted as CDROM with in VM

[![vmware tools
install](http://1.bp.blogspot.com/-ThUF8cYzXf8/UjdSbEfZR8I/AAAAAAAAVYM/FP45AmtYzFk/s320/install-vmware.png)](http://1.bp.blogspot.com/-ThUF8cYzXf8/UjdSbEfZR8I/AAAAAAAAVYM/FP45AmtYzFk/s1600/install-vmware.png)
Install VMware Tools

-   Extract Your VmwareTools-9.2.0-799703.tar.gz file to somewhere.
-   Goto \"vmware-tools-distrib\" folder path in terminal
-   Then run this command \"./vmware-install.pl\"
-   Just press enter for all the questions asked while installing

[![Install
vmware](http://4.bp.blogspot.com/-3LuB2o5GXbw/UjdUj2GiMoI/AAAAAAAAVYY/8cVWCD4isVc/s320/vmware-install.PNG)](http://4.bp.blogspot.com/-3LuB2o5GXbw/UjdUj2GiMoI/AAAAAAAAVYY/8cVWCD4isVc/s1600/vmware-install.PNG)
Vmware Install

**Add shared folder for VM:**

-   Goto Player → Manage → Virtual Machine Settings
-   In Options tab you can find the Shared Folders

[![image3](http://2.bp.blogspot.com/-y4FssiiprlQ/UjdWjo36pyI/AAAAAAAAVYk/7k6y22KWeb4/s320/vmware-settings.PNG)](http://2.bp.blogspot.com/-y4FssiiprlQ/UjdWjo36pyI/AAAAAAAAVYk/7k6y22KWeb4/s1600/vmware-settings.PNG)
Shared Folder

-   Then reboot your machine

**Auto mount shared folder on startup:**

Finally I came back to point. After restarted the shared folder are not
shown with in \"/mnt/hgfs/\" folder. So here is the fix for that.

There is a startup script called \"open-vm-tools\" with in /etc/init.d/
folder. Just add the below line in the start function.

``` bash
mount -t vmhgfs .host:/ /mnt/hgfs
```

Then restart the service \"sudo service open-vm-tools restart\".

[![image4](http://2.bp.blogspot.com/-pDdUDIjTvY0/UjdYEkE7QwI/AAAAAAAAVYw/oFb1zARhXrA/s320/vmware-initd.PNG)](http://2.bp.blogspot.com/-pDdUDIjTvY0/UjdYEkE7QwI/AAAAAAAAVYw/oFb1zARhXrA/s1600/vmware-initd.PNG)
open-vm-tools startup

**My Environmental :**

| Product : Vmware Player version 5.0.0 build-812388
| Vmware Tools: VmwareTools-9.2.0-799703
| Guest OS : Ubuntu 12.04 LTS 32 bit
| Host OS : Windows 7 64 bit
