:title: Ubuntu Hidden Features You Need
:slug: ubuntu-hidden-features-you-need
:date: 2015-07-30 07:43:27
:tags: 
:category: 
:author: arul
:lang: en
:status: draft
:summary: 

you may refer this is as things to do after ubuntu installation. 

After first install to make it more usuable follow the things. 

### Privacy

sudo apt-get remove unity-lens-shopping

127.0.0.1   productsearch.ubuntu.com

add this in /etc/hosts

All Settings --> Privacy --> Search then OFF Include online search results


### Networing

Bluetooth enable receive files

Personal File Sharing --> Receive Files over Bluetooth --> Check Two check boxes. 

change bluetooth SSID name

it always show ubuntu-0 to change that. in bluetooth control panel there is no option.

sudo hciconfig hci0 name 'Device Name' - this is temp change

http://askubuntu.com/questions/80960/how-to-change-bluetooth-device-name

touch /etc/machine-info

echo "PRETTY_HOSTNAME=device-name" | sudo tee -a /etc/machine-info

sudo service bluetooth restart

### add swap memory
