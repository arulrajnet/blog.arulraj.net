Multiple mysql instances in windows
###################################
:date: 2012-05-02 13:39
:author: arul
:category: Database
:tags: mysql, Tips &amp; Tricks, windows
:slug: multiple-mysql-instances-in-windows
:status: published

Now again windows stuff... I am using windows OS in office 😌... This
post is about a simple tweaks about running multiple mysql instance in
one windows machine. Each instance runs in a different port and behaves
as a dedicated standalone server.

|mysql multiple instances|

**Why multiple instances..?**

  If you are a developer its for you. Sometimes you need to test your
  application with different type of data (like QA, Production) to
  replicate some error and etc., At that time no need to drop your old
  database and put the new one. Just use this and change the db port in
  your application configuration. This will be helpful for system
  administrators also to provide database service to his users.

**Requirement:**

-  mysql installed windows machine
-  Administrative privileges for that machine

For me mysql installed location is e:\\softs\\mysql\\


**Steps:**

Create [instances\\production] with in mysql installed directory (you can create anywhere). Better do everything in command prompt. 

.. code-block:: text

    e:
    cd \softs\mysql\
    md instances\production


Copy your data and share folder to production folder

.. code-block:: text

    copy data instances\production\
    copy share instances\production\


To create your custom ini file copy my.ini file and edit

.. code-block:: text

    copy my.ini instances\production.ini

Edit Production.ini
-------------------

- change port as 3307 under [client] and [mysqld] section
- Change basedir and datadir in that ini file

`Click Here <http://files.arulraj.net/code/database/production.ini>`__ for my production.ini file

Now add your custom ini in system starup

.. code-block:: text

    mysqld --install mysqldproduction --defaults-file="E:\softs\mysql\instances\production.ini"

Now goto Control Panel → Administrative tools → Services. Then search
for 'mysqldproduction' and start service. 

OR

.. code-block:: text

    net start mysqldproduction


You may think all is done. But after this only I faced problems.

**Cannot find the file specified:**

When I try to start that service "System error has occurred. The system cannot find the file specified."

There is registry changes needed to fix that issue

- To open registry editor Start → Run
- Type 'regedit' and enter.
- Next, browse to the registry key named: HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\mysqldproduction\\ImagePath
- Now you can see there is *no double quotes* in that --defaults-file so change ImagePath to

.. code-block:: bash

    "E:\softs\mysql\bin\mysqld" --defaults-file="E:\softs\mysql\instances\production.ini" mysqldproduction


Now start that service.

Keep watching Event Viewer. That is the best place to get debug information. Again I am getting error while starting server

|Event viewer for mysql|

**Can't find messagefile:**

The error is

.. code-block:: text

  System error 1067 has occurred.
  The process terminated unexpectedly.
  Can't find messagefile 'E:\softs\mysql\instances\production\share\errmsg.sys'

**Fix:**

  Just copy errmsg.sys file from [MYSQL_BASE]\share\english\ to that instances\production\share folder

Now everything is fine. Service will start successfully.

.. |mysql multiple instances| image:: http://1.bp.blogspot.com/-AJSmo9CM1fk/T6Fyl-FmAQI/AAAAAAAAPWg/EnHRjYBPCK0/s400/Multipleinstances.png
   :target: http://1.bp.blogspot.com/-AJSmo9CM1fk/T6Fyl-FmAQI/AAAAAAAAPWg/EnHRjYBPCK0/s1600/Multipleinstances.png
.. |Event viewer for mysql| image:: http://3.bp.blogspot.com/-khW4T_J1vso/T6GMNPk7tPI/AAAAAAAAPW4/q29gl6NoL3g/s400/event-viewer.PNG
   :target: http://3.bp.blogspot.com/-khW4T_J1vso/T6GMNPk7tPI/AAAAAAAAPW4/q29gl6NoL3g/s1600/event-viewer.PNG
