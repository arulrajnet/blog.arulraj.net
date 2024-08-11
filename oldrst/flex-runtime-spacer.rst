Flex runtime spacer
###################
:date: 2011-04-03 06:39
:author: arul
:category: Programming
:tags: Actionscript, Flash
:slug: flex-runtime-spacer
:disqus_identifier: /2011/04/flex-runtime-spacer.html

I am using Flex 4 for one of my Flex project. That project needs some dynamic spacing between the components. Here is the example code for the runtime spacer. I am using spark components here.

Code:

.. code-block:: flex

	<?xml version="1.0" encoding="utf-8"?>

	<s:Application name="Spark_Spacer_Test"
		xmlns:fx="http://ns.adobe.com/mxml/2009"
		xmlns:s="library://ns.adobe.com/flex/spark"
		xmlns:mx="library://ns.adobe.com/flex/mx" >

	<s:controlBarContent>
		<s:Label text="Space (px):" />
		<s:HSlider id="sl" minimum="0" maximum="600" value="200" />
	</s:controlBarContent>

	<s:HGroup top="20" horizontalCenter="0">
		<s:VGroup>
			<s:Button id="button1" label="Me" />
		</s:VGroup>
		<s:VGroup id="vSpacer" width="{sl.value}" >
			<s:Rect width="{sl.value}" height="0" />
		</s:VGroup>
		<s:VGroup>
			<s:Button id="button2" label="You" />
		</s:VGroup>
	</s:HGroup>

	</s:Application>

Running example:


.. raw:: html

	<embed src="https://files.arulraj.net/code/flash/example/RuntimeSpacer.swf" width="500" height="300"></embed>
