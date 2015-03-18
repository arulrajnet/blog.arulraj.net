Multiple mysql instances in windows
###################################
:date: 2012-05-02 13:39
:author: arul
:category: Database
:tags: mysql, Tips &amp; Tricks, windows
:slug: multiple-mysql-instances-in-windows
:status: published

Now again windows stuff... I am using windows OS in office :(... This
post is about a simple tweaks about running multiple mysql instance in
one windows machine. Each instance runs in a different port and behaves
as a dedicated standalone server.

[caption id="" align="aligncenter" width="400" caption="multiple mysql
in one machine"]\ |mysql multiple instances|\ [/caption]

| **Why multiple instances..?**
|  If you are a developer its for you. Sometimes you need to test your
  application with different type of data (like QA, Production) to
  replicate some error and etc., At that time no need to drop your old
  database and put the new one. Just use this and change the db port in
  your application configuration. This will be helpful for system
  administrators also to provide database service to his users.

Requirement:

-  mysql installed windows machine
-  Administrative privileges for that machine

.. raw:: html

   <div>

For me mysql installed location is e:\\softs\\mysql\\

.. raw:: html

   </div>

.. raw:: html

   <div>

**Steps:**

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   <ol>
   <li>

Create [instances\\production] with in mysql installed directory (you
can create anywhere). Better   do everything in command prompt. 

.. raw:: html

   </li>

-  [bash]
    e:
    cd \\softs\\mysql\\
    md instances\\production
    [/bash]
-  

.. raw:: html

   <li>

Copy your data and share folder to production folder

.. raw:: html

   </li>

-  [bash]
    copy data instances\\production\\
    copy share instances\\production\\
    [/bash]

.. raw:: html

   <li>

To create your custom ini file copy my.ini file and edit

.. raw:: html

   </li>

-  [bash]
    copy my.ini instances\\production.ini
    [/bash]

.. raw:: html

   <li>

Open production.ini and change port as 3307 under [client] and [mysqld]
section

.. raw:: html

   </li>
   <li>

Change basedir and datadir in that ini file.
`Clickhere <http://arulraj.net/labs/downloads/softs/database/production.ini>`__
for my example file

.. raw:: html

   </li>
   <li>

Now add your custom ini in system starup

.. raw:: html

   </li>

-  [bash]
    mysqld --install mysqldproduction
   --defaults-file="E:\\softs\\mysql\\instances\\production.ini"
    [/bash]

.. raw:: html

   <li>

Now goto Control Panel → Administrative tools → Services. Then search
for 'mysqldproduction' and start service. OR

.. raw:: html

   </li>

-  [bash]
    net start mysqldproduction
    [/bash]

.. raw:: html

   </ol>

.. raw:: html

   </div>

You may think all is done. But after this only I faced problems.

| **Cannot find the file specified:**
|  When I try to start that service "System error has occurred.The
  system cannot find the file specified."

Open your registry editor at:

.. raw:: html

   <ol>
   <li>

Start → Run

.. raw:: html

   </li>
   <li>

type 'regedit' and enter.

.. raw:: html

   </li>
   <li>

Next, browse to the registry key
named: HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\mysqldproduction\\ImagePath

.. raw:: html

   </li>
   <li>

Now you can see there is no double quotes in that --defaults-file so
change ImagePath to

.. raw:: html

   </li>

-  [bash]
    "E:\\softs\\mysql\\bin\\mysqld" --defaults-file="E:\\softs\\mysql\\instances\\production.ini" mysqldproduction
    [/bash]

.. raw:: html

   <li>

Now start that service.

.. raw:: html

   </li>
   </ol>

Keep watching Event Logger. That is the best place to get debug
information. Again error while starting server

[caption id="" align="aligncenter" width="400" caption="Event viewer for
mysql"]\ |Event viewer for mysql|\ [/caption]

| **Can't find messagefile:**
|  The error is
|  [text]
|  System error 1067 has occurred.

The process terminated unexpectedly.

| Can't find messagefile
  'E:\\softs\\mysql\\instances\\production\\share\\errmsg.sys'
|  [/text]

| **Fix:**
|  Just copy errmsg.sys file from [MYSQL\_BASE]\\share\\english\\ to
  that instances\\production\\share folder

Now everything is fine. Service will start successfully.

.. |mysql multiple instances| image:: http://1.bp.blogspot.com/-AJSmo9CM1fk/T6Fyl-FmAQI/AAAAAAAAPWg/EnHRjYBPCK0/s400/Multipleinstances.png
   :target: http://1.bp.blogspot.com/-AJSmo9CM1fk/T6Fyl-FmAQI/AAAAAAAAPWg/EnHRjYBPCK0/s1600/Multipleinstances.png
.. |Event viewer for mysql| image:: http://3.bp.blogspot.com/-khW4T_J1vso/T6GMNPk7tPI/AAAAAAAAPW4/q29gl6NoL3g/s400/event-viewer.PNG
   :target: http://3.bp.blogspot.com/-khW4T_J1vso/T6GMNPk7tPI/AAAAAAAAPW4/q29gl6NoL3g/s1600/event-viewer.PNG
