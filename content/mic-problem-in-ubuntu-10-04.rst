Mic problem in ubuntu 10.04
###########################
:date: 2010-07-05 13:35
:author: arul
:category: Linux
:tags: Linux, ubuntu, how to
:slug: mic-problem-in-ubuntu-10-04

**Mic Problem in ubuntu 10.04 for Root user**

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image0|

.. raw:: html

   </div>

I am using ubuntu 10.04 in my laptop. I created a user when installing
ubuntu . The sound and Mic are working fine for that user. I enabled the
root by using the following command

To enable root user. Login with existing user then goto Terminal.

    sudo passwd root

Now the root user is enabled. I logged in with root user. I seen the
sound is not working for me. The volume icon is always in "mute" state

| What is the Error shown ...?
|  When i click the "Sound Preference" in volume button or System -->
  Preference --> Sound it always shows a Warning message "Waiting for
  Sound system to respond"

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image1|

.. raw:: html

   </div>

| How to fix mic problem for root user ..?
|  Goto System --> Preference --> Startup Applications .

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image2|

.. raw:: html

   </div>

Now you need add a new startup application. Add "pulseaudio" as a
startup application

| Name: pulseaudio
|  Command : /usr/bin/pulseaudio
|  Comment: To start pulseaudio deamon

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image3|

.. raw:: html

   </div>

Then logout and login again. For min i restarted my system. Now you can
see the Volume control icon in unmute state and you can edit your sound
preference now.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image4|

.. raw:: html

   </div>

Editing sound preference:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image5|

.. raw:: html

   </div>

.. |image0| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/TDIvaC1A0YI/AAAAAAAAAb8/fg2JNqwg6uE/s320/Volume+in+ubuntu+10.04.png
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/TDIvaC1A0YI/AAAAAAAAAb8/fg2JNqwg6uE/s1600/Volume+in+ubuntu+10.04.png
.. |image1| image:: http://3.bp.blogspot.com/_X5tq9y9xv2s/TEc_0dAcuYI/AAAAAAAAAdc/uRcnI1a_fG0/s320/waiting+for+response.png
   :target: http://3.bp.blogspot.com/_X5tq9y9xv2s/TEc_0dAcuYI/AAAAAAAAAdc/uRcnI1a_fG0/s1600/waiting+for+response.png
.. |image2| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/TDIxqUrbzsI/AAAAAAAAAcE/jVA2AakzRC4/s320/startup+application+-+ubuntu.png
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/TDIxqUrbzsI/AAAAAAAAAcE/jVA2AakzRC4/s1600/startup+application+-+ubuntu.png
.. |image3| image:: http://3.bp.blogspot.com/_X5tq9y9xv2s/TDIyC_EXQrI/AAAAAAAAAcM/JC7uXRAJqvk/s320/Add+start+up+application+ubuntu.png
   :target: http://3.bp.blogspot.com/_X5tq9y9xv2s/TDIyC_EXQrI/AAAAAAAAAcM/JC7uXRAJqvk/s1600/Add+start+up+application+ubuntu.png
.. |image4| image:: http://2.bp.blogspot.com/_X5tq9y9xv2s/TDIywdsgklI/AAAAAAAAAcU/htWK_E-B4o4/s320/working+mic+for+ubuntu.png
   :target: http://2.bp.blogspot.com/_X5tq9y9xv2s/TDIywdsgklI/AAAAAAAAAcU/htWK_E-B4o4/s1600/working+mic+for+ubuntu.png
.. |image5| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/TDIz1bMbXWI/AAAAAAAAAck/o55AK7XlmX4/s320/Sound+Preferences+-+ubuntu+10.04.png
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/TDIz1bMbXWI/AAAAAAAAAck/o55AK7XlmX4/s1600/Sound+Preferences+-+ubuntu+10.04.png
