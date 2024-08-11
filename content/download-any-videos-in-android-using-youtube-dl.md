---
title: Download any videos in android using youtube-dl
slug:   download-any-videos-in-android-using-youtube-dl
date:   2015-11-21 12:14:38
tags:   streaming, mobile, youtube-dl, android
category:   android
author: arul
lang:   en
status:   published
disqus_identifier:    /2015/11/download-any-videos-in-android-using-youtube-dl.html
---

There are lot of app there in google play store to download video
youtube. All are claiming it has all the features and so and so\... But
the reality is, they are not working in all the times.

In my laptop I am using [youtube_dl](https://rg3.github.io/youtube-dl/)
to download videos. Its working for most of the video sites including
youtube, vimeo and etc., I want setup that in my android mobile. So here
is the how to do\...

**Steps**

> -   Install python on android
> -   Install youtube-dl
> -   Download a video using youtube-dl

## Install Python

Install
[QPython](https://play.google.com/store/apps/details?id=com.hipipal.qpyplus&hl=en)
from google app store to use python in android.

<figure class="align-center">
<img src="/assets/images/QPython-Google-Play.png"
alt="/assets/images/QPython-Google-Play.png" />
</figure>

## Install youtube-dl

Goto QPython Dashboard. Slide left from home screen to go dashboard.

<figure class="align-center">
<img src="/assets/images/QPython-dashboard.png"
alt="/assets/images/QPython-dashboard.png" />
</figure>

Click Libraries and \"pip console\"

<figure class="align-center">
<img src="/assets/images/QPython-pip-console.png"
alt="/assets/images/QPython-pip-console.png" />
</figure>

In the console `pip install -U youtube-dl`

<figure class="align-center">
<img src="/assets/images/QPython-Installing-youtube-dl.png"
alt="/assets/images/QPython-Installing-youtube-dl.png" />
</figure>

To validate the youtube downloader in android `youtube-dl --version`

<figure class="align-center">
<img src="/assets/images/QPython-youtube-dl-version.jpeg"
alt="/assets/images/QPython-youtube-dl-version.jpeg" />
</figure>

## Download Video

To download video, Goto pip console

Then
`youtube-dl -o Chammak_Challo.mp4 https://www.youtube.com/watch?v=yh2K9VlGj9Q`

The argument \"-o NAME_OF_FILE.mp4\" is required field.

From youtube

<figure class="align-center">
<img src="/assets/images/Qpython-downloding-from-youtube.jpeg"
alt="/assets/images/Qpython-downloding-from-youtube.jpeg" />
</figure>

From facebook

<figure class="align-center">
<img src="/assets/images/Qpython-downloding-from-facebook.png"
alt="/assets/images/Qpython-downloding-from-facebook.png" />
</figure>
