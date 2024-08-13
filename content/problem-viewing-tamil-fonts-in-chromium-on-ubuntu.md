---
title: Problem viewing Tamil fonts in chromium on Ubuntu
date:   2011-08-26 12:41
author: arul
category:   Linux
tags:   Browser, tamil, ubuntu, how-to, linux
slug:   problem-viewing-tamil-fonts-in-chromium-on-ubuntu
status:   published
disqus_identifier:    /2011/08/problem-viewing-tamil-fonts-in-chromium-on-ubuntu.html
---

I am the big fan of tamil love poems.. 😊 Within Google reader all tamil
blogs fonts are displayed correctly in chromium which was downloaded
from Ubuntu software center. But when I goto that link directly, that
page is not rendered properly. It shows some junk character in between.

For example Initially this blog http://bit.ly/ndtgfq shown below

[![image0](http://3.bp.blogspot.com/-rRgxWW7Qfvs/TlfmYG-R55I/AAAAAAAAArc/-I3ojySvirc/s400/Tamil%2Bfont%2Berror.png)](http://3.bp.blogspot.com/-rRgxWW7Qfvs/TlfmYG-R55I/AAAAAAAAArc/-I3ojySvirc/s1600/Tamil%2Bfont%2Berror.png)
Tamil font is not rendered properly

But in the firefox its rendered correctly. It shows the fonts correctly.
I solved this issue after little bit googling 😜

Here is the fix.

-   Goto that directory /usr/share/fonts/truetype/freefont/
-   Delete both the FreeSerif.ttf and FreeSans.ttf file.

``` bash
sudo rm -f /usr/share/fonts/truetype/freefont/FreeSerif.ttf 
sudo rm -f /usr/share/fonts/truetype/freefont/FreeSans.ttf 
```

Then restart your browser. Now its shown correctly for me.

[![image1](http://4.bp.blogspot.com/-b0-zDfWqj5w/Tlfn0iQY8nI/AAAAAAAAArk/CrtbQxkS3gE/s400/Tamil%2Bfont%2Bsuccess.png)](http://4.bp.blogspot.com/-b0-zDfWqj5w/Tlfn0iQY8nI/AAAAAAAAArk/CrtbQxkS3gE/s1600/Tamil%2Bfont%2Bsuccess.png)
Tamil font displayed fine
