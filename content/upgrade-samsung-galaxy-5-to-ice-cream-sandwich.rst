Upgrade Samsung Galaxy 5 to Ice Cream Sandwich
##############################################
:date: 2012-07-26 14:54
:author: arul
:category: Android
:tags: android, hacking, How to, Mobile
:slug: upgrade-samsung-galaxy-5-to-ice-cream-sandwich
:status: published

**How to upgrade to Android 4.0.4**

[caption id="" align="aligncenter" width="400"]\ |image0| Android 4.0.4
for Galaxy 5[/caption]

This time I come with Android 4.0.4 (Ice Cream Sandwich). Hope you are
all already upgraded your galaxy to Froyo by following
my earlier \ `post <http://www.arulraj.net/2011/08/upgrade-samsung-galaxy-5-and-3-to-froyo.html>`__\ .
Others no worries its the time for 4.0.4. The upgradation of 4.0.4 is
much easier than earlier and no more complicated steps.

Important:

This is not a official firmware from samsung like 2.2. Its created
by \ `CyanogenMod <http://en.wikipedia.org/wiki/CyanogenMod>`__.
I personally tested myself in my mobile most of the things works fine so
feel free to use.

Requirements:

-  A windows PC
-  USB cable
-  Samsung Galaxy 5 (GT-I5503) mobile :)

Download the below files.

.. raw:: html

   <div style="padding-left: 30px;">

ODIN
– `S5570\_Odin\_Multi\_Downloader\_v4.38.exe <http://goo.gl/ba7Pj>`__
OPS file – `EUROPA\_v1.0.ops <http://goo.gl/00kbE>`__

.. raw:: html

   </div>

.. raw:: html

   <div style="padding-left: 30px;">

ClockworkMod Recovery
– `recovery-clockwork-5.5.0.4-galaxy5.tar <http://goo.gl/O3pjc>`__

.. raw:: html

   </div>

.. raw:: html

   <div style="padding-left: 30px;">

Firmware 4.0.4
– `update-cm-9-20120608-MADTEAM-galaxy5-signed.zip <http://goo.gl/JVUek>`__

.. raw:: html

   </div>

.. raw:: html

   <div style="padding-left: 30px;">

Google apps – \ `gapps-ics-small-20120429.zip <http://goo.gl/jRYD8>`__

.. raw:: html

   </div>

Before start Backup your contacts and everything. Because Upgrade will
delete everything from your mobile not from sd card. There are two phase

.. raw:: html

   <div>

#. Boot your mobile in recovery mode
#. Install firmware and Google Apps

.. raw:: html

   <div>

**Clockworkmod Recovery:**

.. raw:: html

   </div>

.. raw:: html

   <div style="padding-left: 30px;">

For this you need ODIN and recovery-clockwork-5.5.0.4-galaxy5.tar.

.. raw:: html

   </div>

.. raw:: html

   <div style="padding-left: 30px;">

[caption id="" align="alignnone" width="325"]\ |image1| How to
Downloading mode[/caption]

Steps:

-  Copy Firmware and Google Apps files to your sd card. We will use that
   in next phase.
-  Power off your mobile and Start your mobile in downloading mode.  For
   that Press Volume Down + Home Button [Center Button] + Power Button.
-  Run that ODIN exe.
-  Connect to USB. Now ODIN detected your mobile in COM port.
-  Check the “One Package” Check box and Check all boxes in Options.
-  Select your OPS File.
-  Select recovery-clockwork-5.5.0.4-galaxy5.tar
-  Press Start button

.. raw:: html

   <div>

[caption id="" align="aligncenter" width="600"]\ |image2| ODIN for
recovery[/caption]

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Now your mobile is automatically restart. It will show you a recovery
screen. Phase 2 starts

**Install Firmware and Google Apps:**

.. raw:: html

   <div>

[caption id="" align="aligncenter" width="300"]\ |image3| ClockworkMod
Recovery Screen[/caption]

.. raw:: html

   </div>

.. raw:: html

   <div>

**Steps:**

.. raw:: html

   </div>

.. raw:: html

   <div>

-  Cleanup

   -  Center button to select an option. Arrow keys for move up and down
   -  Select wipe data/factory reset
   -  A new screen will come. Press / Select yes.
   -  Back to main menu [press back button]
   -  Select Advanced
   -  Select Wipe Dalvik Cache
   -  Press Yes
   -  Select Wipe Battery Stats
   -  Press Yes
   -  Back to main menu

-  Install Firmware

   -  Select Install zip from sd card
   -  Select Choose a zip file
   -  Select update-cm-9-20120608-MADTEAM-galaxy5-signed.zip from your
      sd card.
   -  Press yes

-  Install Google Apps

   -  Again Select Install zip from sd card
   -  Select Choose a zip file
   -  Select gapps-ics-small-20120429.zip from your sd card
   -  Press yes

-  Final

   -  Important. Select Wipe cache partition
   -  Press yes
   -  Back to main menu
   -  Select reboot system now.

-  You are done... First time boot takes more time. So Don't Panic

.. raw:: html

   </div>

.. raw:: html

   <div>

Images:

.. raw:: html

   </div>

.. raw:: html

   <div>

[caption id="" align="alignnone" width="400"]\ |image4| Cleanup -
Advanced - Wipe Dalvik and Battery stats[/caption]

.. raw:: html

   </div>

.. raw:: html

   <div>

[caption id="" align="alignnone" width="400"]\ |image5| Install Firmware
from zip[/caption]

.. raw:: html

   </div>

[caption id="" align="alignnone" width="400"]\ |image6| Install Google
apps from zip[/caption]

.. raw:: html

   <div>

[caption id="" align="alignnone" width="400"]\ |image7| Ice Cream
Sandwich in Galaxy 5[/caption]

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

** FAQ:**

.. raw:: html

   </div>

Most of the default applications are not available..?

Yes. Most common application like Gmail, Maps, youtube are not there.
You need to download and install from market.

.. raw:: html

   <div>

.. raw:: html

   </div>

I want to root my phone..?

No need. By default its rooted :)

.. raw:: html

   <div>

.. raw:: html

   </div>

After upgraded FM is not working..?

This is a bug in this firmware.

.. raw:: html

   <div>

.. raw:: html

   </div>

How to revert back to Original..?

Simple. Follow this post \ http://www.arulraj.net/?p=372

ref: \ `http://madteam.co/news/2012/05/guide-cyanogenmod-installation-guide-for-galaxy-5/ <http://goo.gl/dZQtg>`__

update 11th Sep 2012:

-  Firmware download links updated
-  For latest Google apps \ http://goo.im/gapps/

.. |image0| image:: http://4.bp.blogspot.com/-ubNe_i_2S3Q/UBGDTVHDS_I/AAAAAAAAS60/WjUA-mBXfbI/s400/overview.jpg
   :target: http://4.bp.blogspot.com/-ubNe_i_2S3Q/UBGDTVHDS_I/AAAAAAAAS60/WjUA-mBXfbI/s1600/overview.jpg
.. |image1| image:: http://1.bp.blogspot.com/-c_aKPHUAY3M/UBGcZRa8UVI/AAAAAAAAS8k/erOgo5_QBqo/s400/how-to-downloading-mode_new.png
   :target: http://1.bp.blogspot.com/-c_aKPHUAY3M/UBGcZRa8UVI/AAAAAAAAS8k/erOgo5_QBqo/s1600/how-to-downloading-mode_new.png
.. |image2| image:: http://3.bp.blogspot.com/-caKtsKjPWQc/UBGPQpLF7WI/AAAAAAAAS74/IFyshkeV2Lw/s600/odin.jpg
   :target: http://3.bp.blogspot.com/-caKtsKjPWQc/UBGPQpLF7WI/AAAAAAAAS74/IFyshkeV2Lw/s1600/odin.jpg
.. |image3| image:: http://4.bp.blogspot.com/-7bqJGC7any0/UBGfl0ztpLI/AAAAAAAAS80/KUe4L8Y53vg/s400/recovery_screen.jpg
   :target: http://4.bp.blogspot.com/-7bqJGC7any0/UBGfl0ztpLI/AAAAAAAAS80/KUe4L8Y53vg/s1600/recovery_screen.jpg
.. |image4| image:: http://2.bp.blogspot.com/-6onAhKek8Wg/UBGmADWKzUI/AAAAAAAAS9E/UBRhDZeM9Kw/s400/advanced_wipe.png
   :target: http://2.bp.blogspot.com/-6onAhKek8Wg/UBGmADWKzUI/AAAAAAAAS9E/UBRhDZeM9Kw/s1600/advanced_wipe.png
.. |image5| image:: http://3.bp.blogspot.com/-2-CX0shKmk0/UBGrVCcnefI/AAAAAAAAS9c/guF7BFQYX5Q/s400/install_firmware.png
   :target: http://3.bp.blogspot.com/-2-CX0shKmk0/UBGrVCcnefI/AAAAAAAAS9c/guF7BFQYX5Q/s1600/install_firmware.png
.. |image6| image:: http://1.bp.blogspot.com/-qFo9ciN0FY4/UBGt-geXKPI/AAAAAAAAS9w/ANGwNbeOIVo/s400/install_gapps.png
   :target: http://1.bp.blogspot.com/-qFo9ciN0FY4/UBGt-geXKPI/AAAAAAAAS9w/ANGwNbeOIVo/s1600/install_gapps.png
.. |image7| image:: http://2.bp.blogspot.com/-LtZJwFaNgQQ/UBGUoKLCc_I/AAAAAAAAS8Q/2pcPHdYuSK0/s400/android4.png
   :target: http://2.bp.blogspot.com/-LtZJwFaNgQQ/UBGUoKLCc_I/AAAAAAAAS8Q/2pcPHdYuSK0/s1600/android4.png
