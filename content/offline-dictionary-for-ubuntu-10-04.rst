Offline dictionary for ubuntu 10.04
###################################
:date: 2010-06-28 13:53
:author: arul
:category: Linux
:tags: ubuntu, how to
:slug: offline-dictionary-for-ubuntu-10-04

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image0|

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Why offline dictionary ..?

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Anyway ubuntu 10.04 have dictionary by default. You can find the
dictionary from Application → office → Dictionary. You can find the
meaning of a english word using this. When you search for meaning of a
word its communicate with online dictionary server for ex. dict.org then
get the result. If you not having the Net connection / poor connection
its useless. In this situation offline dictionary will helpful to you.
For this you need to install dictionary server in your local ubuntu
machine. here is how to do this.

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image1|

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

How to install dictionary server in local ..?

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Goto terminal and run the following commands

.. raw:: html

   </div>

| [bash]
|  sudo apt-get install dictd
|  sudo apt-get install dict-gcide
|  sudo apt-get install dict-moby-thesaurus
|  [/bash]

| dictd - This is the Dictionary server which supports DICT protocol.
|  dict-gcide - English Dictionary
|  dict-moby-thesaurus - thesaurus data source in English. This is an
  optional one

Yes now you are successfully installed a dictionary server. Now you need
to add this server with your dictionary client.

| How to add local dictionary to dictionary client ..?
|  Goto Dictionary then Edit → Preference

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image2|

.. raw:: html

   </div>

Click the "Add" button to add a new dictionary

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image3|

.. raw:: html

   </div>

| Enter your local dictionary details.
|  Dictionary name : Default
|  Transport : Dictionary Server
|  Hostname : 127.0.0.1
|  Port : 2628

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image4|

.. raw:: html

   </div>

Thats all. Now you can search locally.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image5|

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Update on 6th June 2011:

.. raw:: html

   </div>

.. raw:: html

   <div class="separator"
   style="clear: both; text-align: left; padding-left: 30px;">

Now I found an application for offline Dictionary from ubuntu software
center you can install it from here. Name is
`Artha <http://artha.sourceforge.net/wiki/index.php/Home>`__ .

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image6|

.. raw:: html

   </div>

Update on 20th November 2011:

| Here I have given steps for installing dictionary server for a
  dictionary client such as "Gnome Dictionary". Before Installing
  dictionary server make sure do have any dictionary client.
|  [bash]sudo apt-get install gnome-dictionary[/bash]
|  this is the command for installing Gnome Dictionary.

.. |image0| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TCj1u9sK79I/AAAAAAAAAbE/6-RRuRSCn6w/s320/ubuntu_icon.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TCj1u9sK79I/AAAAAAAAAbE/6-RRuRSCn6w/s1600/ubuntu_icon.png
.. |image1| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/TCj6wHIa52I/AAAAAAAAAbM/r_06GVCYYNc/s320/How+to+offline+Dictionery+ubuntu.png
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/TCj6wHIa52I/AAAAAAAAAbM/r_06GVCYYNc/s1600/How+to+offline+Dictionery+ubuntu.png
.. |image2| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/TCj7I1bnJXI/AAAAAAAAAbU/9Xf59VIKGzM/s320/How+to+offline+Dictionery+ubuntu+-+preference.png
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/TCj7I1bnJXI/AAAAAAAAAbU/9Xf59VIKGzM/s1600/How+to+offline+Dictionery+ubuntu+-+preference.png
.. |image3| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TCj7lwcawGI/AAAAAAAAAbc/kn0Tb2pGQ6M/s320/How+to+offline+Dictionery+ubuntu-add+dictionary.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TCj7lwcawGI/AAAAAAAAAbc/kn0Tb2pGQ6M/s1600/How+to+offline+Dictionery+ubuntu-add+dictionary.png
.. |image4| image:: http://3.bp.blogspot.com/_X5tq9y9xv2s/TCj8O4iRQpI/AAAAAAAAAbk/wsIQHjRkmc0/s320/How+to+offline+Dictionery+ubuntu-Edit+Dictionary+Source.png
   :target: http://3.bp.blogspot.com/_X5tq9y9xv2s/TCj8O4iRQpI/AAAAAAAAAbk/wsIQHjRkmc0/s1600/How+to+offline+Dictionery+ubuntu-Edit+Dictionary+Source.png
.. |image5| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/TCj80W9JaTI/AAAAAAAAAbs/RH9BORx27fs/s320/java+-+ubuntu+Dictionary+search.png
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/TCj80W9JaTI/AAAAAAAAAbs/RH9BORx27fs/s1600/java+-+ubuntu+Dictionary+search.png
.. |image6| image:: http://1.bp.blogspot.com/-UvmfYZPfF-0/TevXeMyrFdI/AAAAAAAAAps/oUuZWdM5oXY/s400/artha-offlince-dictionary.png
   :target: http://1.bp.blogspot.com/-UvmfYZPfF-0/TevXeMyrFdI/AAAAAAAAAps/oUuZWdM5oXY/s1600/artha-offlince-dictionary.png
