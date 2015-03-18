Google chrome Download video
############################
:date: 2011-03-19 14:06
:author: arul
:category: Browser
:tags: Browser, hacking, ubuntu, Flash, Linux
:slug: google-chrome-download-video

The most video content web sites use flash player as them video
player. In Linux you can download streaming videos without any third
party tools. Previously the videos which you are watching by default its
stored in /tmp directory. You can copy the video from there. But in the
google chrome or Chromium browser by default its come with a flash
player. If you using that flash player the video is not downloaded in
/tmp directory. They are using there own intelligence to prevent this.
Here we are going to see a simple hack to download videos in google
chrome . Steps are

-  Goto installed plugins \ about:plugins in chrome / mozilla
-  Click Details to view with more information. Disable the Flash
   Plugin. The Location of the plugin would be
   "/usr/lib/adobe-flashplugin/libflashplayer.so"
-  Download the tar.gz version of flash player from
   here \ http://get.adobe.com/flashplayer/
-  Extract that file and copy the libflashplayer.so
   to /usr/lib/chromium-browser/plugins .  Then Enable this in plugin
   page.
-  If you view any video it will download in
   /home/<USER\_NAME>/.cache/chromium/Default/Cache this folder.
-  For Google chrome user cache location will be
   /home/<USER\_NAME>/.cache/google-chrome/Default/Cache

Make a link for easy access

    ln -s /home/arul/.cache/chromium/Default/Cache/ /tmp/chrome-cache

Screenshots:

Details View of the Plugin page
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image0|

.. raw:: html

   </div>

Chromium Plugin folder
^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image1|

.. raw:: html

   </div>

Chromium Cache folder
^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image2|

.. raw:: html

   </div>

My Configuration:

| OS : Ubuntu 10.04
|  Browser : Chromium 10.0.648.133 (Developer Build 77742) Ubuntu 10.04
|  Flash : Shockwave Flash 10.2 r152

Update on 21th March 2011:

After a deep testing the video downloaded is disappear after sometime. I
tested against youtube.

Otherwise use older version:

Download the older version of Flashplayer 10. Then copy that to chromium
plugin directory. Enable this plugin now you can get the file in the
/tmp directory. I am using Version: 10.0 r45. I get this version from
with flex sdk runtime folder.

.. |image0| image:: http://1.bp.blogspot.com/-cLF0pmaL9ws/TYULYUaA1oI/AAAAAAAAAns/BrRbE1fbemo/s400/chrome%2Bplugin%2B-%2BDetails%2Bview.png
   :target: http://1.bp.blogspot.com/-cLF0pmaL9ws/TYULYUaA1oI/AAAAAAAAAns/BrRbE1fbemo/s1600/chrome%2Bplugin%2B-%2BDetails%2Bview.png
.. |image1| image:: http://1.bp.blogspot.com/-k8fb-V-sEks/TYUL-qW_N2I/AAAAAAAAAn0/t-R6vmr_-ow/s400/chrome%2Bplugin%2Bdirectory.png
   :target: http://1.bp.blogspot.com/-k8fb-V-sEks/TYUL-qW_N2I/AAAAAAAAAn0/t-R6vmr_-ow/s1600/chrome%2Bplugin%2Bdirectory.png
.. |image2| image:: http://4.bp.blogspot.com/-RHXSFHAJpCA/TYUMIGQU6_I/AAAAAAAAAn8/M_eTTLo3IKM/s400/chrome%2Bcache%2Blocation.png
   :target: http://4.bp.blogspot.com/-RHXSFHAJpCA/TYUMIGQU6_I/AAAAAAAAAn8/M_eTTLo3IKM/s1600/chrome%2Bcache%2Blocation.png
