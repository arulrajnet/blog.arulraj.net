---
title: Batch file for building any java application
date: 2009-09-24 03:58:00
author: arul
category: Widget
tags: commands,Widget,windows,Programming
slug: batch-file-for-building-any-java-application
disqus_identifier: /2009/09/batch-file-for-building-any-java-application.html
status: published
---

**Batch file for building any java application**

[![image0](http://2.bp.blogspot.com/_X5tq9y9xv2s/Srs4KNLAw0I/AAAAAAAAAFw/YgXxL4EMQe0/s400/MS-DOS-Batch-File.png)](http://2.bp.blogspot.com/_X5tq9y9xv2s/Srs4KNLAw0I/AAAAAAAAAFw/YgXxL4EMQe0/s1600-h/MS-DOS-Batch-File.png)

**What is batch file\...?**

In DOS, OS/2, and Microsoft Windows, a batch file is a text file
containing a series of commands intended to be executed by the command
interpreter. Article on
[wikipedia](http://en.wikipedia.org/wiki/Batch_file)

This batch file contains the set of instruction to build a any java
application. To get the good result you follow the below folder
structure..

For example C:apache-tomcat-6.0.18webapps contains the many java web
application. place this batch file in webapps folder.

> -   The java files in webapps\<PROJECT_NAME\>src  folder. With in the
>     src folder u can follw the java package structure.
> -   The jar files for your application in webapps\<PROJECT_HOME\>lib
>     folder.
> -   Then run that batch file like

C:apache-tomcat-6.0.18webapps\> build.bat Library

> -   Here the Library is your project Home. you can use this bat file
>     anywhere not only for tomcat webapps folder.

Environment Variable Prequisites:

> 1.  JAVA_HOME       Must point at your Java Development Kit
>     installation.
> 2.  JAVA_OPTS       (Optional) Java runtime options.
> 3.  CATALINA_HOME        (Optional) May point at your Catalina
>     \"build\" directory.

**How to set JAVA_HOME \...?**

JAVA_HOME basically known as Java Environmental Variable.Refers from
[web](http://confluence.atlassian.com/display/CONF26/Set+JAVA_HOME+variable+in+Windows)

If you already know the install path for the Java or Software
Development Kit,skip this first two steps. Otherwise, find the install
path by following these instructions:

> 1.  Unless you changed the install path for the Java Developement Kit
>     during installation, it will be in a directory under
>     `C:\Program Files\Java`. Using Explorer, open the directory
>     `C:\Program Files\Java`
> 2.  Inside that path will be one or more subdirectories such as
>     `jdk1.5.0_08`. If you just installed the Java Development Kit, it
>     will be installed to the newest directory, which you can find by
>     sorting by date. For example, it may be installed in
>     `C:\Program Files\Java\jdk1.5.0_08`. This is the install path.

Once you have identified the JDK install path:

> 1.  Right click on the **My Computer** icon on your desktop and select
>     properties
> 2.  Click the **Advanced** Tab
> 3.  Click the **Environment Variables** button
> 4.  Under System Variable, click **New**
> 5.  Enter the variable name as `JAVA_HOME`
> 6.  Enter the variable value as the install path for the Development
>     Kit
> 7.  Click OK
> 8.  Click Apply Changes

[![image1](http://3.bp.blogspot.com/_X5tq9y9xv2s/Srs-dTRgMzI/AAAAAAAAAF4/VzLWmytRU4A/s400/JAVA_HOME.jpg)](http://3.bp.blogspot.com/_X5tq9y9xv2s/Srs-dTRgMzI/AAAAAAAAAF4/VzLWmytRU4A/s1600-h/JAVA_HOME.jpg)

**What is JAVA_OPTS \...?**

This JAVA_OPTS may increase your server performance. For example

`set JAVA_OPTS=-Xms128 -Xmx512`

The two extra parameters specified via JAVA_OPTS are as follows:

:   -Xms - the amount of memory that the JVM starts with. -Xmx - the
    maximum memory that the JVM may have.

List of Java Hotspot Option
[Here](http://java.sun.com/javase/technologies/hotspot/vmoptions.jsp).

**What is CATALINA_HOME\...?**

Set an environment variable CATALINA_HOME to the path of the directory
into which you have installed Tomcat.

For example :

`set CATALINA_HOME = C:\apache-tomcat-6.0.18`

**How this Batch File works \...?**

> Get the all jar files from \<PROJECT_HOME\>lib folder and set this as
> classpath.
>
> Then compile all java files inside the src folder. and build the class
> files inside the \<PROJECT_HOME\>WEB-INF Folder.

**How to Download this Batch file \...?**

You can download this batch file from
[Here](http://arulraj1985.googlepages.com/build.bat).

<http://arulraj1985.googlepages.com/build.bat>
