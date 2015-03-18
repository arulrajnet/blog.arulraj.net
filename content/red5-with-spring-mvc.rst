Red5 with Spring MVC
####################
:date: 2012-04-13 15:55
:author: arul
:category: Red5
:tags: java, red5, spring, Flash, Programming
:slug: red5-with-spring-mvc
:status: published

**Access Red5 context in spring MVC DispatcherServlet**

|image0|

Before we start, some prerequisites for reader.

-  How Spring MVC works.
   `tutorial <http://static.springsource.org/spring/docs/3.0.x/spring-framework-reference/html/mvc.html>`__
-  Basic knowledge about red5.

Then only you can understand clearly :) . If you don't have, no worries.
Having knowledge in core java and servlet is enough

Day by day I experienced in Red5. I will explain a useful enhancement
about red5. Let's start...

Red5 is an open source flash media server. If your webapplication is in
the same server you can build some interesting streaming apps by binding
your webapp and red5app. But you can not use red5 as a web application
server, because by default RTMPServlet support macromedia-fcs
(application/x-fcs) content type not http. But Internally Red5 uses
Tomcat and Spring. By simple tweaks you can add http support for your
red5 application.

So I add my own Red5DispatcherServlet in red5app web.xml to handle http
request.

add this in your web.xml

| [xml]
|  <servlet>
|  <servlet-name>red5Demo-web</servlet-name>
| 
  <servlet-class>com.demo.web.servlet.Red5DispatcherServlet</servlet-class>
|  <init-param>
|  <param-name>contextConfigLocation</param-name>
|  <param-value>
|  /WEB-INF/red5Demo-dispatcher-servlet.xml
|  </param-value>
|  </init-param>
|  </servlet>
|  [/xml]

All configurations files
in \ https://github.com/arulrajnet/red5Demo/tree/master/java/webapp/WEB-INF

You can use the default spring mvc DispatcherServlet. But problem is you
can't access the red5 context from your controller. It means all objects
loaded by red5 ContextLoggingListener can't be accessble from your web
context. Did you understand...?

ok. Usually spring DispatcherServlet creates one web context and sets
parents as ApplicationContext loaded by spring mvc
ContextLoaderListener. Did you notice in red5app web.xml file we are
using red5 own context loader listener. So if you use Spring mvc
DispatcherServlet there is no parent context.

To override this we have to set red5 ApplicationContext as
DispatcherServlet parent context. For that only I have some
customization

Red5DispatcherServlet.java

| [java]
|  package com.demo.web.servlet;

| import org.red5.logging.Red5LoggerFactory;
|  import org.slf4j.Logger;
|  import org.springframework.web.context.WebApplicationContext;
|  import
  org.springframework.web.context.support.WebApplicationContextUtils;
|  import org.springframework.web.servlet.DispatcherServlet;

public class Red5DispatcherServlet extends DispatcherServlet {

private static final long serialVersionUID = 1L;

private static final Logger LOG =
Red5LoggerFactory.getLogger(Red5DispatcherServlet.class, "red5Demo");

private WebApplicationContext parentContext;

| @Override
|  protected WebApplicationContext initWebApplicationContext() {
|  WebApplicationContext wac = null;
|  parentContext =
  WebApplicationContextUtils.getWebApplicationContext(getServletContext());
|  if (parentContext == null) {
|  parentContext = (WebApplicationContext)
  getServletContext().getAttribute(
|  WebApplicationContext.ROOT\_WEB\_APPLICATION\_CONTEXT\_ATTRIBUTE);
|  }
|  if (parentContext == null) {
|  LOG.error("No web application context found.");
|  } else {
|  wac = createWebApplicationContext(parentContext);
|  }

| setDetectAllHandlerAdapters(Boolean.TRUE);
|  setDetectAllHandlerMappings(Boolean.TRUE);
|  setDetectAllHandlerExceptionResolvers(Boolean.TRUE);
|  setDetectAllViewResolvers(Boolean.TRUE);

onRefresh(wac);

| String attrName = getServletContextAttributeName();
|  getServletContext().setAttribute(attrName, wac);
|  if (this.logger.isDebugEnabled()) {
|  this.logger.debug("Published WebApplicationContext of servlet '" +
  getServletName()
|  + "' as ServletContext attribute with name [" + attrName + "]");
|  }

| return wac;
|  }

| public WebApplicationContext getParentContext() {
|  return parentContext;
|  }

| public void setParentContext(WebApplicationContext parentContext) {
|  this.parentContext = parentContext;
|  }
|  }
|  [/java]

Then define your handlers and view resolvers in
red5Demo-dispatcher-servlet.xml

I have created one demo application for red5 with spring mvc. please
refer github red5Demo https://github.com/arulrajnet/red5Demo

To Download this code

Install Git then run the below command.

git clone git@github.com:arulrajnet/red5Demo.git

I will write a separate post for setup red5 development environment and
how to build that app.

.. |image0| image:: http://2.bp.blogspot.com/--6PGozKYyQY/T4ieL7Dv2KI/AAAAAAAAOjw/rUknwLPrOlY/s320/Untitled.png
   :target: http://2.bp.blogspot.com/--6PGozKYyQY/T4ieL7Dv2KI/AAAAAAAAOjw/rUknwLPrOlY/s1600/Untitled.png
