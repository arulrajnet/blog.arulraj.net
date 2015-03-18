How to install mplayer on fedora ..?
####################################
:date: 2010-01-19 08:48
:author: arul
:category: Linux
:tags: Fedora, Linux
:slug: how-to-install-mplayer-on-fedora

**How to install mplayer on fedora**

|http://www.haifux.org/lectures/134/lecture/images/mplayer.png|

When i try to install mplayer-1.0-0.102.20080903svn.fc10.src.rpm in
fedora i got this error. i download this file from
`rpmfusion <http://download1.rpmfusion.org/free/fedora/releases/10/Everything/source/SRPMS/repoview/index.html>`__

| [plain]
|  [root@localhost Media]# rpm -ivh
  mplayer-1.0-0.102.20080903svn.fc10.src.rpm
|  warning: mplayer-1.0-0.102.20080903svn.fc10.src.rpm: Header V3 DSA
  signature: NOKEY, key ID 49c8885a
|  1:mplayer warning: user mockbuild does not exist - using root
|  warning: group mockbuild does not exist - using root
|  warning: user mockbuild does not exist - using root
|  warning: group mockbuild does not exist - using root
|  warning: user mockbuild does not exist - using root
|  warning: group mockbuild does not exist - using root
|  warning: user mockbuild does not exist - using root
|  warning: group mockbuild does not exist - using root
|  ########################################### [100%]
|  [/plain]

I have the same problem when i try to install wine-1.0.1-1.el4.i386.rpm

| I have not internet connection in my home pc. so what to do..?
|  i goes to "/usr/src/redhat/SOURCES" folder there is a file called
  mplayer-export-2008-09-03.tar.bz2
|  Extract the file and configure it then make and make install.
|  Now i have mplayer in my home pc

| [plain]
|  [root@localhost Movies]# mplayer 2012.avi
|  MPlayer dev-SVN-r27514 (C) 2000-2008 MPlayer Team
|  CPU: Intel(R) Pentium(R) 4 CPU 3.00GHz (Family: 15, Model: 4,
  Stepping: 3)
|  CPUflags: MMX: 1 MMX2: 1 3DNow: 0 3DNow2: 0 SSE: 1 SSE2: 1
|  Compiled for x86 CPU with extensions: MMX MMX2 SSE SSE2

| Playing 2012.avi.
|  AVI file format detected.
|  [aviheader] Video stream found, -vid 0
|  [aviheader] Audio stream found, -aid 1
|  AVI: ODML: Building ODML index (2 superindexchunks).
|  VIDEO: [XVID] 608x272 12bpp 29.970 fps 674.6 kbps (82.4 kbyte/s)
|  [/plain]

|image1|

when i play the avi file using mplayer it does not play the video only
play the audio

Now i changed the command

[root@localhost Movies]# mplayer -vo x11 -ao alsa 2012.avi

Now working fine

|image2|

.. |http://www.haifux.org/lectures/134/lecture/images/mplayer.png| image:: http://www.haifux.org/lectures/134/lecture/images/mplayer.png
.. |image1| image:: http://3.bp.blogspot.com/_X5tq9y9xv2s/S1W9z-cISFI/AAAAAAAAAHg/LW8cMmLo91E/s400/Screenshot-MPlayer.png
   :target: http://3.bp.blogspot.com/_X5tq9y9xv2s/S1W9z-cISFI/AAAAAAAAAHg/LW8cMmLo91E/s1600-h/Screenshot-MPlayer.png
.. |image2| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/S1W90LG8hUI/AAAAAAAAAHo/M8yz1QPT8cs/s400/Screenshot-MPlayer-1.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/S1W90LG8hUI/AAAAAAAAAHo/M8yz1QPT8cs/s1600-h/Screenshot-MPlayer-1.png
