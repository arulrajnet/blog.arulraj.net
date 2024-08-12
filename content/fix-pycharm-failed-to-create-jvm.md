---
title: Fix - Pycharm Failed to create JVM
date: 2014-10-03 12:12
author: arul
category: Tools
tags: IDE,java,python,programming
slug: fix-pycharm-failed-to-create-jvm
status: published
disqus_identifier: /2014/10/fix-pycharm-failed-to-create-jvm.html
---
-
**How to Run your Pycharm IDE under 64bit JVM..?**

[![Pycharm Error Code -4](http://4.bp.blogspot.com/-llWB2o4A5Ww/VC7ZhgH-j5I/AAAAAAAAWC4/wbtlkiYONLc/s320/pycharm-error-code.PNG){.align-middle}](http://4.bp.blogspot.com/-llWB2o4A5Ww/VC7ZhgH-j5I/AAAAAAAAWC4/wbtlkiYONLc/s1600/pycharm-error-code.PNG)

**What is the real issue..?**

First you should to know all jetbrains IDE\'s are written in Java. The
issue because of your pycharm needs more memory to process your projects
and files at the backend Java requires memory. But its not able to
acquire that much of memory. So its closed obtrubtly.

Everyone will say increase the JVM/Java max heap size in
`pycharm.properties` file. Then restart the pycharm. But thats not a
permanent solution.

The real problem is pycharm internally uses 32bit jvm which comes with
the installer package. The 32 bit JVM can allocate maximum 2GB of space
only.

**What is the solution for it..?**

So the fix is you have to start your pycharm with 64bit JVM. Here we
will see how to start with 64bit JVM. Three steps to fix that

-   Set the 64bit SDK as environmental variable
-   create properties for 64bit version
-   start the ide from .bat file

**Set 64Bit SDK:**

Before setting environmental variable you have to find out which version
of java you are using. To find out Open Command Prompt → Then run the
below command

> java -version

It should have the \"Java Hotspot(TM) 64-Bit Server\" line in the
output. If there is no Bit information then its 32bit java. Then proceed
furthur you have to download and install the 64bit JDK from
<http://java.com/>

[![Java Version](http://4.bp.blogspot.com/-dQGv7xsG25s/VC7ZizVLThI/AAAAAAAAWDI/55dvR_UwtM0/s320/pycharm-find-java-version.PNG)](http://4.bp.blogspot.com/-dQGv7xsG25s/VC7ZizVLThI/AAAAAAAAWDI/55dvR_UwtM0/s1600/pycharm-find-java-version.PNG)

Then open Control Panel → Edit Environmental Variable for Your Account

In User variables set `PYCHARM_SDK` and path will be your 64 bit java
version

[![PYCHARM_JDK](http://2.bp.blogspot.com/-8K20N9lH9SQ/VC7ZhrcJ7II/AAAAAAAAWC8/Av1sErElf-c/s320/pycharm-env.PNG)](http://2.bp.blogspot.com/-8K20N9lH9SQ/VC7ZhrcJ7II/AAAAAAAAWC8/Av1sErElf-c/s1600/pycharm-env.PNG)

**Create properties file:**

For 64bit you have to create separate properties file for that.  Create
file named as `pycharm64.exe.vmoptions` in the root directory of IDE

``` text
-server
-Xms256m
-Xmx2048m
-XX:MaxPermSize=512m
-XX:ReservedCodeCacheSize=128m
-ea
-Dsun.io.useCanonCaches=false
-Djava.net.preferIPv4Stack=true
-Djsse.enableSNIExtension=false
-XX:+UseCodeCacheFlushing
-XX:+UseConcMarkSweepGC
-XX:SoftRefLRUPolicyMSPerMB=100
```

**To start:**

IDE should start with the pycharm.bat file.

This fix will work for other IDE such as WebStrom, PhpStrom, IntelliJ
and RubyMine from jetbrains also.

Basically you have to create `<product>64.exe.vmoptions` file. Set the
64bit Java environmental variable for that IDE. Then start the
`<product>.bat` file

**Environmental Variable for Different product:**

-   IDEA_JDK for IntelliJ IDEA
-   WEBIDE_JDK for PhpStorm and WebStorm
-   PYCHARM_JDK for PyCharm
-   RUBYMINE_SDK for RubyMine

To know about what environmental variable have to use, open
`<product>.bat` file. Then you will get to know.

[![pycharm.bat](http://2.bp.blogspot.com/-iTUeJ174ljc/VC7ZjyPDevI/AAAAAAAAWDQ/XhIp6aO88DY/s320/pycharm-startup-script.PNG)](http://2.bp.blogspot.com/-iTUeJ174ljc/VC7ZjyPDevI/AAAAAAAAWDQ/XhIp6aO88DY/s1600/pycharm-startup-script.PNG)

Read More at [intellij
Support](https://intellij-support.jetbrains.com/entries/23393413-The-JVM-could-not-be-started-The-main-method-may-have-thrown-an-exception)
