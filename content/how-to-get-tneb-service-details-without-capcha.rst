:title: How to get TNEB Service Details without capcha
:slug: how-to-get-tneb-service-details-without-capcha
:date: 2015-09-06 21:03:28
:tags: javascript
:category: Tools
:author: Arul
:lang: en
:status: published
:summary: 

To get direct link for find your usage from TNEB give your service number in the below form and press submit. 

**TNEB Usage permlink Form**

.. raw:: html

  <iframe width="100%" height="400" src="//jsfiddle.net/arulrajnet/0dfht8L2/embedded/result" allowfullscreen="allowfullscreen" frameborder="0"></iframe>


How its works
#############

- For example, the service no is 265 / 005 / 1234 

- It will take your service no and do base64 of "TANGEDCO||265||005||1234" is ``VEFOR0VEQ098fDI2NXx8MDA1fHwxMjM0``

- Then base64 of Region(09) is ``OQ==``

- Then finally URL is http://tneb.tnebnet.org/newlt/consumerwise_gmc_report.php?encserno=VEFOR0VEQ098fDI2NXx8MDA1fHwxMjM0&rsno=OQ==

You can find the source code from here https://jsfiddle.net/arulrajnet/0dfht8L2/
