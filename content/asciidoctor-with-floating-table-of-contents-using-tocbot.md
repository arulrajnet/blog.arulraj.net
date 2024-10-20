---
title: AsciiDoctor with Floating Table of contents Using Tocbot
date: 2024-09-14 21:42:00
author: arul
category: Documentation
tags: AsciiDoc
slug: asciidoctor-with-floating-table-of-contents-using-tocbot
disqus_identifier: asciidoctor-with-floating-table-of-contents-using-tocbot
cover: default.png
color: gray
headline: default headline
status: draft
---
I want to talk about different tools for documentation in this series of articles. Taking asciidoc / asciidoctor as the first tool to talks about.

The first-time I heard about asciidoc in the [Spring Docs](https://github.com/spring-io/spring-doc-resources/tree/master). Yes, I am a Java Guy.

## What is AsciiDoctor?


## How to install and Use?

### Linux

```bash
sudo apt-get update
sudo apt-get -y install --no-install-recommends asciidoctor
```

OR

Install RVM (Ruby version manager). Then using `gem install ascciidoctor`

```bash
curl -sSL https://rvm.io/mpapis.asc | gpg --import -
curl -sSL https://rvm.io/pkuczynski.asc | gpg --import -

curl -sSL https://get.rvm.io | bash -s stable
source ~/.rvm/scripts/rvm
rvm install 3.3.5
rvm use 3.3.5
gem install asciidoctor
```

Usually `rvm` installed in `/usr/local/rvm/bin/rvm`. If rvm command not found, then use this path.

RVM is [not supported for windows](https://github.com/rvm/rvm/issues/4645)

Interestingly, there are different version manager for different programing language

* NVM for NodeJS
* GVM for Golang
* Pyenv for Python
* Jenv for Java

Will discuss in a separate blog post and my dev setup.
### Windows

Download and install the ruby from [Ruby Installer](https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-3.3.5-1/rubyinstaller-3.3.5-1-x64.exe)

Then open the terminal or Git-Bash

```bash
gem install asciidoctor
```

## Adding Table of contents

Here is my adoc file. Pushed into this github repository.

To add table of contents to a page

```asciidoc
:toc: left

```


Refer the output [here](https://arulrajnet.github.io/asciidoctor-tocbot/toc-without-tocbot.html)
## Table of contents with TocBot


## Floating TOC

Its just a CSS trick.


## Who are all using AsciiDoc ?



## Pros and Cons



## Other tools

* Markdown Based
	* Mkdocs
	* Read the docs
	* Docusaurus
	* GitBook
* restructuredText Based
	* Sphinx
* Asciidoc based
	* antora
* Pandoc
*
