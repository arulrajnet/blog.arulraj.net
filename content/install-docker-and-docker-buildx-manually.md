---
title: Install Docker, Compose and Buildx Manually
date: 2024-08-19 07:06:00
author: arul
category: Docker
tags: Tips-and-Tricks
slug: install-docker-compose-and-buildx-manually
status: published
headline: Install docker, docker buildx and docker compose manually. This steps can be used to setup docker with in docker.
cover: assets/images/install-docker-manually-cover.png
---
In this article, Install the docker binary manually. The setup `compose` and `buildx`. So that `docker buildx` or `docker compose` (There is a space after docker) command will work as like any other installation.

These can be used install `docker with in docker.`
## Docker

```bash
DOCKER_VERSION=27.2.0
curl -SLO "https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz"
tar -xzvf "docker-${DOCKER_VERSION}.tgz" -C /tmp
cp /tmp/docker/docker /usr/local/bin/
rm -rf /tmp/docker
rm -rf "docker-${DOCKER_VERSION}.tgz"
```

The compose and buildx comes under the docker cli plugins.
### Docker Buildx

```bash
DOCKER_BUILDX_VERSION=0.16.2
curl -SLO "https://github.com/docker/buildx/releases/download/v${DOCKER_BUILDX_VERSION}/buildx-v${DOCKER_BUILDX_VERSION}.linux-amd64"
mkdir -p ${HOME}/.docker/cli-plugins
cp "buildx-v${DOCKER_BUILDX_VERSION}.linux-amd64" ${HOME}/.docker/cli-plugins/docker-buildx
rm "buildx-v${DOCKER_BUILDX_VERSION}.linux-amd64"
```
### Docker Compose

```bash
DOCKER_COMPOSE_VERSION=v2.29.2
curl -SLO "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-linux-x86_64"
mkdir -p ${HOME}/.docker/cli-plugins
cp "docker-compose-linux-x86_64" ${HOME}/.docker/cli-plugins/
rm "docker-compose-linux-x86_64"
```


Read more [here](https://docs.docker.com/compose/install/linux/)
## Usual way of install Docker and Compose

Docker

```bash
curl -sSL https://get.docker.com/ | sh
sudo usermod -aG docker ${USER}
```

Docker compose

```bash
DOCKER_COMPOSE_VERSION=v2.29.2
sudo curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
cat << "EOF" >> ~/.bashrc
alias fig="docker-compose"
EOF
```

### Why fig alias?

The docker-compose project was originally named `fig` as an open-source initiative. After Docker acquired it, the project was renamed to `docker-compose`.

Just a history.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I wanted to call it &quot;Plum&quot; but thankfully <a href="https://twitter.com/AanandPrasad?ref_src=twsrc%5Etfw">@AanandPrasad</a> had better taste in names. <a href="https://t.co/V45MyfvYyG">https://t.co/V45MyfvYyG</a></p>&mdash; Ben Firshman (@bfirsh) <a href="https://twitter.com/bfirsh/status/1737641556386132396?ref_src=twsrc%5Etfw">December 21, 2023</a></blockquote><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


Refer this [commit](https://github.com/docker/compose/commit/8998bd1adc3def9e6e55b654b16415a46e1ca28b)
