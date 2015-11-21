:title: Live Cricket Score on your terminal
:slug: live-cricket-score-on-your-terminal
:date: 2015-05-10 13:11:59
:tags: linux, cricket, shellscript
:category: Linux
:author: arul
:lang: en

**Live Cricket Score From CricInfo on your Bash Terminal**

|score_terminal|

You are a hardcore cricket fan, want to get updated the score while working 😄 😄 . But bored to open a browser ⇒ goto cricinfo ⇒ goto particular cricket match. Welcome, this script for you only. 

Why this Script..?
##################

I am not the fan of cricket. But some of friends working as Linux Administrators who is always looking black and white terminal, They want to know the score. So I wrote a shellscript to get score from cricinfo. Now they happily run this script in an another terminal and gets updated about score.

How to use..?
#############

- Download the file from github `livecricketscore.sh <gist_livecricketscore_>`_
- Then copy that file in to /usr/bin/ folder
- Run that ``livecricketscore`` from anywhere
- It will ask for the which match score you want to know
- Select the matcher number
- It will continuously run untill you kill ( CTRL + C ) that

.. code-block:: bash

	wget --no-check-certificate https://gist.githubusercontent.com/arulrajnet/fb71169c35180f9d9abd/raw/livecricketscore.sh
	chmod +x livecricketscore.sh
	cp livecricketscore.sh /usr/bin/livecricketscore
	sh /usr/bin/livcricketscore

You need to install xmllint if its not there already. To install xmllint in ubuntu

.. code-block:: bash

	apt-get update
	apt-get install libxml2-utils

Credits
#######

Thanks to ww.espncricinfo.com . I am using their RSS feed to list the live matches and get the score.

.. _gist_livecricketscore: https://gist.githubusercontent.com/arulrajnet/fb71169c35180f9d9abd "Gist Link for LiveCricketScore"

.. |score_terminal| image:: http://1.bp.blogspot.com/-aJzVV1AyHS4/VU4v696M-HI/AAAAAAAAWPc/iWGrzuIGMMc/s640/livecricketscore.png
	:target: http://1.bp.blogspot.com/-aJzVV1AyHS4/VU4v696M-HI/AAAAAAAAWPc/iWGrzuIGMMc/s1600/livecricketscore.png
