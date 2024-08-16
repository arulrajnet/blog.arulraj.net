---
title: Upgrade postgres client 9.3 to 9.4 in ubuntu 14.04
date:   2015-05-14 22:40:30
tags:   postgresql, database
slug:   upgrade-postgres-client-9-3-to-9-4-in-ubuntu-14-04
category:   Database
author: arul
lang:   en
status:   draft
disqus_identifier:    database-upgrade-samsung-galaxy-5-to-ice-cream-sandwich
---

sudo apt-get remove postgresql-client-9.3 sudo apt-get install
postgresql-client-9.4 sudo sh -c \'echo \"deb
<http://apt.postgresql.org/pub/repos/apt/> \$(lsb_release -cs)-pgdg
main\" \> /etc/apt/sources.list.d/pgdg.list\' sudo apt-get install wget
ca-certificates wget \--quiet -O -
<https://www.postgresql.org/media/keys/ACCC4CF8.asc> \| sudo apt-key add
-sudo apt-get update sudo apt-get upgrade sudo apt-get install
postgresql-client-9.4

sudo apt-get upgrade pgadmin3

psgl \--version

<http://wiki.postgresql.org/wiki/Apt>
