Jsp to Servlet converter
########################
:date: 2010-04-22 09:45
:author: arul
:category: Programming
:tags: java
:slug: jsp-to-servlet-converter

**Jsp to Servlet converter**

|image0|

Here is the Ant build file to convert jsp file to servlet file.

jspc (JavaServerPages Compiler) tool is helping to convert the jsp.
The requirements are you need

-  java sdk
-  apache tomcat
-  ant

.. code-block:: xml

  <project name="Test" default="compile" basedir=".">

  <description>

  JSP to Servlet Converter

  </description>

  <property name="name" value="JSP to Servlet" />

  <property environment="env" />

  <property name="ANT_HOME" value="${env.ANT_HOME}" />

  <property name="TOMCAT_HOME" value="D:\server\Tomcat 5.5" />

  <target name="init" description="Initialization" >

  <path id="tomcat.classpath">

  <fileset dir="${TOMCAT_HOME}\common\lib">

  <include name="*.jar" />

  </fileset>

  </path>

  <path id="ant.classpath">

  <fileset dir="${ANT_HOME}\lib">

  <include name="*.jar"/>

  </fileset>

  </path>

  <path id="webapp.classpath">

  <fileset dir=".\WEB-INF\lib">

  <include name="*.jar" />

  </fileset>

  </path>

  </target>

  <target name="compile" depends="init" description="compile the source" >

  <mkdir dir="./out" />

  <jspc srcdir="."

  destdir="out"

  verbose="9">

  <classpath>

  <path refid="tomcat.classpath" />

  <path refid="ant.classpath" />

  <path refid="webapp.classpath" />

  </classpath>

  <include name="*.jsp" />

  </jspc>

  </target>

  <target name="build" depends="compile"/>

  <target name="clean" description="clean the directories">

  <delete dir="./out" />

  </target>

  </project>

.. |image0| image:: http://www.socialbc.com/files/active/1/JSP_LOGO_RGB.jpg
