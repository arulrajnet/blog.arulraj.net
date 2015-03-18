Print screen using java
#######################
:date: 2010-06-23 13:20
:author: arul
:category: Programming
:tags: java
:slug: print-screen-using-java

Is there any api for capure my screen ..?
  You don't need any api. Java have the inbuild functionalities for this. Using the Robot class you can
  print your screen. Here is the code sample and explanation.

*Example code:*

.. code-block:: java

  import java.awt.image.BufferedImage;
  import java.awt.Rectangle;
  import java.awt.Dimension;
  import java.awt.Toolkit;
  import java.awt.Robot;
  import java.io.File;
  import javax.imageio.ImageIO;

  class ScreenRecorder {
    public static void main(String args[]) {
      try {
        Toolkit tool = Toolkit.getDefaultToolkit();
        Dimension d = tool.getScreenSize();
        Rectangle rect = new Rectangle(d);
        Robot robot = new Robot();
        Thread.sleep(2000);
        File f = new File("screenshot.jpg");
        BufferedImage img = robot.createScreenCapture(rect);
        ImageIO.write(img,"jpeg",f);
        tool.beep();
      } catch(Exception e){
        e.printStackTrace();
      }
    }
  }

-  Import the classes you need.
-  Using the ToolKit you can get your screensize.
-  Form a Rectangle object with this width and height
-  capture the screen for this full width and height.
-  There is a Thread.sleep for 2 sec for my convenience
-  You can specify your own width and height by

    rect = new Rectangle(640,480);

I think this is help you more. Now am working on record the desktop
using java. Soon i will come up with good product.

*Captured Image:*

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image0|

.. raw:: html

   </div>

.. |image0| image:: http://3.bp.blogspot.com/_X5tq9y9xv2s/TCJeHxGfD1I/AAAAAAAAAag/ERj3EzaMTIA/s320/screenshot.jpg
   :target: http://3.bp.blogspot.com/_X5tq9y9xv2s/TCJeHxGfD1I/AAAAAAAAAag/ERj3EzaMTIA/s1600/screenshot.jpg
