:title: Docker aufs failed in ubuntu 14.04.02
:slug: docker-aufs-failed-in-ubuntu-14-04-02
:date: 2015-07-08 11:04:32
:tags: Ubuntu, Docker
:category: Linux
:author: Arul
:status: draft
:lang: en
:summary: 


Ubuntu 14.04.02 upgrade to new kernal version 3.18.0-031800-generic

This not combatible with docker. I am getting

ERRO[0000] [graphdriver] prior storage driver "aufs" failed: invalid argument
FATA[0000] Error starting daemon: error initializing graphdriver: invalid argument
/var/run/docker.sock is up



So you have to revert back to 3.16.0-41-generic

update that in /boot/grup/grup.cfg

