---
title: Bash completions for kubectl
date: 2016-01-23 12:26:32
tags: ubuntu,bash-completion
slug: bash-completions-for-kubectl
category: kubernetes
author: arul
lang: en
disqus_identifier: /2016/01/bash-completions-for-kubectl.html
status: published
---

To install bash completion for your kubectl

Get your kubectl client version

``` bash
kubectl version -c
```

Get the completion script for the corresponding to your kubectl version.

**Ubuntu**

``` bash
curl -sSL https://raw.githubusercontent.com/kubernetes/kubernetes/$(kubectl version -c | grep -o -P '(?<=GitCommit:").*(?=",)')/contrib/completions/bash/kubectl | sudo tee /etc/bash_completion.d/kubectl
```

**Mac**

``` bash
brew install bash-completion
curl -sSL https://raw.githubusercontent.com/kubernetes/kubernetes/$(kubectl version -c | grep -o -P '(?<=GitCommit:").*(?=",)')/contrib/completions/bash/kubectl > /usr/local/etc/bash_completion.d/kubectl
```

<figure class="align-center">
<img src="/assets/images/2016/1/kubectl-bash-completion.png"
alt="/assets/images/2016/1/kubectl-bash-completion.png" />
</figure>
