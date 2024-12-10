---
title: Pi-Hole as Internet Parental Control
date: 2024-12-09 07:54:00
author: arul
category: Network
tags: network,DIY
slug: pi-hole-as-internet-parental-control
disqus_identifier: pi-hole-as-internet-parental-control
cover: /assets/images/pi-hole-cover-image-parental-control-with-pihole-dns-server.png
color: gray
headline: How to use pi-hole and do minimal parental control. In this post we block the internet for the TV.
status: published
---
This post explains how I am using Pi-hole to block the internet for my TV 📺. I am using Pi-hole as parental control 👨‍👩‍👧‍👦.

Some time back I set up [pi-hole](https://github.com/pi-hole/pi-hole) on a Raspberry Pi in my home network to block advertisements.

<blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">~30% of my home internet traffic are tracking or advertisement. Now its all are blocked with <a href="https://twitter.com/hashtag/pihole?src=hash&amp;ref_src=twsrc%5Etfw">#pihole</a> <a href="https://t.co/mRai9IBwgb">pic.twitter.com/mRai9IBwgb</a></p>&mdash; arulraj.net (@arulrajnet) <a href="https://twitter.com/arulrajnet/status/1272530082129522688?ref_src=twsrc%5Etfw">June 15, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Now, I have reused it to block the internet for a specific device or domain.

## My network

* The pi-Hole act as a DNS and DHCP server
* Main Router is just a WAN provider
	* Route 8.8.8.8, 4.4.4.4 and 8.8.4.4 traffic to 192.168.1.53
	* Youtube app or Android SmartTV doesn't honor the DNS received via DHCP Offer.
	* Thats why route all the DNS traffic to pi-hole
* Extender is to widen the coverage


![[my-home-network-pihole.drawio.png]]
## Use case

At our home, TV time for the kids is mostly reserved for weekends. But once they start watching, getting them to stop can feel like a never-ending struggle. Forget asking for the remote; that’s practically impossible!

I needed a foolproof way to ensure the TV goes off after a set time without any arguments.

The Pi-hole came for rescue.
## Hack

A little bit background on Pi-Hole.

* Its a DNS server with the [advertisement domains](https://github.com/StevenBlack/hosts) list.
* Whenever a device try to resolve those domains, it returns as `0.0.0.0`
* Its also acts as DHCP server

![[output/assets/images/nslookup-output-of-tracking-domain-with-pi-hole.png]]

We are going to use the following resources to block internet.

* Groups - Its for grouping clients
* Clients - Every MAC address in the network as client and assign the client to a Group
* Domains - Custom whitelist or blocklist the domains and assign to a Group.

These are the steps we are going to do

* Create a group.
* Create domain. Add the domain to block and add that domain to group.
* Create client and assign that client to group.

Create a Group. This will used to add the blocklist client.

![[output/assets/images/pi-hole-create-group.png]]
Here I have created group called `Block_Internet`
## To block all internet for the particular device

Add a new block list domain.

Domains → Regex Filter

Regular Expression: `.*`
Comment: `Block All`
Click Add to Blacklist

![[output/assets/images/pi-hole-regex-filter-for-block-all.png]]

Once added, change the group to `Block_Internet`

![[output/assets/images/pi-hole-add-the-black-list-to-group.png]]

Now add the client to the group.

In my case whenever the TV time got over, I will add the `TV` client into the list.

![[output/assets/images/pi-hole-add-client-to-block-group.png]]

## To block youtube

Add `*.googlevideo.com` domain to the regex filter.
## Things to Improve on Pi-Hole

* Time based restriction or group assignment
* domain list support for this kind of use cases

## Final Thoughts

All this blocking works perfectly—until the day they discover VPNs. For now, they’re too young to figure it out. To them, it’s just “Dad’s magic.” 😆
