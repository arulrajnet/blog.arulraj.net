Stream any video into VLC
##########################

:title: Stream any video into VLC
:slug: stream-any-video-into-vlc
:date: 2015-09-11 22:07:12
:tags: streaming, vlc, youtube-dl
:category: Streaming
:author: arul
:lang: en
:disqus_identifier: /2015/09/stream-any-video-into-vlc.html


You can stream any online like youtube, vimeo, facebook, dailymotion, etc., video into your VLC / mplayer using youtube-dl. Here I will explain how to do that.

.. figure:: http://1.bp.blogspot.com/-oE3JlsHUyPE/VfMISTKA3TI/AAAAAAAAWWY/7oGiGoyFx5Q/s320/stream-to-vlc.png
  :target: http://1.bp.blogspot.com/-oE3JlsHUyPE/VfMISTKA3TI/AAAAAAAAWWY/7oGiGoyFx5Q/s1600/stream-to-vlc.png
  :align: center
  :alt: Streaming in VLC using youtube-dl


First Install latest greatest youtube-dl

.. code-block:: bash

  sudo pip install --upgrade youtube-dl
  OR
  sudo apt-get install youtube-dl

As per todoy the version is 2015.09.09. To get version ``youtube-dl --version``

Here is the command to stream to vlc

.. code-block:: bash

  youtube-dl -o - "http://your.media/url" | vlc -

You can also set up a function in your ~/.bash_aliases file like

.. code-block:: bash

  function streamer() {
    youtube-dl -o - "$1" | vlc -
  }

Referred from https://github.com/rg3/youtube-dl/issues/2124#issuecomment-32429104
