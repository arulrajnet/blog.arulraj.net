---
title: Golang Version Manager(GVM) for Windows Git Bash
date: 2024-10-20 09:13:50
author: arul
category: Development
tags: Golang,Dev-Setup,Git-Bash,windows
slug: golang-version-manager-gvm-for-windows-git-bash
disqus_identifier: golang-version-manager-gvm-for-windows-git-bash
color: gray
headline: Golang Version Manager(GVM) for Windows Git Bash
status: published
cover: /assets/images/default.png
---
I use windows for my work and I frequently switch between Golang 18 and the latest version. Also I use Git Bash as terminal in my windows. Here is the steps to setup GVM in that. There is a slight difference between the official documentation. Thats why this post. 

## What official documentation says?

Most of you used this [gvm](https://github.com/moovweb/gvm) . But this is doesn't support for windows. So I have found this [andrewkroh/gvm: Go Version Manager](https://github.com/andrewkroh/gvm) . Its supports windows as well. 

If you are using powershell go with their documentation

```bash
[Net.ServicePointManager]::SecurityProtocol = "tls12"
Invoke-WebRequest -URI https://github.com/andrewkroh/gvm/releases/download/v0.5.2/gvm-windows-amd64.exe -Outfile C:\Windows\System32\gvm.exe
gvm --format=powershell 1.23.2 | Invoke-Expression
go version
```

But there is no documentation for Git bash. 

## How to do in Git Bash

### Install

Open Git Bash.

This is for install gvm and install golang 1.18

```bash
mkdir -p ~/bin
curl -sL -o ~/bin/gvm https://github.com/andrewkroh/gvm/releases/download/v0.5.2/gvm-windows-amd64.exe
chmod +x ~/bin/gvm
gvm install 1.18
```

### Setup default Golang

The following will auto add it in your `.bashrc` file. This will setup golang 1.18 as default.

```bash
cat << "EOF" >> ~/.bashrc
#
# GVM (Go Version Manager) https://github.com/andrewkroh/gvm
#
if which gvm > /dev/null; then
  if gvm list | grep -q "1.18"; then
    eval "$(gvm --format=bash 1.18)"
  fi
fi
EOF
```

### To change Golang

To change the golang to `1.23` from `1.18` on runtime

Install 1.23 if not already installed

```bash
gvm install 1.23
```

To change

```bash
eval $(gvm use --format=bash 1.23)
```