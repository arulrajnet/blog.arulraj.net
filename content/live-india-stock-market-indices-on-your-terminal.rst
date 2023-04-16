Live India Stock Market Indices on your Terminal
################################################

:title: Live India Stock Market Indices on your Terminal
:slug: live-india-stock-market-indices-on-your-terminal
:date: 2015-05-10 14:18:18
:tags: share market, linux, python, shellscript
:category: Linux
:author: arul
:lang: en
:disqus_identifier: /2015/05/live-india-stock-market-indices-on-your-terminal.html

**Live BSE and NSE index on your bash terminal**

|stockmarketindia|

The script get the live index from BSE and NSE stock market.

How to Use
----------

- Download the script from github `stockmarketindia.py <stockmarketindiapy_>`_
- Copy the file into ``/usr/bin`` folder.
- Run ``stockmarketindia`` anywhere from terminal.

.. code-block:: bash

	wget --no-check-certificate https://gist.githubusercontent.com/arulrajnet/21addbacdbdfd6e190f4/raw/stockmarketindia.py
	chmod +x stockmarketindia.py
	sudo cp stockmarketindia.py /usr/bin/stockmarketindia


API Used
--------

The python script using google finance API. http://finance.google.com/finance/info?client=ig&q=INDEXBOM:SENSEX


Indexes are Included
--------------------

**BSE**

.. code-block:: text

	INDEXBOM:SENSEX
	INDEXBOM:BSE-100
	INDEXBOM:BSE-200
	INDEXBOM:BSE-500
	INDEXBOM:BSE-SMLCAP
	INDEXBOM:BSE-MIDCAP

**NSE**

.. code-block:: text

	NSE:NIFTY
	NSE:NIFTYJR

.. |stockmarketindia| image:: http://1.bp.blogspot.com/-fDoy3dPAOBQ/VUXc8-MHu3I/AAAAAAAAAus/YhaywsrtU4g/s640/stockmarketindia.png
	:target: http://1.bp.blogspot.com/-fDoy3dPAOBQ/VUXc8-MHu3I/AAAAAAAAAus/YhaywsrtU4g/s1600/stockmarketindia.png
.. _stockmarketindiapy: https://gist.githubusercontent.com/arulrajnet/21addbacdbdfd6e190f4
