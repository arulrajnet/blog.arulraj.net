How to add Red5 service
#######################
:date: 2010-07-27 13:20
:author: arul
:category: Red5
:tags: commands, Linux, red5, scripting, how to
:slug: how-to-add-red5-service

**How to add Red5 service**

|image0|

In this article you are going to add red5 service in your Linux box.

Please use the Below script.

[bash]

| #!/bin/bash
|  # Author www.arulraj.net
|  # red5    This is used to start, stop, restart and status of red5
|  #

export RED5\_HOME=/opt/red5

| PID=0
|  RTMPPORT=1935
|  prog="red5"

| start(){
|  status
|  if [ $PID -eq 0 ] ; then
|  echo $"Starting $prog..."
|  nohup $RED5\_HOME/red5.sh 1> $RED5\_HOME/log/stdout.log 2>
  $RED5\_HOME/log/stderr.log < /dev/null &
|  PID=$!
|  echo $"$prog started at port $RTMPPORT and PID[$PID]."
|  else
|  echo
|  fi
|  return $PID
|  }

| stop(){
|  status
|  if [ $PID -eq 0 ] ; then
|  echo
|  else
|  echo $"Stopping $prog..."
|  $RED5\_HOME/red5-shutdown.sh
|  echo $"PID[$PID] is killed."
|  fi
|  return $PID
|  }

| restart(){
|  stop
|  sleep 2
|  start
|  }

| status() {
|  RTMPPORT=\`cat $RED5\_HOME/conf/red5.properties \| grep -w
  "rtmp.port" \| awk -F= '{print $2}'\`
|  #PID=\`lsof -i \| grep java \| grep \*:$RTMPPORT \| awk '{print
  $2}'\`
|  PID=\`ps -ef \| grep red5 \| grep java \| awk '{print $2}'\`
|  if [ x"$PID" == "x" ] ; then
|  PID=0
|  echo $"$prog is not running."
|  else
|  echo $"$prog running on port $RTMPPORT and PID[$PID]."
|  fi
|  return $PID
|  }

| # How its called.
|  case "$1" in
|  start)
|  start
|  ;;
|  stop)
|  stop
|  ;;
|  status)
|  status
|  ;;
|  restart)
|  restart
|  ;;
|  \*)
|  echo $"Usage: $0 {start\|stop\|status\|restart}"
|  PID=1
|  esac

exit $PID

[/bash]

Steps:

-  Save these shell script lines as a file. For mine i saved as file
   "red5". OR You can download this file from
   `Here <http://arulraj.net/labs/script/red5>`__
-  Copy this file to /etc/init.d/
-  Then execute the below commands to start red5 when your system starts

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image1|

.. raw:: html

   </div>

I checked with ubuntu 10.04. For chkconfig work on ubuntu you need to
install chkconfig

| This above script Not working in Ubuntu
|  [bash]apt-get install chkconfig[/bash]

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image2|

.. raw:: html

   </div>

| Add red5 in startup - ubuntu:
|  Use this command
|  [bash]
|  sudo update-rc.d red5 defaults
|  [/bash]
|  Thanks to anonymous for this info.

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Usage:

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Start : /etc/init.d/red5 start

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Stop : /etc/init.d/red5 stop

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Status : /etc/init.d/red5 status

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Restart : /etc/init.d/red5 restart

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Please Let me know if you have any issues or better ideas...

.. raw:: html

   </div>

.. |image0| image:: http://red5.googlecode.com/svn/doc/trunk/FinalLogo.png
.. |image1| image:: http://3.bp.blogspot.com/_X5tq9y9xv2s/TFB9KfBDYDI/AAAAAAAAAd0/V698BY0k9jA/s640/red5+chkconfig+not+working.png
   :target: http://3.bp.blogspot.com/_X5tq9y9xv2s/TFB9KfBDYDI/AAAAAAAAAd0/V698BY0k9jA/s1600/red5+chkconfig+not+working.png
.. |image2| image:: http://3.bp.blogspot.com/_X5tq9y9xv2s/TE8s5WDkvGI/AAAAAAAAAds/kPzFBTdJOeo/s320/Red5+service+script.png
   :target: http://3.bp.blogspot.com/_X5tq9y9xv2s/TE8s5WDkvGI/AAAAAAAAAds/kPzFBTdJOeo/s1600/Red5+service+script.png
