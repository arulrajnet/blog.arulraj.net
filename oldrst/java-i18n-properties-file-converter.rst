Java i18n properties file converter 
####################################
:date: 2010-07-30 15:00
:author: arul
:category: Programming
:tags: java
:slug: java-i18n-properties-file-converter
:disqus_identifier: /2010/07/java-i18n-properties-file-converter.html

**Properties File converter**

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image0|

.. raw:: html

   </div>

Google Translator can convert any word/sentence from one language to
other language. Now a days all web application have i18n support. The
developers just create a properties file for English in key value format
and then using google translator they create other language properties
for his/her testing purpose.  But in this method they need to go google
translator webpage and convert line by line to make the other language
properties file. But this process takes more time than writing a code :)
[really...!]. I too pass this situation, at that time i just search
google is there any Java api for google translator.

Then i found a opensource software for this, that is called `Google api
translate <http://code.google.com/p/google-api-translate-java/downloads/detail?name=google-api-translate-java-0.92.jar>`__
. Now come to the topic, here a java class for converting your English
properties file to Chinese .

Example code:

.. code-block:: java

  package com.sharedaa.translate;

  import java.io.BufferedReader;
  import java.io.File;
  import java.io.FileInputStream;
  import java.io.FileOutputStream;
  import java.io.InputStreamReader;
  import java.util.Iterator;
  import java.util.LinkedHashMap;
  import java.util.Set;
  import java.util.StringTokenizer;
  import com.google.api.translate.Language;
  import com.google.api.translate.Translate;

  public class TranslatorMain {
    static TranslatorMain main = null;
    static {
      main = new TranslatorMain();
    }

    /**
     * Singleton Constructor
     */
    private TranslatorMain() {

    }

    /**
     * To Get the singleton object
     * @return
     */
    public TranslatorMain getInstance() {
      return main;
    }

    /**
     * Main method
     * @param args
     * @throws Exception
     */
    public static void main(String[] args) throws Exception {
      //        System.setProperty("http.proxyHost", "3.246.36.25");
      //        System.setProperty("http.proxyPort", "80");
      //        System.setProperty("http.proxyUser", "admin");
      //        System.setProperty("http.proxyPassword", "admin");
      File inFile = new File("input.properties");
      File outFile = new File("output.properties");
      LinkedHashMap<String, String> inFileHash = null;
      LinkedHashMap<String, byte[]> outFileHash = null;
      FileOutputStream foutStream = null;
      try{
        Translate.setHttpReferrer("localhost");
        System.out.println("The proxy is connected..");
        inFileHash = main.getInputProperties(inFile);
        outFileHash = new LinkedHashMap<String, byte[]>();
        foutStream = new FileOutputStream(outFile);
        Set<String> infilekeySet = inFileHash.keySet();
        Iterator<String> infilekeyItr = infilekeySet.iterator();
        while (infilekeyItr.hasNext()) {
          String key = infilekeyItr.next();
          String value = inFileHash.get(key);
          System.out.println("Translating : " + value);
          byte[] transByte = Translate.execute(value, Language.ENGLISH,
          Language.CHINESE).getBytes("UTF8");
          outFileHash.put(key, transByte);
          foutStream.write(key.getBytes());
          foutStream.write("=".getBytes());
          foutStream.write(transByte);
          foutStream.write("\\n".getBytes());
        }
        System.out.println("End : Writing new Properties File....");
      } catch (Exception e) {
        e.printStackTrace();
      } finally {
        foutStream.close();
      }
  }

  /**
   * This for read a properties file and returns as a Hashmap
   * @param inputProperties
   * @return
   * @throws Exception
   */
  public LinkedHashMap<String, String> getInputProperties(File inputProperties) throws Exception {
    System.out.println("Start : Reading properties file..");
    LinkedHashMap<String, String> inputHash = null;
    FileInputStream finStream = null;
    BufferedReader bReader = null;
    try {
      inputHash = new LinkedHashMap<String, String>();
      finStream = new FileInputStream(inputProperties);
      bReader = new BufferedReader(new InputStreamReader(finStream));
      String line = bReader.readLine();
      String key = null;
      String value = null;
      while (line != null) {
        StringTokenizer token = new StringTokenizer(line, "=");
        if (token.countTokens() >= 2) {
          key = token.nextElement().toString();
          value = token.nextElement().toString();
          inputHash.put(key, value);
          //System.out.println("Key : " + key + " Value : " + value);
        }
        line = bReader.readLine();
      }
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      bReader.close();
      finStream.close();
    }
    System.out.println("End : Reading properties file..");
    return inputHash;
    }
  }


When you run this code most probably you got the below error. I Got this
error

.. code-block:: log

  java.lang.Exception: [google-api-translate-java] Error retrieving
    translation.
  at com.google.api.GoogleAPI.retrieveJSON(GoogleAPI.java:123)
  at com.google.api.translate.Translate.execute(Translate.java:69)
  at lang.main(lang.java:14)
  Caused by: java.net.UnknownHostException: ajax.googleapis.com
  at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:177)
  at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:366)
  at java.net.Socket.connect(Socket.java:519)
  at java.net.Socket.connect(Socket.java:469)
  at sun.net.NetworkClient.doConnect(NetworkClient.java:163)
  at sun.net.www.http.HttpClient.openServer(HttpClient.java:394)
  at sun.net.www.http.HttpClient.openServer(HttpClient.java:529)
  at sun.net.www.http.HttpClient.<init>(HttpClient.java:233)
  at sun.net.www.http.HttpClient.New(HttpClient.java:306)
  at sun.net.www.http.HttpClient.New(HttpClient.java:323)
  at
    sun.net.www.protocol.http.HttpURLConnection.getNewHttpClient(HttpURLConnection.java:837)
  at
    sun.net.www.protocol.http.HttpURLConnection.plainConnect(HttpURLConnection.java:778)
  at
    sun.net.www.protocol.http.HttpURLConnection.connect(HttpURLConnection.java:703)
  at
    sun.net.www.protocol.http.HttpURLConnection.getOutputStream(HttpURLConnection.java:881)
  at com.google.api.GoogleAPI.retrieveJSON(GoogleAPI.java:107)
  ... 2 more
  BUILD SUCCESSFUL (total time: 6 seconds)


This error for your firewall / your company proxy server blocks [my
company block some sites... :( ]
http://ajax.googleapis.com/ajax/services/language/translate . The api
could not reach the google translate server. At this time just use proxy
address to run [ ... :D ...]

.. code-block:: java

  System.setProperty("http.proxyHost", "10.20.1.20");
  System.setProperty("http.proxyPort", "80");
  System.setProperty("http.proxyUser", "admin");
  System.setProperty("http.proxyPassword", "admin");


Code Explanation :

-  The above class is a Singleton class. That is achieved by class
   initiated with in the static block and a private constructor
-  The getInputProperties() method reads input properties file and
   stored in a Hashmap in a key value format.  LinkedHashMap for getting
   the ordered output from the Map how you are inserted.
-  Then each key value is send to the Translate.execute() method in
   google api with the From and To Language String.
-  Then the results are written in another file. Thats all...

You can Expand this code what ever you want. If you want to download
this eclipse java Project `click here <http://sites.google.com/site/arulraj1985/list-of-files/Translator.zip?attredirects=0&d=1>`__.

The only thing is this is an online application. you need a net
connection for this.

.. |image0| image:: http://2.bp.blogspot.com/_X5tq9y9xv2s/TFMxF5Sh_sI/AAAAAAAAAe8/tiTfkCTchFI/s320/translate+to+properties+file.jpg
   :target: http://2.bp.blogspot.com/_X5tq9y9xv2s/TFMxF5Sh_sI/AAAAAAAAAe8/tiTfkCTchFI/s1600/translate+to+properties+file.jpg
