Upgrade Samsung Galaxy 5 to Ice Cream Sandwich
##############################################
:date: 2012-07-26 14:54
:author: arul
:category: Android
:tags: android, hacking, How to, Mobile
:slug: upgrade-samsung-galaxy-5-to-ice-cream-sandwich
:status: published
:disqus_identifier: /2012/07/upgrade-samsung-galaxy-5-to-ice-cream-sandwich.html

**How to upgrade to Android 4.0.4**

|image0|

This time I come with Android 4.0.4 (Ice Cream Sandwich). Hope you are all already upgraded your galaxy to Froyo by following my earlier \ `post <http://www.arulraj.net/2011/08/upgrade-samsung-galaxy-5-and-3-to-froyo.html>`__\ . Others no worries its the time for 4.0.4. The upgradation of 4.0.4 is much easier than earlier and no more complicated steps.

**Important:**

This is not a official firmware from samsung like 2.2. Its created by `CyanogenMod <http://en.wikipedia.org/wiki/CyanogenMod>`__. I personally tested myself in my mobile most of the things works fine so feel free to use.

**Requirements:**

-  A windows PC
-  USB cable
-  Samsung Galaxy 5 (GT-I5503) mobile 😄

Download the below files.

* ODIN – `S5570\_Odin\_Multi\_Downloader\_v4.38.exe <http://bit.ly/1dTykIG>`__

* OPS file – `EUROPA\_v1.0.ops <http://bit.ly/1HRLlcZ>`__

* ClockworkMod Recovery – `recovery-clockwork-5.5.0.4-galaxy5.tar <http://bit.ly/1KLcKR0>`__

* Firmware 4.0.4 – `update-cm-9-20120608-MADTEAM-galaxy5-signed.zip <http://bit.ly/1F0MLQi>`__

* Google apps – `gapps-ics-small-20120429.zip <http://bit.ly/1dTyNuC>`__

Before start Backup your contacts and everything. Because Upgrade will delete everything from your mobile not from sd card. 

There are two phase

#. Boot your mobile in recovery mode
#. Install firmware and Google Apps


**Clockworkmod Recovery:**

For this you need ODIN and recovery-clockwork-5.5.0.4-galaxy5.tar.

|image1|

Steps:
------

-  Copy Firmware and Google Apps files to your sd card. We will use that in next phase.
-  Power off your mobile and Start your mobile in downloading mode.  For that Press Volume Down + Home Button [Center Button] + Power Button.
-  Run that ODIN exe.
-  Connect to USB. Now ODIN detected your mobile in COM port.
-  Check the “One Package” Check box and Check all boxes in Options.
-  Select your OPS File.
-  Select :code:`recovery-clockwork-5.5.0.4-galaxy5.tar`
-  Press Start button

|image2|

Now your mobile is automatically restart. It will show you a recovery screen. 

Phase 2 starts

**Install Firmware and Google Apps:**

|image3|

**Steps:**

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
   -  Select :code:`update-cm-9-20120608-MADTEAM-galaxy5-signed.zip` from your sd card.
   -  Press yes

-  Install Google Apps

   -  Again Select Install zip from sd card
   -  Select Choose a zip file
   -  Select :code:`gapps-ics-small-20120429.zip` from your sd card
   -  Press yes

-  Final

   -  Important. Select Wipe cache partition
   -  Press yes
   -  Back to main menu
   -  Select reboot system now.

-  You are done... First time boot takes more time. So Don't Panic

Images:


Image of Cleanup - Advanced - Wipe Dalvik and Battery stats

|image4|

Install Firmware from zip

|image5|

Install Google apps from zip

|image6|

Ice Cream Sandwich in Galaxy 5

|image7|

FAQ:
====

**Most of the default applications are not available..?**

Yes. Most common application like Gmail, Maps, youtube are not there.
You need to download and install from market.

**I want to root my phone..?**

No need. By default its rooted :)

**After upgraded FM is not working..?**

This is a bug in this firmware.

**How to revert back to Original..?**

Simple. Follow this post http://www.arulraj.net/2011/08/upgrade-samsung-galaxy-5-and-3-to-froyo.html

Reference: \ `http://madteam.co/news/2012/05/guide-cyanogenmod-installation-guide-for-galaxy-5/ <http://goo.gl/dZQtg>`__

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
