Upgrade Samsung Galaxy 5 and 3 to Froyo
#######################################
:date: 2011-08-05 03:55
:author: arul
:category: Android
:tags: android, Mobile, Linux, how to
:slug: upgrade-samsung-galaxy-5-and-3-to-froyo

**How to Upgrade your android to 2.2**

|image0| 

Galaxy 5 and 3 with 2.2

I am going to give steps for how to updagrade your Samsung Galaxy 3 (GT-I5800) and Samsung Galaxy 5 (GT-I5503) phone OS Android 2.1 (Eclair) to Android 2.2 (Froyo). I tested these steps myself. So feel free to use. It will surely work for Asia / India users.

The Hardware Requirement are:

-  Windows PC.
-  Samsung Usb cable
-  Absolutely a Mobile either Galaxy 5 or 3

The Software Requirement are:

-  ODIN Multi Downloader.
-  OPS file
-  Firmware file

The OPS file and Firmware are varies depends upon your Handset. First download the required files.

**For Galaxy 5:**

* ODIN - `S5570\_Odin\_Multi\_Downloader\_v4.38.exe <http://bit.ly/1dTykIG>`__
* OPS file - `EUROPA\_v1.0.ops <http://bit.ly/1HRLlcZ>`__
* Firmware - `I5503DXJP8\_I5503DXJP7\_I5503OLBJP7.tar.gz <http://bit.ly/1AQYje3>`__

**For Galaxy 3:**

* ODIN - `S5570\_Odin\_Multi\_Downloader\_v4.38.exe <http://bit.ly/1dTykIG>`__
* OPS File - `apollo\_0531.zip <http://bit.ly/1Jy3DnL>`__
* Firmware - `I5801DDJP6\_I5801ODDJP6\_INU.zip <http://bit.ly/1F0PVn7>`__

Before start Backup your contacts and everything. Because Upgrade will delete everything from your mobile not from sd card.

|image1| 

Image of How to start mobile in downloading mode.

**Steps:**

-  Clean your existing data. Goto to Settings → Privacy → Factory data Reset
-  Remove your SIM and SD card
-  Run that ODIN exe. Some times it requires Admin privileges.
-  Power off your mobile. 
-  Start your mobile as Downloading mode. For that Press Volume Down + Home Button [Center Button] + Power Button
-  Connect to USB. Now ODIN detected your mobile in COM port.
-  Check the "One Package" Check box and Check all boxes in Options.
-  Select your OPS File.
-  Select your firmware. Extract that rar file and select tar file with in that.
-  Click start button.

|image2| 
How to setup / Settings

|image3|
Upgrading

It will automatically reboot after finish. Rebooting takes 5-10 min don't panic, please be patient. Then unplug your mobile. Yeah you are successfully upgraded to Froyo...!!

|image4|
Rebooting

|image5| 
Success .. Upgraded

Note: Click on the images for large view.

My configuration:

  - Windows 7 PC
  - ODIN v4.38
  - Galaxy 5 and Galaxy 3
  - I am from India

To find firmware and OPS for your mobile: http://www.samfirmware.com/fwandroid.htm

FAQ:
====

**After upgraded gprs is not working..?**

Setup manual APN settings or Delete your APN's and reset. It will 100% work. But I am not facing any wifi problem.

**My Phone is not detected..?**

Before start upgrading install USB driver for samsung. You can download from here http://goo.gl/223cK

**How to root my phone..?**

-  Download SuperOneClick latest version from `here <http://goo.gl/sD1KY>`__
-  Select Exploit as "GingerBreak"
-  Make sure you phone is detected
-  Press Root button

**Fix for samsung logo only showing..?**

Follow the same process before rebooting a recovery window displaying 3
options.

-  In that 3 First select "Clear your cache"
-  Then "Clear data and reset"
-  Finally select the option to reboot.

Now your phone not struct in samsung logo.

**How to upgraded to 2.3 ..?**

I have upgraded to 2.3.7 (CyanogenMod) by following this link \ http://t.co/4wI6FSmk

**How to upgraded to 4.0.4 ..?**

I have written a post to upgrade our Galaxy 5 to Android Ice Cream Sandwich \ http://www.arulraj.net/2012/07/upgrade-samsung-galaxy-5-to-ice-cream-sandwich.html

**How to go back to 2.1 ..?**

First you have to find your firmware version

|image6|

Firmware version

-  Go to Settings → About phone note down your baseband version
-  Try to get your firmware from internet. Or use this
   `I5503DDJG4 <http://hotfile.com/dl/123203814/82f0724/I5503DDJG4.rar.html>`__ ,
   `I5503DXJG5 <http://dl.dropbox.com/u/2710268/I5503DXJG5.rar>`__ 2.1
   firmware (Galaxy 5). Password for zip file is “samfirmware.com”
-  Use the same ODIN and OPS file and follow the same steps above.


.. |image0| image:: https://lh3.googleusercontent.com/-8yr0vIMYWGk/TjuxF4bMH5I/AAAAAAAAAqI/b_ar3tGzFeI/s400/Galaxy-5-and-3.jpg
   :target: https://lh3.googleusercontent.com/-8yr0vIMYWGk/TjuxF4bMH5I/AAAAAAAAAqI/b_ar3tGzFeI/s800/Galaxy-5-and-3.jpg
.. |image1| image:: http://4.bp.blogspot.com/-Xy--_q7QAfI/Tju1Fsh0G8I/AAAAAAAAAqQ/HOsRICq7kHk/s400/how-to-downloading-mode.png
   :target: http://4.bp.blogspot.com/-Xy--_q7QAfI/Tju1Fsh0G8I/AAAAAAAAAqQ/HOsRICq7kHk/s1600/how-to-downloading-mode.png
.. |image2| image:: http://3.bp.blogspot.com/-ADPkjhCvSks/Tju2uyxStfI/AAAAAAAAAqg/qwvekNHtxc0/s400/odin.png
   :target: http://3.bp.blogspot.com/-ADPkjhCvSks/Tju2uyxStfI/AAAAAAAAAqg/qwvekNHtxc0/s1600/odin.png
.. |image3| image:: http://1.bp.blogspot.com/-r3VzrjvkG58/Tju2StFZiqI/AAAAAAAAAqY/gS93DB7BPd0/s400/Downloading-Mode.jpg
   :target: http://1.bp.blogspot.com/-r3VzrjvkG58/Tju2StFZiqI/AAAAAAAAAqY/gS93DB7BPd0/s600/Downloading-Mode.jpg
.. |image4| image:: http://1.bp.blogspot.com/-BI0r3a1z9Z8/Tju7vUZ60sI/AAAAAAAAAq4/GPg_gQtKwZ4/s400/Android-Rebooting.jpg
   :target: http://1.bp.blogspot.com/-BI0r3a1z9Z8/Tju7vUZ60sI/AAAAAAAAAq4/GPg_gQtKwZ4/s600/Android-Rebooting.jpg
.. |image5| image:: http://3.bp.blogspot.com/-g_0juKi1KZU/Tju4M_1CRkI/AAAAAAAAAqw/RhZD479naBU/s400/galaxy-about-phone.png
   :target: http://3.bp.blogspot.com/-g_0juKi1KZU/Tju4M_1CRkI/AAAAAAAAAqw/RhZD479naBU/s600/galaxy-about-phone.png
.. |image6| image:: http://1.bp.blogspot.com/-I4YZL2v3Su8/T035soaNoqI/AAAAAAAANjY/QbvWlwCO5ik/s320/android+version.PNG
   :target: http://1.bp.blogspot.com/-I4YZL2v3Su8/T035soaNoqI/AAAAAAAANjY/QbvWlwCO5ik/s1600/android+version.PNG
