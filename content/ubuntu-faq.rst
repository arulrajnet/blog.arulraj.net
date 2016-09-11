Ubuntu FAQ
##########
:date: 2010-06-13 13:44
:author: arul
:category: Linux
:tags: commands, Linux, ubuntu, how to
:slug: ubuntu-faq

|image0|

Hi i am using ubuntu in `my
laptop <http://www.arulraj.net/2010/06/install-ubuntu-10-04-in-acer-5740.html>`__
. Previously i am using windows os. i face some problems like how to
open my computer in shorcut, show desktop, Run etc., i search in google
and resolve here i explain how to do those things. This is not for
ubuntu/linux guru's only for newbies like me :)

How to open My computer (filesystem) in ubuntu ..?

There is a command called "nautilus" . This will help you. Open Terminal
then type "nautilus /" this will open your filesystem. Then create
Launcher (shortcut) for this.

How to Create a shortcut ..?

Go to your Desktop. Then Right Click --> Select "Create Launcher". It
shows a window Fill up the like the below

|image1|

In the Create Launcher window Type this Command "nautilus /". Select
your own name and own comment. Then click OK. Now the your "My Computer
" icon is created in the Desktop like the below

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image2|

.. raw:: html

   </div>

Using the nautilus command you can create the shortcut for any folder.
For Home folder change the command "nautilus /root" .

| There is a another method to do all the things.
|  Goto terminal then type "gconf-editor" it opens a Configuration
  Editor. Its like a Registry Editor in windows operating system.

Its like the below

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image3|

.. raw:: html

   </div>

| Goto Configuration Editor --> apps --> nautilus --> Desktop
|  Then Check the checkbox "computer\_icon\_visible" and
  "home\_icon\_visible" . Now the your computer and Home icons are shown
  in your desktop.

|image4|

How to create custom keyboard shortcut ..?

In ubuntu you can create your own custom keyboard shortcut. Goto System
--> Preference --> keyboard shortcuts.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image5|

.. raw:: html

   </div>

It opens a new window. Click the Add button then Enter your own name and
type the command for that. For example if you want to open "System
Monitor" its like Task manager in windows type this command
"gnome-system-monitor". Then press Apply. Now its time to select your
shortcut keys. Select which one you added then choose your combination
of keys.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image6|

.. raw:: html

   </div>

| How to set environmental variables ..?
|  Lot of ways available to set the environmental variable. But this is
  the most simple one. You can add your variable in "/etc/environment"
  file
|  open this file then add your bin folder in the PATH. You can add HOME
  variable like "JAVA\_HOME" in the next line.

|image7|

Some Ubuntu shortcuts :

| To open Terminal window CTRL+ALT+T
|  To open Run window ALT+F2
|  To Choose the Desktop Windows key + E
|  Show Desktop CTRL+ALT+D

.. |image0| image:: http://lh6.ggpht.com/_X5tq9y9xv2s/TBE3MO5AjmI/AAAAAAAAAZI/_QfbEoEor1Q/s512/ubuntu-logo.gif
   :target: http://picasaweb.google.com/lh/photo/H_Aajl3cxrd_q5qtDv82yRRU7417pzdLFPTzvmy2uw8?feat=blogger
.. |image1| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/TBUfGYQA4oI/AAAAAAAAAZQ/iJRZnOfdDws/s320/ubuntu+create+shorcut.png
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/TBUfGYQA4oI/AAAAAAAAAZQ/iJRZnOfdDws/s1600/ubuntu+create+shorcut.png
.. |image2| image:: http://3.bp.blogspot.com/_X5tq9y9xv2s/TBUfItPVR2I/AAAAAAAAAZY/rB8CIUT-cNQ/s320/ubuntu+my+computer.png
   :target: http://3.bp.blogspot.com/_X5tq9y9xv2s/TBUfItPVR2I/AAAAAAAAAZY/rB8CIUT-cNQ/s1600/ubuntu+my+computer.png
.. |image3| image:: http://2.bp.blogspot.com/_X5tq9y9xv2s/TBUm5ktozNI/AAAAAAAAAZg/2pdoXC_fiGU/s320/ubuntu+Configuration+Editor+-+desktop.png
   :target: http://2.bp.blogspot.com/_X5tq9y9xv2s/TBUm5ktozNI/AAAAAAAAAZg/2pdoXC_fiGU/s1600/ubuntu+Configuration+Editor+-+desktop.png
.. |image4| image:: http://2.bp.blogspot.com/_X5tq9y9xv2s/TBUo0o1QdoI/AAAAAAAAAZo/NTOAbc70qKA/s320/ubuntu+desktop+icon.png
   :target: http://2.bp.blogspot.com/_X5tq9y9xv2s/TBUo0o1QdoI/AAAAAAAAAZo/NTOAbc70qKA/s1600/ubuntu+desktop+icon.png
.. |image5| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TBZqxPcrfUI/AAAAAAAAAaA/ZnNuu2pn8m8/s320/ubuntu+keyboard+shorcut.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TBZqxPcrfUI/AAAAAAAAAaA/ZnNuu2pn8m8/s1600/ubuntu+keyboard+shorcut.png
.. |image6| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TBUxbc0bnCI/AAAAAAAAAZw/uyh9gjH6vWE/s320/Keyboard+shorcut.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TBUxbc0bnCI/AAAAAAAAAZw/uyh9gjH6vWE/s1600/Keyboard+shorcut.png
.. |image7| image:: http://3.bp.blogspot.com/_X5tq9y9xv2s/TBU0yyPQyRI/AAAAAAAAAZ4/RiE8Aiw85dg/s320/ubuntu+environment+variable.png
   :target: http://3.bp.blogspot.com/_X5tq9y9xv2s/TBU0yyPQyRI/AAAAAAAAAZ4/RiE8Aiw85dg/s1600/ubuntu+environment+variable.png
