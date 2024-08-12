---
title: How to create and use private / public keys
date: 2009-07-23 06:27
author: arul
category: Linux
tags: commands,Linux,Programming,how-to
slug: how-to-create-and-use-private-public-keys
disqus_identifier: /2009/07/how-to-create-and-use-private-public-keys.html
status: published
---

[![image0](http://2.bp.blogspot.com/_Tq9uaJI0Xww/SmhV6r4dTlI/AAAAAAAAFIM/74M6AzeYa_w/s400/puttygen.jpg)](http://2.bp.blogspot.com/_Tq9uaJI0Xww/SmhV6r4dTlI/AAAAAAAAFIM/74M6AzeYa_w/s1600-h/puttygen.jpg)

Hi all,

Here the document for how to create private and public keys for login.
This is more helpful others can login to your machine without disclose
the password.

**How to create private key for my machine..?**

Go to /home/root/.ssh folder. Then run ssh-keygen command. Answer the
questions. Then the key and pub files are created. save this .pub file
as authorized_keys.

``` bash
[root@localhost ~]# cd .ssh/
[root@localhost .ssh]# ls
known_hosts
[root@localhost .ssh]# ssh-key
ssh-keygen ssh-keyscan
[root@localhost .ssh]# ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): example.ppk
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in example.ppk.
Your public key has been saved in example.pub.
The key fingerprint is:
6e:e4:ff:3b:a6:52:0d:57:ec:d2:f8:dd:e5:08:22:d6 root@localhost
[root@localhost .ssh]# cat example.pub >> authorized_keys
[root@localhost .ssh]# ls
authorized_keys example.ppk example.pub known_hosts
```

**How to use the private keys..?**

*In putty*

-   Open putty and type the \'Host Name\' (ie <root@192.168.1.117>)
-   Give a name in \'Saved Session\'
-   Select Connection \--\> SSH \--\> Auth \--\> Browse \--\> Select the
    corresponding \*.ppk file (ie example.ppk)
-   Now go to \'Session\' Just click \'Save Button\'

Now you can login to your machine without password in putty. For putty
and puttygen
[download](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)

*In Win-SCP*

-   Start WinSCP. Under Session, enter the Host
    name(<root@192.168.1.117>), User name(root), and Private key
    file(\*.ppk) and click \'Save\'.

Now you can login to your machine without password in WinSCP.

[![image1](http://1.bp.blogspot.com/_Tq9uaJI0Xww/SmhWF1yTZXI/AAAAAAAAFIU/CEsMmDSIw6U/s400/privatekey.jpg)](http://1.bp.blogspot.com/_Tq9uaJI0Xww/SmhWF1yTZXI/AAAAAAAAFIU/CEsMmDSIw6U/s1600-h/privatekey.jpg)

*In SCP Command*

``` bash
scp -i example.ppk test.jpg root@192.168.1.117:/home/root/
```

*In SSH Command*

``` bash
ssh -i example.ppk root@192.168.1.117
```
