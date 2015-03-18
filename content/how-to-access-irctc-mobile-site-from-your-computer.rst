How to access irctc mobile site from your computer
##################################################
:date: 2012-01-31 02:50
:author: arul
:category: Browser
:tags: Browser, hacking, how to, mobile
:slug: how-to-access-irctc-mobile-site-from-your-computer
:status: published

**How to access irctc mobile site from your computer**

[caption id="" align="aligncenter" width="240" caption="Taken from
android browser"]\ |image0|\ [/caption]

Two weeks before irctc launched mobile site for train booking. But when
I try to go https://www.irctc.co.in/mobile from my pc its redirect to
usual site. The problem is they are checking the request coming from
mobile or computer in server side using user agent and if its from
mobile allowed otherwise its redirected to ordinary site.

So here is the fix :)

Requirement:

-  absolutely a pc
-  Mozilla Firefox
-  User Agent switcher add-on

How to:

-  Open Firefox
-  Download and Install the User Agent switcher add-on from
   `here  <https://addons.mozilla.org/en-US/firefox/addon/user-agent-switcher/>`__
-  Change the User agent to iPhone 3.0 by Go to Tools
-  Now open the https://www.irctc.co.in/mobile in Firefox
-  Yeah you are done. cheers...!!!

User Agent switcher:

[caption id="" align="aligncenter" width="400" caption="Change to iPhone
3.0"]\ |image1|\ [/caption]

How irctc looks in firefox:

[caption id="" align="aligncenter" width="400" caption="Mobile Login
page"]\ |image2|\ [/caption]

[caption id="" align="aligncenter" width="400" caption="Mobile Home
page"]\ |image3|\ [/caption]

[caption id="" align="aligncenter" width="400" caption="Mobile plan my
travel"]\ |image4|\ [/caption]

Advantages of mobile agent:

-  Firstly its very fast.
-  Easy to book. Just three clicks.
-  No more asking password again and again
-  No more session expired / timeout page :D
-  Do remember you can only book **5 transactions per month** through
   mobile irctc site.

**FAQ:**

| I tried in mobile still redirect to ordinary site..?
|  Use https instead of http and make sure www in that url
  https://www.irctc.co.in/mobile

| How can I change the user agent in google chrome..?
|  To change user agent in google chrome check this video tutorial
  http://www.youtube.com/watch?v=IiT7z8zAbn0 But for that you need
  chrome 17 version. To find out which chrome you are using type
  "about:version" in address bar then enter. If you have chrome version
  16, wait for 17 to be stable otherwise try beta version.
|  **Update:** Now a extension is available for chrome
  ` <https://chrome.google.com/webstore/detail/djflhoibgkdhkhhcedjiklpkjnoahfmg>`__\ use
  this.

| Is this irctc hack..?
|  No. Its just a browser hack..!!! you can see any mobile website using
  this.

| How to use this mobile site..?
|  Please find the manual from here. `View
  Manual <https://www.irctc.co.in/beta_htmls/index.htm>`__

| **Its shows me a blank page..?**
|  Last few days I am also getting blank pages. That website is seems to
  be down. Even its shows error page when I tried from mobile device. No
  fix for this :-) check this
  `link <http://www.downforeveryoneorjustme.com/www.irctc.co.in/mobile>`__ for
  its down or not

| My Firefox is does not support for this add-on..?
|  I think you are using old one. Try to update your firefox browser. OR
  from here \ http://releases.mozilla.org/pub/mozilla.org/addons/59/ you
  can find the different version of that add-on. Download which one is
  suitable for your firefox.

.. |image0| image:: http://1.bp.blogspot.com/-7TGwu0R8Woc/TyecsHLfDiI/AAAAAAAAJIk/k_B8DnwHEew/s400/irctc_in_android_browser.png
   :target: http://1.bp.blogspot.com/-7TGwu0R8Woc/TyecsHLfDiI/AAAAAAAAJIk/k_B8DnwHEew/s1600/irctc_in_android_browser.png
.. |image1| image:: http://3.bp.blogspot.com/-Q3dWVraB26g/Tyeo4jLneqI/AAAAAAAAJI0/gIPfMDGJ-y8/s400/User_agent_firefox.png
   :target: http://3.bp.blogspot.com/-Q3dWVraB26g/Tyeo4jLneqI/AAAAAAAAJI0/gIPfMDGJ-y8/s1600/User_agent_firefox.png
.. |image2| image:: http://2.bp.blogspot.com/-X3MnnhCcEbU/TyepsS3HEeI/AAAAAAAAJJA/72pM_nkgmKs/s400/irctc_firefox_mobile_login.PNG
   :target: http://2.bp.blogspot.com/-X3MnnhCcEbU/TyepsS3HEeI/AAAAAAAAJJA/72pM_nkgmKs/s400/irctc_firefox_mobile_login.PNG
.. |image3| image:: http://3.bp.blogspot.com/-n75ZOpg1b98/TyeqTnGPxNI/AAAAAAAAJJM/pub05DdyFpI/s400/irctc_firefox_mobile_home.PNG
   :target: http://3.bp.blogspot.com/-n75ZOpg1b98/TyeqTnGPxNI/AAAAAAAAJJM/pub05DdyFpI/s1600/irctc_firefox_mobile_home.PNG
.. |image4| image:: http://3.bp.blogspot.com/-wHuu4TgXKWw/TyeqxQhckVI/AAAAAAAAJJY/kJOQLrX-0N4/s400/irctc_firefox_mobile_plan_my_travel.PNG
   :target: http://3.bp.blogspot.com/-wHuu4TgXKWw/TyeqxQhckVI/AAAAAAAAJJY/kJOQLrX-0N4/s1600/irctc_firefox_mobile_plan_my_travel.PNG
