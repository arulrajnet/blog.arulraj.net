Flash Player Debugger
#####################
:date: 2010-03-07 23:27
:author: arul
:category: Flash
:tags: Browser, Flash, Widget, windows
:slug: flash-player-debugger

**Flash Player Debugger**

|image0|\ How to get the flash player debugger version ...?

You can download the flashplayer debugger version from
here\ http://www.adobe.com/support/flashplayer/downloads.html .

The direct download link for windows is For
`IE <http://download.macromedia.com/pub/flashplayer/updaters/10/flashplayer_10_ax_debug.exe>`__
and for
`mozilla <http://download.macromedia.com/pub/flashplayer/updaters/10/flashplayer_10_plugin_debug.exe>`__.
Using the debugger version the trace output will be printed in
flashlog.txt .

The flashlog.txt path

For windows xp is "C:\\Documents and Settings\\<login
username>\\Application Data\\Macromedia\\Flash
Player\\Logs\\flashlog.txt "

For Windows Vista and windows 7 is : "C:\\Users\\<login
username>\\AppData\\Roaming\\Macromedia\\Flash
Player\\Logs\\flashlog.txt"

Debugging ..?

If the trace not shown on the log create mm.cfg file .

| Create a file for windows xp c:\\Documents and Settings\\mm.cfg
|  for vista C:\\Users\\<login username>\\mm.cfg with the following

| [text]
|  ErrorReportingEnable=0
|  TraceOutputFileEnable=1
|  MaxWarnings=0
|  [/text]

.. |image0| image:: http://1.bp.blogspot.com/_X5tq9y9xv2s/S5SG-gaYi8I/AAAAAAAAAMg/SXqWMtnCTEk/s400/adobeflashplayer.jpg
   :target: http://1.bp.blogspot.com/_X5tq9y9xv2s/S5SG-gaYi8I/AAAAAAAAAMg/SXqWMtnCTEk/s1600-h/adobeflashplayer.jpg
