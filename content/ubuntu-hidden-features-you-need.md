---
title: Ubuntu Hidden Features You Need
date:   2015-12-23 14:31:16
tags:   linux, tips, ubuntu
slug:   ubuntu-hidden-features-you-need
category:   ubuntu
author: arul
lang:   en
status:   draft
disqus_identifier:    ubuntu-ubuntu-hidden-features-you-need
---

you may refer this is as things to do after ubuntu installation.

After first install to make it more usuable follow the things.

Things you should do after install ubuntu.

###Privacy

When ever you search for the file or application. The results also added
from amazon, wiki etc., There are different options to remove that
feature

``` bash
echo "127.0.0.1   productsearch.ubuntu.com" | sudo tee -a /etc/hosts
```

OR

All Settings \--\> Privacy \--\> Search then OFF Include online search
results

I Prefered to use this.

OR

``` bash
sudo apt-get remove unity-lens-shopping
```

###Networing

**Bluetooth enable receive files**

Personal File Sharing \--\> Receive Files over Bluetooth \--\> Check Two
check boxes.

**change bluetooth SSID name**

it always show ubuntu-0 to change that. In bluetooth control panel there
is no option.

``` bash
sudo hciconfig hci0 name 'device-name' - this is temp change
```

<http://askubuntu.com/questions/80960/how-to-change-bluetooth-device-name>

replace \"device-name\" with yours.

``` bash
echo "PRETTY_HOSTNAME=device-name" | sudo tee -a /etc/machine-info
sudo service bluetooth restart
```

Image of bluetooth settings.

###Check for additional drivers

###Install flash player with chrome

``` bash
sudo apt-get update
sudo apt-get install chromium-browser pepperflashplugin-nonfree
sudo update-pepperflashplugin-nonfree --install
```

###Add swap memory

I faced chrome always hanging. After adding swap space I m not face that
issue.
