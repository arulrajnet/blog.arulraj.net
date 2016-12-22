Hectic problem in ubuntu - resolved
###################################
:date: 2010-12-23 14:07
:author: arul
:category: Linux
:tags: Linux, ubuntu, how to
:slug: hectic-problem-in-ubuntu-resolved
:disqus_identifier: /2010/12/hectic-problem-in-ubuntu-resolved.html

**My Hectic problem in Ubuntu**

|image0|

Here I will explain how to resolve hectic problems in ubuntu (that I
felt were tough). Here is the list of my problems.

#. Number Lock not enabled when booting
#. Brightness adjustment
#. Tata photon+ data card problem
#. Unauthorized resource when update﻿
#. VLC problem
#. GPG error: http://ppa.launchpad.net lucid Release: The following
   signatures couldn't be verified because the public key is not
   available: NO\_PUBKEY D225991A72B194E5Failed
#. Screen lock for root user
#. "P"- Button in Acer 5740﻿﻿

Enable Numlock when boot..?

By default the Number lock is disabled. To enable Numlock when booting.

-  Install numlockx from your ubuntu software center
-  add the line shown below, at the End of File (before exit0)

| if [ -x /usr/bin/numlockx ]; then
|  /usr/bin/numlockx on
|  fi

OR

You can add numlockx in startup ( System → Preferences → Startup
Applications).

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image1|

.. raw:: html

   </div>

But in this solution the num lock will turn on only after logged in.

| Brightness Adjustment ..?
|  In ubuntu there is a option to adjust the brightness. But no luck for
  me

Go to → Preferences → There is a option available for brightness
adjustment.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image2|

.. raw:: html

   </div>

Tata Photon problem ..?

Tata Photon plus came with my laptop as a vendor compliment. When I
plugged the data card in my system, it was not detected, it was just
detected as memory card (as pen drive ). Here are the steps to fix for
this issue.

-  Download usbmodeswith from this
   `link <https://launchpad.net/ubuntu/+archive/primary/+files/usb-modeswitch_1.1.0-2_i386.deb>`__
   or you can download from ubuntu software center.
-  Run this "lsusb" and find Product and Vendor id respective to the
   "Huawei Technologies Co., Ltd." for mine its like 12d1:1446 in that
   vendor id is 12d1 and product id is 1446
-  Goto this folder /etc/usb.modswitch.d/ then find the file with name
   "12d1:1446"
-  Add this 140b in TargetProductList in that file
-  Now run this command. " usb\_modeswitch -v VENDOR\_ID -p PRODUCT\_ID
   -M MESSAGE\_CONTENT ". For mine " usb\_modeswitch -v 12d1 -p 1446 -M
   55534243123456780000000000000011060000000000000000000000000000 "
-  Now the data card detected as modem.
-  To Check whether its detected as a modem run the lsusb command its
   changed to 12d1:140b

Ubuntu Software Center:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image3|

.. raw:: html

   </div>

lsusb:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image4|

.. raw:: html

   </div>

cat 12d1:1446:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image5|\ ﻿

.. raw:: html

   </div>

usb\_modeswitch command:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image6|

.. raw:: html

   </div>

To check:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image7|

.. raw:: html

   </div>

The disadvantage is that,  you need to run this command every time you
plug in the card. Guys if you know a better solution comment here.

Unauthorized resource when update ...?

This error came when i was update my system using "Update Manager"
(System → Administration → Update Manager). Here are the steps to
resolve this issue

-  Goto System → Administration → Software Sources
-  Change that Download From Select Box to Main Server instead of Local
   Server (For mine Server From India)

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image8|

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

VLC root user problem ..?

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

VLC is running fine for my other user. The only problem is that it could
not support for root user. Various forums say by default that VLC is
disabled for root user. If you want enable this you need to download the
source code and make a small change then rebuild and install. Too bad
... :(

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

GPG Error ..?

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

I got this error when running my update manager. I don't know how this
error came and why my system is looking for the public key. Here are the
steps to fix the problem.

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

-  Run these commands in terminal

.. raw:: html

   </div>

::

    gpg --keyserver keyserver.ubuntu.com --recv 72B194E5

::

    gpg --export --armor 72B194E5 | sudo apt-key add -

| Use these last 8 digits for any other keys . I referred from
  `here <http://ubuntuforums.org/showthread.php?t=1046158>`__
|  Screen lock for root user ..?

From my understanding from various forums, the screen lock for root user
is disabled in the linux kernal itself. But I found a message in the
screen saver itself. Here it is

.. raw:: html

   <div style="clear: both; text-align: center;">

|image9|

.. raw:: html

   </div>

.. raw:: html

   <div>

Warning: The screen will not be locked for the root user.

.. raw:: html

   </div>

.. raw:: html

   <div>

"P"- Button in Acer 5740﻿﻿ ...?

.. raw:: html

   </div>

.. raw:: html

   <div>

The "P" button in the top right corner of the keyboard. You may think
that this is the Power button or something else (Initially I  thought
the same .. :(  ) But there is no default task assigned for this button.
You can customize this button as you need. I am using this button as
Mute Button :) Here is the how to...

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image10|

.. raw:: html

   </div>

.. raw:: html

   <div>

-  Goto System → Preferences → Keyboard shortcuts
-  In the Sound tap you can set the New shortcut for Volume mute

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image11|

.. raw:: html

   </div>

Most of these problems are because of accessing as a **root user**. If 
I change the user it will be fixed. But most of my docs and software are
pre-configured with this user. I just want to disable my root account
and migrate from root to some other user.

My Configuration :

.. raw:: html

   </div>

OS - Ubuntu 10.04

Login user - root

Machine - `Acer
5740 <http://www.arulraj.net/2010/06/install-ubuntu-10-04-in-acer-5740.html>`__

.. |image0| image:: http://3.bp.blogspot.com/_X5tq9y9xv2s/TKjoyGZNheI/AAAAAAAAAi8/5gH6PxD0DtY/s320/thinking+ubuntu.jpg
   :target: http://3.bp.blogspot.com/_X5tq9y9xv2s/TKjoyGZNheI/AAAAAAAAAi8/5gH6PxD0DtY/s1600/thinking+ubuntu.jpg
.. |image1| image:: http://3.bp.blogspot.com/_X5tq9y9xv2s/TROcpK9B-OI/AAAAAAAAAlI/HsZmcQpuYlM/s400/numlockx%2Bstartup.png
   :target: http://3.bp.blogspot.com/_X5tq9y9xv2s/TROcpK9B-OI/AAAAAAAAAlI/HsZmcQpuYlM/s1600/numlockx%2Bstartup.png
.. |image2| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/TROgOZn2wsI/AAAAAAAAAlQ/ObB8Azl-53E/s400/brightness%2Bpreference.png
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/TROgOZn2wsI/AAAAAAAAAlQ/ObB8Azl-53E/s1600/brightness%2Bpreference.png
.. |image3| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TROTxIvOYgI/AAAAAAAAAkg/pJs-ZiTCl5k/s400/usb%2Bmodeswitch-Ubuntu%2BSoftware%2BCenter.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TROTxIvOYgI/AAAAAAAAAkg/pJs-ZiTCl5k/s1600/usb%2Bmodeswitch-Ubuntu%2BSoftware%2BCenter.png
.. |image4| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TROUuPlivVI/AAAAAAAAAko/7-msl5lSre8/s400/lsusb-terminal.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TROUuPlivVI/AAAAAAAAAko/7-msl5lSre8/s1600/lsusb-terminal.png
.. |image5| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TROW_nPIlKI/AAAAAAAAAkw/oE0PtAA5fTg/s400/cat%2B12d1%253A1446.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TROW_nPIlKI/AAAAAAAAAkw/oE0PtAA5fTg/s1600/cat%2B12d1%253A1446.png
.. |image6| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/TROZRYE6aKI/AAAAAAAAAk4/mQvDFEjblc0/s400/usb_modeswitch.png
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/TROZRYE6aKI/AAAAAAAAAk4/mQvDFEjblc0/s1600/usb_modeswitch.png
.. |image7| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/TROaRxmEdkI/AAAAAAAAAlA/EuwPi7sXNZ8/s400/lsusb-to%2Bcheck.png
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/TROaRxmEdkI/AAAAAAAAAlA/EuwPi7sXNZ8/s1600/lsusb-to%2Bcheck.png
.. |image8| image:: http://2.bp.blogspot.com/_X5tq9y9xv2s/TROQKMA4AnI/AAAAAAAAAkY/yF7J5SgkNok/s400/Screenshot-Software%2BSources.png
   :target: http://2.bp.blogspot.com/_X5tq9y9xv2s/TROQKMA4AnI/AAAAAAAAAkY/yF7J5SgkNok/s1600/Screenshot-Software%2BSources.png
.. |image9| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TROi8zrTKWI/AAAAAAAAAlY/Hrh7D2VwvbU/s400/root%2Bscreen%2Block.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TROi8zrTKWI/AAAAAAAAAlY/Hrh7D2VwvbU/s1600/root%2Bscreen%2Block.png
.. |image10| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TROlZQBhmvI/AAAAAAAAAlg/wCAcxLSVdIo/s400/acer%2B5740%2Bp%2Bbutton.jpg
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TROlZQBhmvI/AAAAAAAAAlg/wCAcxLSVdIo/s1600/acer%2B5740%2Bp%2Bbutton.jpg
.. |image11| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TROnINJaJ3I/AAAAAAAAAlo/jYaYYMt3Xa0/s400/mute%2B-%2BKeyboard%2BShortcuts.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TROnINJaJ3I/AAAAAAAAAlo/jYaYYMt3Xa0/s1600/mute%2B-%2BKeyboard%2BShortcuts.png
