---
title: How to access external java libraries with in pentaho
date:   2014-09-24 12:38
author: arul
category:   Business intelligence
tags:   BI Tools, java, pentaho, how-to, Tools
slug:   how-to-access-external-java-libraries-with-in-pentaho
status:   published
disqus_identifier:    /2014/09/how-to-access-external-java-libraries-with-in-pentaho.html
---

**How to access external libraries with in pentaho..?**

[![Java Component in ETL
Flow](http://1.bp.blogspot.com/-AuXLtbyvurk/VCMQTRArekI/AAAAAAAAWCk/_qNXoURYSVY/s480/mongo-read-empty-java-write-csv.PNG)](http://1.bp.blogspot.com/-AuXLtbyvurk/VCMQTRArekI/AAAAAAAAWCk/_qNXoURYSVY/s1600/mongo-read-empty-java-write-csv.PNG)

Pentaho Data Integration Tool (PDI) is mainly used for Extraction,
Transformation, Load (ETL). They have their own
[components](http://wiki.pentaho.com/display/EAI/Pentaho+Data+Integration+Steps)
to do basic and advanced ETL operations.

## **Install**

-   Download and Extract of [Community
    edition](http://community.pentaho.com/projects/data-integration/) of
    PDI.
-   Extract the downloaded zip file as data-integration.
-   You need Java in your machine for PDI Tool to run.
-   To run PDI open spoon.bat in windows.

Here PDI / Pentaho Data Integration Tool / Spoon / Kettle all are mean
same.

You can run your own java code as a component in the ETL flow. For that
have the component called [User Defined Java
Class](http://wiki.pentaho.com/display/EAI/User+Defined+Java+Class).
Absolutely you will use external classes or jar\'s in your java
component. In this post will guide you to load those external jar\'s
while pentaho loads.

## Configure

-   Create `libext` folder with in data-integration.
-   Backup your `launcher.properties` file with in
    `data-integration/launcher` folder.
-   Then save below as launcher.properties in that folder

``` text
main=org.pentaho.di.ui.spoon.Spoon
libraries=../test:../lib:../libswt:../libext
classpath=../:../ui:../ui/images:../lib:../libext

system-property.pentaho.installed.licenses.file=${PENTAHO_INSTALLED_LICENSE_PATH}
```

-   Now copy your external / third party jars into libext folder
-   Now start the spoon.bat

### My setup

OS - Windows 7 64 bit

Java - Java 1.7.0_45 64 bit

PDI - pdi-ce-5.1.0.0-752.zip

### Note

Before adding any jar into libext have a look into
`data-integration/lib`. If the jar is already there you can directly use
that.

Using user defined class in your flow leads to increase your process
time. So use that if you really need it. Refer
<https://twitter.com/arulrajnet/status/514792905127370752>
