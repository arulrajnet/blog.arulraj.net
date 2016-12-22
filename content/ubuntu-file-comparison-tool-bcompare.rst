Ubuntu file comparison tool - Bcompare
######################################
:date: 2010-07-29 11:39
:author: arul
:category: Linux
:tags: Linux, ubuntu, how to
:slug: ubuntu-file-comparison-tool-bcompare
:disqus_identifier: /2010/07/ubuntu-file-comparison-tool-bcompare.html

**Beyond Compare for ubuntu**

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image0|

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

There are some command line tool for compare two files. But i need a
gnome application. The command line tools are.

.. raw:: html

   </div>

-  `diff <http://linux.die.net/man/1/diff>`__
-  `fcomp <http://www.ifi.uio.no/in219/verktoy/doc/html/doc/sag/sag/adminut6.html>`__

For fcomp you need to install fhist.

    apt-get install fhist

Then i tried `meld <http://meld.sourceforge.net/>`__ . This is a Gnome
based file comparison tool for ubuntu. you can install this using ubuntu
software center. This is an opensource one. But its not working as
expected [ May be i am not know the power of meld  ]. I just tried some
files.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image1|

.. raw:: html

   </div>

When i was a windows user :) [till using windows in my office] i used
beyond compare. That is too good for file compare and merge. Now i
searched that software for ubuntu. Yes they provide software for Linux
too..

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image2|

.. raw:: html

   </div>

I installed beyond compare in ubuntu 10.04.

steps:

-  Download deb file from here
   http://www.scootersoftware.com/bcompare-3.1.11.12238_i386.deb
-  Just open the file "with Debi package installer"
-  Click the button "Install package"

Here some screen shots:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image3|

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image4|

.. raw:: html

   </div>

After installing you can open bcompare from Application --> Programming
--> Beyond Compare

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image5|

.. raw:: html

   </div>

For file comparison you can Right click in a file and choose scripts -->
Select for compare

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image6|

.. raw:: html

   </div>

Now the File difference

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image7|

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Update:

.. raw:: html

   </div>

.. raw:: html

   <div class="separator"
   style="clear: both; text-align: left; padding-left: 30px;">

The winmerge is the best windows Bcompare alternative. For more info
http://winmerge.org/ . This is a freeware and opensource. But its only
available for windows not for linux :(

.. raw:: html

   </div>

.. |image0| image:: http://2.bp.blogspot.com/_X5tq9y9xv2s/TFGzRmR8VQI/AAAAAAAAAd8/eDuMSfQbXw4/s320/File+compare.png
   :target: http://2.bp.blogspot.com/_X5tq9y9xv2s/TFGzRmR8VQI/AAAAAAAAAd8/eDuMSfQbXw4/s1600/File+compare.png
.. |image1| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TFG3hufyJ_I/AAAAAAAAAeE/6-wa1EVwrqw/s320/Meld-compare.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TFG3hufyJ_I/AAAAAAAAAeE/6-wa1EVwrqw/s1600/Meld-compare.png
.. |image2| image:: http://2.bp.blogspot.com/_X5tq9y9xv2s/TFG4g9fjV4I/AAAAAAAAAeM/2u7-70rPa8c/s320/Download+bcompare+for+ubuntu.png
   :target: http://www.scootersoftware.com/download.php
.. |image3| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/TFG6Ld-AbcI/AAAAAAAAAeU/L4y7uS4Qu6Q/s320/Bcompare+Install.png
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/TFG6Ld-AbcI/AAAAAAAAAeU/L4y7uS4Qu6Q/s1600/Bcompare+Install.png
.. |image4| image:: http://3.bp.blogspot.com/_X5tq9y9xv2s/TFG6OgfNi1I/AAAAAAAAAec/ifdzPDuXXHs/s320/Installing+bcompare.png
   :target: http://3.bp.blogspot.com/_X5tq9y9xv2s/TFG6OgfNi1I/AAAAAAAAAec/ifdzPDuXXHs/s1600/Installing+bcompare.png
.. |image5| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/TFG67_2mfDI/AAAAAAAAAek/iBb1TkvlM2Q/s320/Bcompare+in+Application.png
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/TFG67_2mfDI/AAAAAAAAAek/iBb1TkvlM2Q/s1600/Bcompare+in+Application.png
.. |image6| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TFG7BdY_hMI/AAAAAAAAAes/lRsskGPzl88/s320/Bcompare+select+for+compare.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TFG7BdY_hMI/AAAAAAAAAes/lRsskGPzl88/s1600/Bcompare+select+for+compare.png
.. |image7| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TFG7_Aq85oI/AAAAAAAAAe0/6oscenx4hYo/s320/Beyond+compare+on+ubuntu.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TFG7_Aq85oI/AAAAAAAAAe0/6oscenx4hYo/s1600/Beyond+compare+on+ubuntu.png
