---
title: How to add Return-path in php mail
date: 2009-07-13 23:19
author: arul
category: php
tags:
  - Linux
  - Programming
  - how
  - to
slug: how-to-add-return-path-in-php-mail
disqus_identifier: /2009/07/how-to-add-return-path-in-php-mail.html
status: published
---

[![image0](http://3.bp.blogspot.com/_Tq9uaJI0Xww/SlyTV7ulT3I/AAAAAAAAFFE/gSyRbeYFT1M/s320/php.png)](http://3.bp.blogspot.com/_Tq9uaJI0Xww/SlyTV7ulT3I/AAAAAAAAFFE/gSyRbeYFT1M/s1600-h/php.png)

Here is the code for add Return-path in php mail programmatically.

``` php
$today = date("F j\t\h Y, g:i a");
$name = 'Yourname';
$from = 'frommail@example.com';
$to = 'tomail@example.com';
$cc = 'ccmail@example.com';
$bcc = 'bccmail@example.com';
$subject = 'Example Subject';

// To send HTML mail
$headers = "MIME-Version: 1.0 \\r\\n";
$headers .= "Content-type: text/html; charset=ISO-8859-1;
format=flowed \\r\\n";
$headers .= "ontent-Transfer-Encoding: 8bit \\r\\n";
$headers .= "X-Mailer: PHP/" . phpversion(). "\\r\\n";
$headers .= "X-Priority: 1 (Highest) \\r\\n";
$headers .= "X-MSMail-Priority: High \\r\\n";
$headers .= "Importance: High \\r\\n";
// Additional headers
$headers .= "From: $name<$from> \\r\\n";

//This is one option to add the return path

$headers .= "Reply-To: $name<$from> \\r\\n";
$headers .= "Return-Path: $from \\r\\n";
$headers .= "Cc: $cc \\r\\n";

//See the 5th argument in mail function for Return-path

mail("toname<$to>",$subject,"This is the test message for How to add return path in the php mail function.",$headers,"-f $from");
```

OR

add sendmail-path in php.ini file

``` bash
sendmail_path = sendmail -t -i -F yourname@yourdomain.com -f  yourname@yourdomain.com
```

How to find php.ini file in Linux system

``` bash
root@localhost:~# find / -name php.ini
```
