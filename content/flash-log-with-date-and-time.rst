Flash Log with date and time
############################
:date: 2010-11-16 15:50
:author: arul
:category: Flash
:tags: Browser, Flash, Programming
:slug: flash-log-with-date-and-time

**Flash trace with Date and Time**

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image0|

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

When i am work with a Difficult Flex application its hard to find which
log is come first and which one come second in the flashlog trace. I
searching for any log4j api like in flex. Yes i got.. Flex have that
inbuit. Here i share that how to i use in my project... The Class is
"**TraceTarget**\ "... Using that class you can trace your log in
different way like Debug, Info, Warn and Error.. Here is My example

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

.. raw:: html

   <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="300" height="150" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0">

.. raw:: html

   <embed type="application/x-shockwave-flash" width="300" height="150" src="http://arulraj.net/wp-content/uploads/2010/11/sharedaaExample.swf">
   </embed>
   </object>

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

sharedaaExample.mxml

.. raw:: html

   </div>

| [xml]
|  <?xml version="1.0" encoding="utf-8"?>
|  <mx:Application xmlns:mx="http://www.adobe.com/2006/mxml"
|  xmlns:sharedaa="com.sharedaa.\*"
|  creationComplete="creationComplete()"
|  preinitialize="initLogging()">
|  <mx:Script><![CDATA[
|  import mx.logging.Log;
|  import mx.logging.ILogger;
|  import mx.logging.LogEventLevel;

import mx.logging.targets.TraceTarget;

| import flash.ui.ContextMenu;
|  import flash.ui.ContextMenuItem;
|  import flash.net.navigateToURL;
|  import flash.net.URLRequest;

import flash.events.ContextMenuEvent;

import flash.display.StageDisplayState;

private var chatContextMenu:ContextMenu;

| private function initLogging():void {
|  // Create a target.
|  var logTarget:TraceTarget = new TraceTarget();

| // Log only messages for the following packages
|  logTarget.filters=["com.sharedaa.\*"];

| // Log all log levels.
|  logTarget.level = LogEventLevel.ALL;

| // Add date, time, category, and log level to the output.
|  logTarget.includeDate = true;
|  logTarget.includeTime = true;
|  logTarget.includeCategory = true;
|  logTarget.includeLevel = true;

| // Begin logging.
|  Log.addTarget(logTarget);
|  }

| private function addContextMenu():void {
|  chatContextMenu = new ContextMenu();
|  chatContextMenu.hideBuiltInItems();
|  var item:ContextMenuItem = new ContextMenuItem("www.arulraj.net");
|  item.addEventListener("menuItemSelect",openNewWindow);
|  chatContextMenu.customItems.push(item);
|  this.contextMenu = chatContextMenu;
|  }

| private function openNewWindow(event:ContextMenuEvent):void {
|  navigateToURL(new URLRequest("http://www.arulraj.net"),"\_blank");
|  }

| private function creationComplete():void {
|  addContextMenu();
|  main.initMain();
|  main.printLog();
|  }
|  ]]></mx:Script>
|  <mx:Canvas id="sharedaa">
|  <mx:Canvas id="mainCanvas" x="0" y="0">
|  <sharedaa:Main x="0" y="0" id="main">
|  </sharedaa:Main>
|  <mx:Label text="Example for Trace with Time" />
|  </mx:Canvas>
|  </mx:Canvas>
|  </mx:Application>
|  [/xml]

And the Actionscript file is

Main.as

| [as3]
|  package com.sharedaa {

| import mx.containers.VBox;
|  import mx.logging.Log;
|  import mx.logging.ILogger;

public class Main extends VBox {

private static var LOG:ILogger = Log.getLogger('com.sharedaa.Main');

| public function initMain():void {
|  LOG.debug("intialize main");
|  }

| public function printLog():void {
|  LOG.info("This is a info log");
|  LOG.debug("here is a debug log");
|  LOG.warn("display your warnings here");
|  LOG.error("This is a error");
|  }

| }
|  }
|  [/as3]

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image1|

.. raw:: html

   </div>

If you know better than this reply your ideas in comments...

.. |image0| image:: http://3.bp.blogspot.com/_X5tq9y9xv2s/TOLw1JAze1I/AAAAAAAAAjY/ht0kfAZ_v5A/s320/Flex+with+Log.png
   :target: http://3.bp.blogspot.com/_X5tq9y9xv2s/TOLw1JAze1I/AAAAAAAAAjY/ht0kfAZ_v5A/s1600/Flex+with+Log.png
.. |image1| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TOL8Ey1125I/AAAAAAAAAjc/BzeYVgfdvfI/s320/flash+log+with+time.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TOL8Ey1125I/AAAAAAAAAjc/BzeYVgfdvfI/s1600/flash+log+with+time.png
