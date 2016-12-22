Small FB hack
#############
:date: 2011-02-25 14:25
:author: arul
:category: Programming
:tags: Browser, hacking, java
:slug: small-fb-hack
:disqus_identifier: /2011/02/small-fb-hack.html

Don't think I had broke the security system of facebook and got others personal information. I am not a such a knowledge person 😄 .. Just see the below picture

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image0|

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Is this possible a human can click 2000 mouse click per second. No way... We broke a facebook application Click! Click! Click!... The application for calculate mouse clicking capacity with in 10 seconds and you can share it in your wall.. simple... You can crack this using java robot class...

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

A two line of code can do this..

.. raw:: html

   </div>

.. code-block:: text

    rb.mousePress(InputEvent.BUTTON1_MASK);
    rb.mouseRelease(InputEvent.BUTTON1_MASK);

Using this i can made upto 15,000 clicks. I am using openjdk in ubuntu. I could not break my friend (Ponraj) record. May be bad thread handing mechanism in openjvm.. Or OS dependency i am not go deep with in that... He using some better code than me. I think he used `Selenium <http://seleniumhq.org/download/>`__ with this. Need to discuss with him and will update here... And i forget to mention your browser also have some limitation... 😌

Here is the code I used...

.. code-block:: java

 import java.awt.AWTException;
 import java.awt.Robot;
 import java.awt.event.InputEvent;

 public class FBClick implements Runnable {

  private static Boolean timeout = false;

  @SuppressWarnings("deprecation")
  public static void main(String d[]) throws InterruptedException,
  AWTException {
    Runnable fb = new FBClick();
    Thread th[] = new Thread[2];
    Thread.sleep(6000);
    for (int i = 0; i < th.length; i++) {
      th[i] = new Thread(fb);
      th[i].start();
    }

    Long startTime = System.currentTimeMillis();
    while (true) {
      Long endTime = System.currentTimeMillis();
      if (endTime - startTime > 11000) {
        for (int i = 0; i < th.length; i++) {
          th[i].stop();
        }
        timeout = true;
        break;
      }
      Thread.sleep(3000);
    }
    System.out.println("The end");
  }

  @Override
  public void run() {
    try {
      Robot rb = new Robot();
      while (!timeout) {
        rb.mousePress(InputEvent.BUTTON1_MASK);
        rb.mouseRelease(InputEvent.BUTTON1_MASK);
      }
    } catch (AWTException e) {
      e.printStackTrace();
    }
  }
 }

How to use this code..?

Compile and Run this java Code and place your mouse on START Button...

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image1|

.. raw:: html

   </div>

*Think like a programmer..* i copied this quote from him... 😄

.. |image0| image:: http://3.bp.blogspot.com/-QCzv73ZG5ZQ/TWgJLMnwG8I/AAAAAAAAAnY/WfoKhXl7jig/s400/fb_hack.png
   :target: http://www.facebook.com/permalink.php?story_fbid=191226034231536&id=100000324222880
.. |image1| image:: http://1.bp.blogspot.com/-H8OtXSjTogY/TWgPnMDeg0I/AAAAAAAAAng/24lE9fshwhg/s400/fb_click_apps.png
   :target: http://apps.facebook.com/swtsubqaslfoptcmo/
