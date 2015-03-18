XML to Actionscript class Turbosqel / ASML example
##################################################
:date: 2013-11-21 09:43
:author: arul
:category: Programming
:tags: Actionscript, Flash, xml
:slug: xml-to-actionscript-class-turbosqel-asml-example
:status: published

**Turbosqel / ASML example**

I found a useful third party actionscript libraris from
githup \ https://github.com/turbosqel. I mostly used these as3SupportLib
and ASML lib all of my flex projects. But initially I were struggle to
find out the example over the internet. So I am writing here one of the
feature of that libraries. 

I am going to explain how to assign value to some variables from remote
xml.

[iframe
src="http://arulraj.net/labs/flash/example/ASMLExample/ASMLExample.html"
width="270" height="250"]

[`View
Source <http://arulraj.net/labs/flash/example/ASMLExample/srcview/index.html>`__
Enabled]

Below code snippet for loading xml from server using as3SupportLib

| [as3]
|  protected var configResource:Resource;
|  protected function onLoadAgain(event:MouseEvent):void
|  {
|  configResource = ResourceManage.setExternal("config.xml");
|  DownloadManager.addEventListener(DownloadManagerEvent.COMPLETE,
  onDownloadComplete);
|  }
|  [/as3]

The below code snippet for XML to Object

| [as3]
|  private function onDownloadComplete(event:DownloadManagerEvent):void
  {
|  var configXml:XML = new XML(configResource.loaderInfo.source);
|  var xmlResult:Array = ASMLManager.parseXML(configXml,this);
|  }
|  [/as3]

For that works that config.xml should be written in certain way. Here is
the doc for how to write
xml \ https://github.com/turbosqel/ASML/blob/master/README.textile

My XML is
here \ http://arulraj.net/labs/flash/example/ASMLExample/config.xml
