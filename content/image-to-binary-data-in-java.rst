Image to binary data in java
############################
:date: 2010-10-27 14:50
:author: arul
:category: Browser
:tags: java, xml
:slug: image-to-binary-data-in-java

**Image to binary data in java**

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image0|

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Today i learn a new thing. That is come across like this way.. I tried
to install "Bing" search provider to  my Mozilla Firefox. But that Bing
favicon is not shown on the search provider.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image1|

.. raw:: html

   </div>

.. raw:: html

   <p>

Download the mozilla firefox addon from here
https://addons.mozilla.org/en-US/firefox/addon/10434 . It gave an xml
file for me.

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

My internet connection is not available at that time. so the favicon
[http://www.bing.com/favicon.ico not downloaded] for Bing is not shown
for me. But the favicon for other search provider like google and amazon
are shown. So i thought this is some thing different. Find the path for
searchplugin in mozilla. In ubuntu the search provider location is

.. raw:: html

   </div>

    .. raw:: html

       <div class="separator" style="clear: both; text-align: left;">

    /usr/lib/firefox-addons/searchplugins/en-US

    .. raw:: html

       </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

For google and others the image tag is look like the below

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

.. code-block:: text

  <img alt="" width="16" height="16"
    />data:image/png;base64,AAABAAEAEBAAAAEAGABoAw.........


.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Now i realized we can use the binary data of the image as a src instead
of image url. Here the wiki page for that
http://en.wikipedia.org/wiki/Data_URI_scheme

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

You can use the binary data in "img" tag in html

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

.. code-block:: text

  <img alt="Embedded Image"
    src="data:image/png;base64,iVBORw0KGgoAAAAN................ />

So i write java program for to convert image to data. Here is the code
for your reference

.. raw:: html

   </div>

.. code-block:: java

 import java.awt.image.BufferedImage;
 import java.io.ByteArrayOutputStream;
 import java.io.File;

 import javax.imageio.ImageIO;

 import com.sun.org.apache.xerces.internal.impl.dv.util.Base64;

 public class Image2Base64 {

  public static void main(String args[]) {
    try {
      BufferedImage image = ImageIO.read(new File("favicon.png"));
      ByteArrayOutputStream baos = new ByteArrayOutputStream();
      ImageIO.write(image, "png", baos);
      String encodedImage = Base64.encode(baos.toByteArray());
      System.out.println(encodedImage);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
 }
.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Here is the Bing img in data format

.. raw:: html

   </div>

|Embedded Image|

Finally i Fix the Bing favicon problem in my Firefox search plugin

Steps:

-  Remove the Bing search plugin first.
-  Goto Manage Search Engine → Select Bing → Remove
-  Copy the below xml and save as bing.xml in
   "/usr/lib/firefox-addons/searchplugins/en-US" for ubuntu OR
   "C:\\Program Files\\Mozilla\\Firefox\\searchplugins" for windows
-  Restart your Firefox

.. code-block:: xml

  <?xml version="1.0" encoding="UTF-8"?>
  <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
  <ShortName>Bing</ShortName>
  <Tags>Bing</Tags>
  <Description>Bing. Search by Microsoft.</Description>
  <Contact>msosa@microsoft.com</Contact>
  <InputEncoding>UTF-8</InputEncoding>
  <SyndicationRight>limited</SyndicationRight>
  <Image width="16"
    height="16">data:image/x-icon;base64,AAABAAEAEBAAAAEAGABoAwAAFgAAACgAAAAQAAAAIAAAAAEAGAAAAAAAAAAAABMLAAATCwAAAAAAAAAAAAAVpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8ysf97zf+24%2F%2FF6f%2FF6f%2FF6f+K0%2F9QvP8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8krP+Z2P%2F%2F%2F%2F%2F%2F%2F%2F%2Fw+f%2FF6f%2FF6f%2Fi9P%2F%2F%2F%2F%2F%2F%2F%2F%2FT7v9Bt%2F8Vpv8Vpv8Vpv8Vpv%2FT7v%2F%2F%2F%2F%2Fw+f97zf8Vpv8Vpv8Vpv8Vpv9QvP%2FT7v%2F%2F%2F%2F%2Fw+f9Bt%2F8Vpv8Vpv97zf%2F%2F%2F%2F%2F%2F%2F%2F9QvP8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8krP%2Fi9P%2F%2F%2F%2F%2Fi9P8Vpv8Vpv+24%2F%2F%2F%2F%2F%2Fi9P8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv+K0%2F%2F%2F%2F%2F%2F%2F%2F%2F8Vpv8Vpv%2FF6f%2F%2F%2F%2F%2F%2F%2F%2F8krP8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv+n3v%2F%2F%2F%2F%2Fw+f8Vpv8Vpv%2FF6f%2F%2F%2F%2F%2F%2F%2F%2F+n3v8krP8Vpv8Vpv8Vpv8Vpv8Vpv9tx%2F%2F%2F%2F%2F%2F%2F%2F%2F+Z2P8Vpv8Vpv%2FF6f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2Fi9P+K0%2F9QvP9QvP9tx%2F%2FF6f%2F%2F%2F%2F%2F%2F%2F%2F+n3v8Vpv8Vpv8Vpv%2FF6f%2F%2F%2F%2F%2FT7v+Z2P%2Fi9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F+24%2F9QvP8Vpv8Vpv8Vpv8Vpv%2FF6f%2F%2F%2F%2F%2FF6f8Vpv8Vpv8krP9QvP9QvP9Bt%2F8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv%2FF6f%2F%2F%2F%2F%2FF6f8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv9Bt%2F9QvP9Bt%2F8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8Vpv8AAHBsAABhdAAAbiAAAHJ0AABsaQAAdGkAACBDAABlbgAAUEEAAEVYAAAuQwAAOy4AAEU7AABBVAAAQ00AAC5W</Image>
  <Url type="text/html"
    template="http://www.bing.com/search?q={searchTerms}&amp;form=OSDSRC"/>
  <Url type="application/x-suggestions+json"
    template="http://api.bing.com/osjson.aspx?query={searchTerms}&amp;language={language}&amp;form=OSDJAS"/>
  </OpenSearchDescription>


.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image3|

.. raw:: html

   </div>

Update: Right now this code only supports png and sometimes ico. i don't
know why it behave like this...

.. |image0| image:: http://3.bp.blogspot.com/_X5tq9y9xv2s/TMiAHb-LmaI/AAAAAAAAAjM/sfMeXSo95hY/s320/logo.png
   :target: http://3.bp.blogspot.com/_X5tq9y9xv2s/TMiAHb-LmaI/AAAAAAAAAjM/sfMeXSo95hY/s1600/logo.png
.. |image1| image:: http://4.bp.blogspot.com/_X5tq9y9xv2s/TMiSnHN2BZI/AAAAAAAAAjQ/2nhvag3eIO0/s320/Bing+search+provider.png
   :target: http://4.bp.blogspot.com/_X5tq9y9xv2s/TMiSnHN2BZI/AAAAAAAAAjQ/2nhvag3eIO0/s1600/Bing+search+provider.png
.. |Embedded Image| image:: data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAxklEQVR42mP4v0z0PyWYgToGbHf8/39PAIQmy4CXR/+DAYimmgFrVCCuIuAyVAPeXf7//8bM//+/PPqPFTzeBjEQpwEwADLgchfCBcdzUdXcW47HAJAkyPnYnAwyCAZALsVqAC7NMAyyAAR+fkAyAOQ3mNMJhTzIazAAN+BsNUIQLZBQMMh1sACGWoZIiaAYgDkNZCC6ZpDByGqgUcuAYjooYGAApAgUNiCMHK0gQ5DSBWZe2GgEcQEoXGAGgDAsWmmTmSjAADs5Dn62z9V4AAAAAElFTkSuQmCC
.. |image3| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/TOIpP67w5dI/AAAAAAAAAjU/QUdkLjf9X2Q/s1600/bing+favicon+for+seach+plugin.png
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/TOIpP67w5dI/AAAAAAAAAjU/QUdkLjf9X2Q/s1600/bing+favicon+for+seach+plugin.png
