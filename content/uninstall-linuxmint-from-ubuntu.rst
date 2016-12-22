Uninstall linuxmint from ubuntu
###############################
:date: 2012-04-01 02:31
:author: arul
:category: Linux
:tags: gnome, Linux, ubuntu, how to
:slug: uninstall-linuxmint-from-ubuntu
:status: published
:disqus_identifier: /2012/04/uninstall-linuxmint-from-ubuntu.html

**How to uninstall linuxmint from ubuntu 11.10**

|image0| Gnome2 Linux mint desktop

First I explain the whole story.. 😄

**Why linuxmint in ubuntu...?**

In the latest Ubuntu 11.10 release canonical team upgraded from Gnome2 to Gnome3 and ubuntu unity as a default login shell. But I am not comfortable with unity and gnome3. Here its a good article about why I don't like this `read it <http://t.co/gukVNjKC>`__. So I need Gome2 back thats why I installed linuxmint shell a.k.a mate shell.

**How I installed linuxmint in my ubuntu..?**

Its simple. I followed this `tutorial <http://www.noobslab.com/2011/11/install-linux-mint-mate-desktop-on.html>`__.

**Now why you want to uninstall..?**

Now again, after installed mate shell facing some problems.

-  ubuntu software center is not working.
-  every gnome settings showing in two times.
-  ubuntu gnome2 and mate have lot of difference.

**Ok. How to unistall mate shell..?**

For everything you need sudo permission. Login in unity shell and open your terminal. Then run this command

.. code-block:: bash

  sudo apt-get autoremove mint-meta-mate

It will uninstall every thing related to linux mint. But still linux mint already changed many things in software repo. So you have to move back to old repo (ubuntu 11.10). For that run these commands

1. Remove linuxmint repo link from software list.

.. code-block:: bash

  sudo gedit /etc/apt/sources.list

2. Remove the old software list. Then move the software list to new directory and create a software list directory. For that follow the below commands.

.. code-block:: bash

  cd /var/lib/apt
  sudo mv lists lists.mate
  sudo mkdir -p lists/partial


3. Getting the ubuntu 11.10 repo

.. code-block:: bash

  sudo apt-get update
  sudo apt-get check
  sudo apt-get clean
  sudo apt-get autoclean
  sudo apt-get autoremove


After that also the ubuntu software center is not working 😞 . The problem is "no module named linuxmint". The reason for this error is every where the distribution id is linuxmint.

.. code-block:: bash

  lsb_release -a

it prints

.. code-block:: text

  Distributor ID: LinuxMint
  Description: Linux Mint 12 Fluxbox
  Release: 12
  Codename: lisa


4. Remove linuxmint distribution id from everywhere

.. code-block:: bash

  sudo gedit /etc/*release

and change everything in the file to:

.. code-block:: text

  DISTRIB_ID=Ubuntu
  DISTRIB_RELEASE=11.10
  DISTRIB_CODENAME=oneiric
  DISTRIB_DESCRIPTION="Ubuntu oneiric"

Then run

.. code-block:: bash

  sudo gedit /etc/*issue

and change to:

.. code-block:: bash

  Ubuntu 11.10 \n \l

5. Restart your machine. Then restart your machine. Now in the login screen you don't see the mate shell option.

Cheers....!!! 😃 😃 you are done...

.. |image0| image:: http://4.bp.blogspot.com/-4YPJxBzfGQY/T3gG3SAYouI/AAAAAAAAOPI/5liEnTA3mfc/s400/linuxmint.jpg
   :target: http://4.bp.blogspot.com/-4YPJxBzfGQY/T3gG3SAYouI/AAAAAAAAOPI/5liEnTA3mfc/s1600/linuxmint.jpg
