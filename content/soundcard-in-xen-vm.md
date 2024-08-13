---
title: Soundcard in xen vm
date: 2010-03-25 11:08
author: arul
category: Virtualization
tags: cloud-computing,xen,Linux
slug: soundcard-in-xen-vm
disqus_identifier: /2010/03/soundcard-in-xen-vm.html
status: published
---

**Enable sound card in xen vm**

[![image0](http://2.bp.blogspot.com/_X5tq9y9xv2s/S6t1j7HhaTI/AAAAAAAAANI/Tc7vempGBMo/s400/soundcard.jpg)](http://2.bp.blogspot.com/_X5tq9y9xv2s/S6t1j7HhaTI/AAAAAAAAANI/Tc7vempGBMo/s1600/soundcard.jpg)

How to enable sound card in the xen based vm..?

The vmware vm have the functionalists for adding sound card to their
vm\'s. Then what about xen vm

[![image1](http://3.bp.blogspot.com/_X5tq9y9xv2s/S6t7MxH-nPI/AAAAAAAAANQ/5-HRevzq_tE/s400/vmware+sound+card.jpg)](http://3.bp.blogspot.com/_X5tq9y9xv2s/S6t7MxH-nPI/AAAAAAAAANQ/5-HRevzq_tE/s1600/vmware+sound+card.jpg)

By adding the below line to your HVM (Hardware Virtual Machine) file,
You can add the sound card for the virtual machine.

``` text
audio=1
soundhw='sb16,es1370'
```

If you play a sound file it you can hear the sound from VMM sound out.
Then your hvm file is look like

``` text
name="sound-card"
builder = "hvm"
memory = "1024"
vif = [ 'type=ioemu, mac=00:16:3e:a0:0:8, bridge=xenbr0' ]
device_model = "/usr/lib/xen/bin/qemu-dm-sync"
kernel = "/usr/lib/xen/boot/hvmloader"
vnc=1
vncunused=0
vnclisten="0.0.0.0"
apic=1
acpi=0
pae=1
vcpus=2
boot='c'
audio=1
soundhw='sb16,es1370'
usb=1
usbdevice='tablet'
disk = ['file:/vm/sound-card/disk,ioemu:hda,w','phy:/dev/zero,hdd:cdrom,r']
```

Now Goto the controlpanel now the sound devices is enabled\...

[![image2](http://2.bp.blogspot.com/_X5tq9y9xv2s/S6uXmdFTDbI/AAAAAAAAANY/t5aud9XDQt0/s400/xen%2Bsound%2Bcard.jpg)](http://2.bp.blogspot.com/_X5tq9y9xv2s/S6uXmdFTDbI/AAAAAAAAANY/t5aud9XDQt0/s1600/xen%2Bsound%2Bcard.jpg)
