---
title: Dos2Unix / Unix2Dos in ubuntu
date:   2011-08-09 11:56
author: arul
category:   Linux
tags:   commands, ubuntu, how-to
slug:   dos2unix-unix2dos-in-ubuntu
status:   published
disqus_identifier:    /2011/08/dos2unix-unix2dos-in-ubuntu.html
---

By default ubuntu does not have dos2unix and unix2dos commands. But they
provide some alternative commands. Those are fromdos and todos.
sometimes its hard to switch to new commands. You can solve this issue
by creating soft / symbolic links. Here its how to do.

[![image0](http://2.bp.blogspot.com/-jElTSUvs3NU/TkFvZUAJY6I/AAAAAAAAArE/dPCEYt8KI04/s400/dos2unix.png)](http://2.bp.blogspot.com/-jElTSUvs3NU/TkFvZUAJY6I/AAAAAAAAArE/dPCEYt8KI04/s400/dos2unix.png)
command creation

First you have to find the location for \"fromdos\". Below command will
return the location

``` bash
which fromdos
```

Then you have to create a soft/symbolic link for that location with the
name \"dos2unix\"

``` bash
sudo ln -s /usr/bin/fromdos /usr/bin/dos2unix
```

Follow the same steps for unix2dos.

To know more about symbolic/soft and hard links [click
here](http://stackoverflow.com/questions/185899/what-is-the-difference-between-a-symbolic-link-and-a-hard-link)
