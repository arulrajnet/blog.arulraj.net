---
title: Setup docker and tools
date: 2016-01-24 06:34:22
tags: ubuntu,bash-completion
slug: setup-docker-and-tools
category: Docker
author: arul
lang: en
disqus_identifier: /2016/01/setup-docker-and-tools.html
status: published
---

Guide to install and configure docker and related tools.

## Install Docker

Installing docker on any bash systems.

``` bash
curl -sSL https://get.docker.com/ | sh
sudo usermod -aG docker ${USER}
```

## Docker Tools

**Docker compose**

To install docker-compose

``` bash
VERSION="v2.24.6"
sudo curl -L https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

To install bash completions for docker-compose

``` bash
curl -ksSL https://raw.githubusercontent.com/docker/compose/$(docker-compose --version | awk 'NR==1{print $NF}')/contrib/completion/bash/docker-compose |sudo tee /etc/bash_completion.d/docker-compose
```

**Docker alias**

Add this in your `.bashrc` file.

``` bash
# ------------------------------------
# Docker alias and function
# ------------------------------------

# Get latest container ID
alias dl="docker ps -l -q"

# Get container process
alias dps="docker ps"

# Get process included stop container
alias dpa="docker ps -a"

# Get images
alias di="docker images"

# Get container IP
alias dip="docker inspect --format '{{ .NetworkSettings.IPAddress }}'"

# Run deamonized container, e.g., $dkd base /bin/echo hello
alias dkd="docker run -d -P"

# Run interactive container, e.g., $dki base /bin/bash
alias dki="docker run -i -t -P"

# Execute interactive container, e.g., $dex base /bin/bash
alias dex="docker exec -i -t"

# Stop all containers
dstop() { docker stop $(docker ps -a -q); }

# Remove all containers
drm() { docker rm $(docker ps -a -q); }

# Stop and Remove all containers
alias drmf='docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)'

# Remove all images
dri() { docker rmi $(docker images -q); }

# Dockerfile build, e.g., $dbu tcnksm/test
dbu() { docker build -t=$1 .; }

# Show all alias related docker
dalias() { alias | grep 'docker' | sed "s/^\([^=]*\)=\(.*\)/\1 => \2/"| sed "s/['|\']//g" | sort; }
```

Refer from <https://github.com/tcnksm/docker-alias/>
