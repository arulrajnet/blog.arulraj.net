Flex videodisplay fullscreen like youtube
#########################################
:date: 2013-04-11 11:29
:author: arul
:category: Flash
:tags: Actionscript, Flash
:slug: flex-videodisplay-fullscreen-like-youtube
:status: published

**Videodisplay in whole screen / Full screen particular component**

After a long time I came with a new post in flex. Yes fullscreen in
flex..!!! Fullscreening a whole app is very simple. You can
full screening by simply changing the display state of your application.
But it will be tricky if you are try to fullscreen a particular
component in an application. In this post I am taking videodisplay
component in a video chat application.

Still you can fullscreen a component using fullScreenSourceRect property
of stage.

    stage.fullScreenSourceRect = new Rectangle (0,0,320,240);

But It is like zooming a component. Its not good such as videodisplay
component. So I came up with an idea. Here its

-  Get that object of element which you are going to make fullscreen.
-  Remove it from parent object.
-  Add that element into stage.
-  Then resize that element to stage width and height.
-  While existing from fullscreen remove from stage and add back to
   parent component.

| [as3]
|  protected function
  fullScreenButton\_clickHandler(event:MouseEvent):void
|  {
|  var liveVideo:Object = liveVideoDisplay.getChildByName("liveVideo");
|  videoBox.removeElement(liveVideoDisplay);
|  stage.addChild(liveVideoDisplay);
|  stage.displayState = StageDisplayState.FULL\_SCREEN;
|  liveVideo.width = stage.width;
|  liveVideo.height = stage.height;
|  stage.addEventListener(FullScreenEvent.FULL\_SCREEN,
  fullScreenHandler);
|  }
|  [/as3]

`View
source <http://www.arulraj.net/labs/flash/example/fullscreen/srcview/>`__
is enabled.

[iframe
src="http://www.arulraj.net/labs/flash/example/fullscreen/fullscreen.html"
width="610" height="300"]
