:title: Download any videos in android using youtube-dl
:slug: download-any-videos-in-android-using-youtube-dl
:date: 2015-11-21 12:14:38
:tags: streaming, mobile, youtube-dl, android
:category: android
:author: Arul
:lang: en
:status: published

There are lot of app there in google play store to download video youtube. All are claiming it has all the features and so and so... But the reality is, they are not working in all the times. 

In my laptop I am using `youtube_dl <https://rg3.github.io/youtube-dl/>`__ to download videos. Its working for most of the video sites including youtube, vimeo and etc., I want setup that in my android mobile. So here is the how to do...

**Steps**

  * Install python on android
  * Install youtube-dl
  * Download a video using youtube-dl

Install Python
--------------

Install `QPython <https://play.google.com/store/apps/details?id=com.hipipal.qpyplus&hl=en>`__ from google app store to use python in android.

.. figure:: /assets/images/QPython-Google-Play.png
    :align: center
    :alt: QPython in Google play store

.. Installing QPython from Google play store.

Install youtube-dl
------------------

Goto QPython Dashboard. Slide left from home screen to go dashboard. 

.. figure:: /assets/images/QPython-dashboard.png
    :align: center
    :alt: QPython Dashboard


Click Libraries and "pip console"

.. figure:: /assets/images/QPython-pip-console.png
    :align: center
    :alt: QPython pip console

In the console ``pip install -U youtube-dl``

.. figure:: /assets/images/QPython-Installing-youtube-dl.png
    :align: center
    :alt: QPython android install youtube-dl

To validate the youtube downloader in android ``youtube-dl --version``

.. figure:: /assets/images/QPython-youtube-dl-version.jpeg
    :align: center
    :alt: QPython android install youtube-dl

Download Video
--------------

To download video, Goto pip console

Then ``youtube-dl -o Chammak_Challo.mp4 https://www.youtube.com/watch?v=yh2K9VlGj9Q``

The argument "-o NAME_OF_FILE.mp4" is required field.

From youtube

.. figure:: /assets/images/Qpython-downloding-from-youtube.jpeg
    :align: center
    :alt: QPython android install youtube-dl


From facebook

.. figure:: /assets/images/Qpython-downloding-from-facebook.png
    :align: center
    :alt: QPython android install youtube-dl
