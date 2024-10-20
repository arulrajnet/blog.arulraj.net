---
title: Flash Log with date and time
date: 2010-11-16 15:50:00
author: arul
category: Flash
tags: Browser,Flash,Programming
slug: flash-log-with-date-and-time
disqus_identifier: /2010/11/flash-log-with-date-and-time.html
status: published
---

**Flash trace with Date and Time**

[![image0](http://3.bp.blogspot.com/_X5tq9y9xv2s/TOLw1JAze1I/AAAAAAAAAjY/ht0kfAZ_v5A/s320/Flex+with+Log.png)](http://3.bp.blogspot.com/_X5tq9y9xv2s/TOLw1JAze1I/AAAAAAAAAjY/ht0kfAZ_v5A/s1600/Flex+with+Log.png)

When i am work with a Difficult Flex application its hard to find which
log is come first and which one come second in the flashlog trace. I
searching for any log4j api like in flex. Yes i got.. Flex have that
inbuit. Here i share that how to i use in my project\... The Class is
\"\*\*TraceTarget\*\*\"\... Using that class you can trace your log in
different way like Debug, Info, Warn and Error.. Here is My example

<!--  TODO : pelican better_figures_and_images is failed because of object data is null -->
<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="300" height="150" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0">
  <embed type="application/x-shockwave-flash" width="300" height="150" src="http://files.arulraj.net/code/flash/example/LogExample/logexample.swf">
  </embed>
</object>

**sharedaaExample.mxml**

``` mxml
<?xml version="1.0" encoding="UTF-8"?>
<mx:Application xmlns:mx="http://www.adobe.com/2006/mxml" xmlns:sharedaa="com.sharedaa.\*" creationComplete="creationComplete()" preinitialize="initLogging()">
  <mx:Script>
  <![CDATA[
   import mx.logging.Log;
   import mx.logging.ILogger;
   import mx.logging.LogEventLevel;
   import mx.logging.targets.TraceTarget;
   import flash.ui.ContextMenu;
   import flash.ui.ContextMenuItem;
   import flash.net.navigateToURL;
   import flash.net.URLRequest;

   import flash.events.ContextMenuEvent;

   import flash.display.StageDisplayState;

   private var chatContextMenu: ContextMenu;

   private function initLogging(): void {
     // Create a target.
     var logTarget: TraceTarget = new TraceTarget();

     // Log only messages for the following packages
     logTarget.filters = ["com.sharedaa.\*"];

     // Log all log levels.
     logTarget.level = LogEventLevel.ALL;

     // Add date, time, category, and log level to the output.
     logTarget.includeDate = true;
     logTarget.includeTime = true;
     logTarget.includeCategory = true;
     logTarget.includeLevel = true;

     // Begin logging.
     Log.addTarget(logTarget);
   }

   private function addContextMenu(): void {
     chatContextMenu = new ContextMenu();
     chatContextMenu.hideBuiltInItems();
     var item: ContextMenuItem = new ContextMenuItem("www.arulraj.net");
     item.addEventListener("menuItemSelect", openNewWindow);
     chatContextMenu.customItems.push(item);
     this.contextMenu = chatContextMenu;
   }

   private function openNewWindow(event: ContextMenuEvent): void {
     navigateToURL(new URLRequest("http://www.arulraj.net"), "\_blank");
   }

   private function creationComplete(): void {
     addContextMenu();
     main.initMain();
     main.printLog();
   }
   ]]>
  </mx:Script>
  <mx:Canvas id="sharedaa">
    <mx:Canvas id="mainCanvas" x="0" y="0">
      <sharedaa:Main x="0" y="0" id="main" />
      <mx:Label text="Example for Trace with Time" />
    </mx:Canvas>
  </mx:Canvas>
</mx:Application>
```

And the Actionscript file is

**Main.as**

``` as3
package com.sharedaa {

  import mx.containers.VBox;
  import mx.logging.Log;
  import mx.logging.ILogger;

  public class Main extends VBox {

    private static var LOG: ILogger = Log.getLogger('com.sharedaa.Main');

    public function initMain(): void {
      LOG.debug("intialize main");
    }

    public function printLog(): void {
      LOG.info("This is a info log");
      LOG.debug("here is a debug log");
      LOG.warn("display your warnings here");
      LOG.error("This is a error");
    }
  }
}
```

[![image1](http://4.bp.blogspot.com/_X5tq9y9xv2s/TOL8Ey1125I/AAAAAAAAAjc/BzeYVgfdvfI/s320/flash+log+with+time.png)](http://4.bp.blogspot.com/_X5tq9y9xv2s/TOL8Ey1125I/AAAAAAAAAjc/BzeYVgfdvfI/s1600/flash+log+with+time.png)

If you know better than this reply your ideas in comments\...
