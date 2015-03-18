Uninstall linuxmint from ubuntu
###############################
:date: 2012-04-01 02:31
:author: arul
:category: Linux
:tags: gnome, Linux, ubuntu, how to
:slug: uninstall-linuxmint-from-ubuntu
:status: published

**How to uninstall linuxmint from ubuntu 11.10**

[caption id="" align="aligncenter" width="400" caption="Gnome2 Linux
mint desktop"]\ |image0|\ [/caption]

First I explain the whole story.. :)

| **Why linuxmint in ubuntu...?**
|  In the latest Ubuntu 11.10 release canonical team upgraded from
  Gnome2 to Gnome3 and ubuntu unity as a default login shell. But I am
  not comfortable with unity and gnome3. Here its a good article about
  why I don't like this `read it <http://t.co/gukVNjKC>`__. So I need
  Gome2 back thats why I installed linuxmint shell a.k.a mate shell.

| **How I installed linuxmint in my ubuntu..?**
|  Its simple. I followed this
  `tutorial <http://www.noobslab.com/2011/11/install-linux-mint-mate-desktop-on.html>`__.

| **Now why you want to uninstall..?**
|  Now again, after installed mate shell facing some problems.

-  ubuntu software center is not working.
-  every gnome settings showing in two times.
-  ubuntu gnome2 and mate have lot of difference.

| **Ok. How to unistall mate shell..?**
|  For everything you need sudo permission. Login in unity shell and
  open your terminal. Then run this command
|  [bash]
|  sudo apt-get autoremove mint-meta-mate
|  [/bash]
|  It will uninstall every thing related to linux mint. But still linux
  mint already changed many things in software repo. So you have to move
  back to old repo (ubuntu 11.10). For that run these commands

| 1. Remove linuxmint repo link from software list.
|  [bash]
|  sudo gedit /etc/apt/sources.list
|  [/bash]

| 2. Remove the old software list.
|  Then move the software list to new directory and create a software
  list directory. For that follow the below commands
|  [bash]
|  cd /var/lib/apt
|  sudo mv lists lists.mate
|  sudo mkdir -p lists/partial
|  [/bash]

| 3. Getting the ubuntu 11.10 repo
|  [bash]
|  sudo apt-get update
|  sudo apt-get check
|  sudo apt-get clean
|  sudo apt-get autoclean
|  sudo apt-get autoremove
|  [/bash]
|  After that also the ubuntu software center is not working :( . The
  problem is "no module named linuxmint". The reason for this error is
  every where the distribution id is linuxmint.
|  [bash]
|  lsb\_release -a
|  [/bash]
|  it prints
|  [text]
|  Distributor ID: LinuxMint
|  Description: Linux Mint 12 Fluxbox
|  Release: 12
|  Codename: lisa
|  [/text]
|  4. Remove linuxmint distribution id from everywhere
|  [bash]
|  sudo gedit /etc/\*release
|  [/bash]
|  and change everything in the file to:
|  [text]
|  DISTRIB\_ID=Ubuntu
|  DISTRIB\_RELEASE=11.10
|  DISTRIB\_CODENAME=oneiric
|  DISTRIB\_DESCRIPTION="Ubuntu oneiric"
|  [/text]
|  Then run
|  [bash]
|  sudo gedit /etc/\*issue
|  [/bash]
|  and change to:
|  [text]
|  Ubuntu 11.10 \\n \\l
|  [/text]
|  5. Restart your machine.
|  Then restart your machine. Now in the login screen you don't see the
  mate shell option.

Cheers....!!! :D :D you are done...

.. |image0| image:: http://4.bp.blogspot.com/-4YPJxBzfGQY/T3gG3SAYouI/AAAAAAAAOPI/5liEnTA3mfc/s400/linuxmint.jpg
   :target: http://4.bp.blogspot.com/-4YPJxBzfGQY/T3gG3SAYouI/AAAAAAAAOPI/5liEnTA3mfc/s1600/linuxmint.jpg
