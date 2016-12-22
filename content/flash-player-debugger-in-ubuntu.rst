Flash player debugger in ubuntu
###############################
:date: 2010-08-02 15:34
:author: arul
:category: Flash
:tags: Flash, Linux
:slug: flash-player-debugger-in-ubuntu
:disqus_identifier: /2010/08/flash-player-debugger-in-ubuntu.html

**How to flash debug player in Linux**

|image0|

After a long time i am working on Flex for one of client for his one to one chat application. At this time i need flash debugger for debugging my program. The debug player need for to print trace() output to flashlog.txt.

Here the steps for how to install debug flashplayer in ubuntu 10.04 firefox 3.6.

Steps:

-  Download the debugger version from `here <http://www.adobe.com/support/flashplayer/downloads.html>`__ . Or Download this Zip file for Linux http://download.macromedia.com/pub/flashplayer/updaters/10/flashplayer_10_plugin_debug.tar.gz
-  Extract that zip file and get that "libflashplayer.so"
-  Goto this folder "/usr/lib/mozilla/plugins" then copy and  paste that libflashplayer.so here. Then Delete the shortcut named "flashplugin-alternative.so"
-  Create a mm.cfg file in your home directory. For example /home/<username>/mm.cfg
-  The mm.cfg file is look like the below

.. code-block:: text

  ErrorReportingEnable=0
  TraceOutputFileEnable=1
  MaxWarnings=0

Then restart your firefox now you can found flashlog.txt file in

cd $HOME/.macromedia/Flash_Player/Logs/ folder.

|image1|

Update on 19th October 2011:

-  Download the debugger version from `here <http://www.adobe.com/support/flashplayer/downloads.html>`__. Then extract that libflashplayer.so
-  Copy that so file to /usr/lib/mozilla/plugins/ dir
-  Then replace the soft link by the following command

.. code-block:: text

  sudo ln -fs /usr/lib/mozilla/plugins/libflashplayer.so /usr/lib/mozilla/plugins/flashplugin-alternative.so

Its works with my Firefox 7.0.1 in ubuntu 11.04

.. |image0| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TFc1w8gf4JI/AAAAAAAAAfE/-ysWrI7BnTE/s320/Flashlog.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TFc1w8gf4JI/AAAAAAAAAfE/-ysWrI7BnTE/s1600/Flashlog.png
.. |image1| image:: http://2.bp.blogspot.com/_X5tq9y9xv2s/TFc5mvVuXeI/AAAAAAAAAfM/K1ZLN2ivtdE/s320/Mozilla+plugin+folder.png
   :target: http://2.bp.blogspot.com/_X5tq9y9xv2s/TFc5mvVuXeI/AAAAAAAAAfM/K1ZLN2ivtdE/s1600/Mozilla+plugin+folder.png
