---
title: How to Add FreeSwitch Service
date: 2009-06-09 05:41:00
author: arul
category: Linux
tags: Linux,VOIP,Flash,how-to
slug: how-to-add-freeswitch-service
disqus_identifier: /2009/06/how-to-add-freeswitch-service.html
status: published
---

Hello all,

Here how to start
[freeswitch](http://wiki.freeswitch.org/wiki/Installation_Guide)when
machine boots.

``` bash
#!/bin/bash
#
# freeswitch This starts and stops the freeswitch
#
# chkconfig: 345 60 50
# chkconfig: - 60 50
# description: freeswitch.sh - startup script for freeswitch on FreeBSD
# processname: /usr/local/freeswitch/bin/freeswitch
# pidfile: /usr/local/freeswitch/log/freeswitch.pid

PATH=/sbin:/bin:/usr/bin:/usr/sbin

# Source function library.
. /etc/init.d/functions

# Get config.
test -f /etc/sysconfig/network && . /etc/sysconfig/network

# Check that we are root ... so non-root users stop here
[ `id -u` = 0 ] || exit 1

# Check that networking is up.
[ "${NETWORKING}" = "yes" ] \|\| exit 0

RETVAL=0
prog="Freeswitch"

start() {
if [ -x /usr/local/freeswitch/bin/freeswitch ] ; then
  echo -n $"Starting $prog: "
  /usr/local/freeswitch/bin/freeswitch -nc &
  RETVAL=$?
  sleep 1
fi
return $RETVAL
}

stop() {
  if [ -x /usr/local/freeswitch/bin/freeswitch ] ; then
    echo -n $"Stopping $prog: "
    /usr/local/freeswitch/bin/freeswitch -stop &
    RETVAL=$?
    sleep 1
  fi
  return $RETVAL
}

restart(){
  stop
  sleep 5
  start
}

# See how we were called.
case "$1" in

start)
  start
;;

stop)
  stop
;;

restart)
  restart
;;

*)
  echo "usage: $0 { start \| stop \| restart }"
  RETVAL=1

esac
exit $RETVAL
```

save these lines as file name freeswitch and copied to /etc/init.d/
folder

then run the below comments

``` bash
chkconfig -add /etc/init.d/freeswitch
chkconfig freeswitch on
```

you are done. Now Freeswitch will start when your PC Boots.

Freeswitch commands:

``` bash
Start : /etc/init.d/freeswitch start
Stop : /etc/init.d/freeswitch stop
Restart : /etc/init.d/freeswitch restart
```
