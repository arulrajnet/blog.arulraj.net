---
title: Hectic problem in ubuntu - resolved
date:   2010-12-23 14:07
author: arul
category:   Linux
tags:   Linux, ubuntu, how to
slug:   hectic-problem-in-ubuntu-resolved
disqus_identifier:    /2010/12/hectic-problem-in-ubuntu-resolved.html
---

**My Hectic problem in Ubuntu**

[![image0](http://3.bp.blogspot.com/_X5tq9y9xv2s/TKjoyGZNheI/AAAAAAAAAi8/5gH6PxD0DtY/s320/thinking+ubuntu.jpg)](http://3.bp.blogspot.com/_X5tq9y9xv2s/TKjoyGZNheI/AAAAAAAAAi8/5gH6PxD0DtY/s1600/thinking+ubuntu.jpg)

Here I will explain how to resolve hectic problems in ubuntu (that I
felt were tough). Here is the list of my problems.

1.  Number Lock not enabled when booting
2.  Brightness adjustment
3.  Tata photon+ data card problem
4.  Unauthorized resource when update﻿
5.  VLC problem
6.  GPG error: <http://ppa.launchpad.net> lucid Release: The following
    signatures couldn\'t be verified because the public key is not
    available: NO_PUBKEY D225991A72B194E5Failed
7.  Screen lock for root user
8.  \"P\"- Button in Acer 5740﻿﻿

Enable Numlock when boot..?

By default the Number lock is disabled. To enable Numlock when booting.

-   Install numlockx from your ubuntu software center
-   add the line shown below, at the End of File (before exit0)

| if \[ -x /usr/bin/numlockx \]; then
|  /usr/bin/numlockx on
|  fi

OR

You can add numlockx in startup ( System → Preferences → Startup
Applications).

<div class="separator" style="clear: both; text-align: center;">

[![image1](http://3.bp.blogspot.com/_X5tq9y9xv2s/TROcpK9B-OI/AAAAAAAAAlI/HsZmcQpuYlM/s400/numlockx%2Bstartup.png)](http://3.bp.blogspot.com/_X5tq9y9xv2s/TROcpK9B-OI/AAAAAAAAAlI/HsZmcQpuYlM/s1600/numlockx%2Bstartup.png)

</div>

But in this solution the num lock will turn on only after logged in.

| Brightness Adjustment ..?
|  In ubuntu there is a option to adjust the brightness. But no luck for
  me

Go to → Preferences → There is a option available for brightness
adjustment.

<div class="separator" style="clear: both; text-align: center;">

[![image2](http://1.bp.blogspot.com/_X5tq9y9xv2s/TROgOZn2wsI/AAAAAAAAAlQ/ObB8Azl-53E/s400/brightness%2Bpreference.png)](http://1.bp.blogspot.com/_X5tq9y9xv2s/TROgOZn2wsI/AAAAAAAAAlQ/ObB8Azl-53E/s1600/brightness%2Bpreference.png)

</div>

Tata Photon problem ..?

Tata Photon plus came with my laptop as a vendor compliment. When I
plugged the data card in my system, it was not detected, it was just
detected as memory card (as pen drive ). Here are the steps to fix for
this issue.

-   Download usbmodeswith from this
    [link](https://launchpad.net/ubuntu/+archive/primary/+files/usb-modeswitch_1.1.0-2_i386.deb)
    or you can download from ubuntu software center.
-   Run this \"lsusb\" and find Product and Vendor id respective to the
    \"Huawei Technologies Co., Ltd.\" for mine its like 12d1:1446 in
    that vendor id is 12d1 and product id is 1446
-   Goto this folder /etc/usb.modswitch.d/ then find the file with name
    \"12d1:1446\"
-   Add this 140b in TargetProductList in that file
-   Now run this command. \" usb_modeswitch -v VENDOR_ID -p PRODUCT_ID
    -M MESSAGE_CONTENT \". For mine \" usb_modeswitch -v 12d1 -p 1446 -M
    55534243123456780000000000000011060000000000000000000000000000 \"
-   Now the data card detected as modem.
-   To Check whether its detected as a modem run the lsusb command its
    changed to 12d1:140b

Ubuntu Software Center:

<div class="separator" style="clear: both; text-align: center;">

[![image3](http://4.bp.blogspot.com/_X5tq9y9xv2s/TROTxIvOYgI/AAAAAAAAAkg/pJs-ZiTCl5k/s400/usb%2Bmodeswitch-Ubuntu%2BSoftware%2BCenter.png)](http://4.bp.blogspot.com/_X5tq9y9xv2s/TROTxIvOYgI/AAAAAAAAAkg/pJs-ZiTCl5k/s1600/usb%2Bmodeswitch-Ubuntu%2BSoftware%2BCenter.png)

</div>

lsusb:

<div class="separator" style="clear: both; text-align: center;">

[![image4](http://4.bp.blogspot.com/_X5tq9y9xv2s/TROUuPlivVI/AAAAAAAAAko/7-msl5lSre8/s400/lsusb-terminal.png)](http://4.bp.blogspot.com/_X5tq9y9xv2s/TROUuPlivVI/AAAAAAAAAko/7-msl5lSre8/s1600/lsusb-terminal.png)

</div>

cat 12d1:1446:

<div class="separator" style="clear: both; text-align: center;">

[![image5](http://4.bp.blogspot.com/_X5tq9y9xv2s/TROW_nPIlKI/AAAAAAAAAkw/oE0PtAA5fTg/s400/cat%2B12d1%253A1446.png)](http://4.bp.blogspot.com/_X5tq9y9xv2s/TROW_nPIlKI/AAAAAAAAAkw/oE0PtAA5fTg/s1600/cat%2B12d1%253A1446.png)﻿

</div>

usb_modeswitch command:

<div class="separator" style="clear: both; text-align: center;">

[![image6](http://1.bp.blogspot.com/_X5tq9y9xv2s/TROZRYE6aKI/AAAAAAAAAk4/mQvDFEjblc0/s400/usb_modeswitch.png)](http://1.bp.blogspot.com/_X5tq9y9xv2s/TROZRYE6aKI/AAAAAAAAAk4/mQvDFEjblc0/s1600/usb_modeswitch.png)

</div>

To check:

<div class="separator" style="clear: both; text-align: center;">

[![image7](http://1.bp.blogspot.com/_X5tq9y9xv2s/TROaRxmEdkI/AAAAAAAAAlA/EuwPi7sXNZ8/s400/lsusb-to%2Bcheck.png)](http://1.bp.blogspot.com/_X5tq9y9xv2s/TROaRxmEdkI/AAAAAAAAAlA/EuwPi7sXNZ8/s1600/lsusb-to%2Bcheck.png)

</div>

The disadvantage is that,  you need to run this command every time you
plug in the card. Guys if you know a better solution comment here.

Unauthorized resource when update \...?

This error came when i was update my system using \"Update Manager\"
(System → Administration → Update Manager). Here are the steps to
resolve this issue

-   Goto System → Administration → Software Sources
-   Change that Download From Select Box to Main Server instead of Local
    Server (For mine Server From India)

<div class="separator" style="clear: both; text-align: center;">

[![image8](http://2.bp.blogspot.com/_X5tq9y9xv2s/TROQKMA4AnI/AAAAAAAAAkY/yF7J5SgkNok/s400/Screenshot-Software%2BSources.png)](http://2.bp.blogspot.com/_X5tq9y9xv2s/TROQKMA4AnI/AAAAAAAAAkY/yF7J5SgkNok/s1600/Screenshot-Software%2BSources.png)

</div>
<div class="separator" style="clear: both; text-align: left;">

VLC root user problem ..?

</div>
<div class="separator" style="clear: both; text-align: left;">

VLC is running fine for my other user. The only problem is that it could
not support for root user. Various forums say by default that VLC is
disabled for root user. If you want enable this you need to download the
source code and make a small change then rebuild and install. Too bad
\... :(

</div>
<div class="separator" style="clear: both; text-align: left;">

GPG Error ..?

</div>
<div class="separator" style="clear: both; text-align: left;">

I got this error when running my update manager. I don\'t know how this
error came and why my system is looking for the public key. Here are the
steps to fix the problem.

</div>
<div class="separator" style="clear: both; text-align: left;">

-   Run these commands in terminal

</div>

    gpg --keyserver keyserver.ubuntu.com --recv 72B194E5

    gpg --export --armor 72B194E5 | sudo apt-key add -

| Use these last 8 digits for any other keys . I referred from
  [here](http://ubuntuforums.org/showthread.php?t=1046158)
|  Screen lock for root user ..?

From my understanding from various forums, the screen lock for root user
is disabled in the linux kernal itself. But I found a message in the
screen saver itself. Here it is

<div style="clear: both; text-align: center;">

[![image9](http://4.bp.blogspot.com/_X5tq9y9xv2s/TROi8zrTKWI/AAAAAAAAAlY/Hrh7D2VwvbU/s400/root%2Bscreen%2Block.png)](http://4.bp.blogspot.com/_X5tq9y9xv2s/TROi8zrTKWI/AAAAAAAAAlY/Hrh7D2VwvbU/s1600/root%2Bscreen%2Block.png)

</div>
<div>

Warning: The screen will not be locked for the root user.

</div>
<div>

\"P\"- Button in Acer 5740﻿﻿ \...?

</div>
<div>

The \"P\" button in the top right corner of the keyboard. You may think
that this is the Power button or something else (Initially I  thought
the same .. :(  ) But there is no default task assigned for this button.
You can customize this button as you need. I am using this button as
Mute Button :) Here is the how to\...

</div>
<div class="separator" style="clear: both; text-align: center;">

[![image10](http://4.bp.blogspot.com/_X5tq9y9xv2s/TROlZQBhmvI/AAAAAAAAAlg/wCAcxLSVdIo/s400/acer%2B5740%2Bp%2Bbutton.jpg)](http://4.bp.blogspot.com/_X5tq9y9xv2s/TROlZQBhmvI/AAAAAAAAAlg/wCAcxLSVdIo/s1600/acer%2B5740%2Bp%2Bbutton.jpg)

</div>
<div>

-   Goto System → Preferences → Keyboard shortcuts
-   In the Sound tap you can set the New shortcut for Volume mute

</div>
<div>
<div class="separator" style="clear: both; text-align: center;">

[![image11](http://4.bp.blogspot.com/_X5tq9y9xv2s/TROnINJaJ3I/AAAAAAAAAlo/jYaYYMt3Xa0/s400/mute%2B-%2BKeyboard%2BShortcuts.png)](http://4.bp.blogspot.com/_X5tq9y9xv2s/TROnINJaJ3I/AAAAAAAAAlo/jYaYYMt3Xa0/s1600/mute%2B-%2BKeyboard%2BShortcuts.png)

</div>

Most of these problems are because of accessing as a **root user**. If 
I change the user it will be fixed. But most of my docs and software are
pre-configured with this user. I just want to disable my root account
and migrate from root to some other user.

My Configuration :

</div>

OS - Ubuntu 10.04

Login user - root

Machine - [Acer
5740](http://www.arulraj.net/2010/06/install-ubuntu-10-04-in-acer-5740.html)
