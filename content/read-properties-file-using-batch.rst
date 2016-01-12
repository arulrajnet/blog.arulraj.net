Read properties file using Batch
################################
:date: 2010-03-24 04:32
:author: arul
:category: Programming
:tags: scripting, windows
:slug: read-properties-file-using-batch

**Read a properties file using bat file**

|image0|

i want to read a below property file and get the particular key value

My properties file look like

.. code-block:: properties

  name=arulraj.net
  version=1.0.2
  date=24/March/2010


I want get the version from the properties file. you can do this by
various method.

**Using Type function:**

.. code-block:: text

  C:\Users\Arul\Desktop>type test.properties | find "version"

There is disadvantage with this method you could not store that value in
a variable.

**Using For Loop:**

.. code-block:: text

  C:\Users\Arul\Desktop>FOR /F %i IN (test.properties) DO echo %i

using this command you can read that file by line by line.

.. code-block:: text

  FOR /F "eol=; tokens=2,2 delims==" %i IN (test.properties) DO echo %i

Using this commend you can get the values only.

eol is End of Line

tokens is specify the which tokens are displayed - 2,2 means only the
second token will be displayed

delims is the deliminator . this is the separator

.. code-block:: text

  FOR /F "eol=; tokens=2,2 delims==" %i IN ('findstr /i "version" test.properties') DO set version=%i

Using *findstr* get the correct string from the properties file and give
as a input to the for loop. That for loop process the result and set
that value to the variable version.

findstr /i means is not a case sensitive one

using echo you can get the value.

``echo %version%``

When you using in a bat add a % befor %i. That is Look like

.. code-block:: text

  FOR /F "eol=; tokens=2,2 delims==" %%i IN ('findstr /i "version" test.properties') DO 
    set version=%%i
    echo %version%

.. |image0| image:: http://2.bp.blogspot.com/_X5tq9y9xv2s/Srs4KNLAw0I/AAAAAAAAAFw/YgXxL4EMQe0/s400/MS-DOS-Batch-File.png
   :target: http://2.bp.blogspot.com/_X5tq9y9xv2s/Srs4KNLAw0I/AAAAAAAAAFw/YgXxL4EMQe0/s1600-h/MS-DOS-Batch-File.png
