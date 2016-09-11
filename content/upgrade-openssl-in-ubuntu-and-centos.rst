Upgrade openssl in Ubuntu and CentOS
####################################
:date: 2014-04-09 20:08
:author: arul
:category: Linux
:tags: commands, fix, ubuntu, how to, centos
:slug: upgrade-openssl-in-ubuntu-and-centos
:status: published

**Upgrade OpenSSL in Ubuntu and CentOS**

|OpenSSL Heartbleed|

Hope you know about openssl heartbleed bug. Don't know about, no problem go through it `http://heartbleed.com/ <http://heartbleed.com>`__ . The point here is you should upgrade your openssl. Because of this bug all linux variants release the patch for openssl. Here the steps for upgrade openssl both ubuntu and centos.

How to find I am using affected version...?
-------------------------------------------

**In ubuntu:**


Run this command

.. code-block:: bash

	openssl version -a

There you can find "built on" date. If that date is older than Apr 7.
Then you are using older version. You should upgrade your version.

.. code-block:: text

	OpenSSL 1.0.1 14 Mar 2012
	built on: Wed Jan 8 20:45:51 UTC 2014


**In CentOS:**


Same as above.

|Open SSL Old Version|

How to upgrade openssl..?
-------------------------

**In Ubuntu:**
          

.. code-block:: bash

	sudo apt-get update
	sudo apt-get install libssl1.0.0 openssl -y


**In CentOS:**
          

.. code-block:: bash

	sudo yum update
	sudo yum update openssl -y

How to check am I upgarded..?
-----------------------------

.. code-block:: bash

	openssl version -a | grep built

|OpenSSL New Version|

The date should greater than or equal to Apr 7.

Hey..!!! you are done. Happy secure linuxing... 😄

.. |OpenSSL Heartbleed| image:: http://4.bp.blogspot.com/-E5NogEilRNs/U0X3gzGooiI/AAAAAAAAVpo/ZZUTzTD_tuk/s640/openssl-logo-bug.png
   :target: http://4.bp.blogspot.com/-E5NogEilRNs/U0X3gzGooiI/AAAAAAAAVpo/ZZUTzTD_tuk/s1600/openssl-logo-bug.png
.. |Open SSL Old Version| image:: http://2.bp.blogspot.com/-ee9O8qZXTUA/U0X5haUOlfI/AAAAAAAAVp4/GoiBS0CgO38/s640/openssl-old-1.png
   :target: http://2.bp.blogspot.com/-ee9O8qZXTUA/U0X5haUOlfI/AAAAAAAAVp4/GoiBS0CgO38/s1600/openssl-old-1.png
.. |OpenSSL New Version| image:: http://3.bp.blogspot.com/-3hnS33ve4JM/U0X5hKOlqGI/AAAAAAAAVp0/ExBE5VMd-a8/s640/openssl-new-1.png
   :target: http://3.bp.blogspot.com/-3hnS33ve4JM/U0X5hKOlqGI/AAAAAAAAVp0/ExBE5VMd-a8/s1600/openssl-new-1.png
