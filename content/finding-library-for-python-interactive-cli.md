---
title: Finding Library for Python Interactive CLI/Shell
date: 2024-09-12 07:16
author: arul
category: Python
tags: CLI
slug: finding-library-for-python-interactive-clishell
disqus_identifier: finding-library-for-python-interactive-clishell
cover: 
color: gray
headline: Journey to find the interactive CLI library in python.
status: published
---
My requirement is to Ask question to user and the user select the answer from choices. I want the cli should be in python because the libraries the cli interact with is already developed python. 

First I have found below from [Reddit](https://www.reddit.com/r/learnpython/comments/spphji/recommended_library_for_an_interactive_cli/)

[PyInquirer](https://github.com/CITGuru/PyInquirer)

Its fits my requirement. But it seems not maintained. So searching for other [alternatives](https://www.google.com/search?q=pyinquirer+alternatives).

Found the below awesome list

[Awesome CLI Frameworks in python](https://github.com/shadawck/awesome-cli-frameworks?tab=readme-ov-file#python)

Then short listed these 

[Python Prompt Toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)
[PyInquirer](https://github.com/CITGuru/PyInquirer)
[InquirerPy](https://github.com/kazhala/InquirerPy)
[Questionary](https://github.com/tmbo/questionary)

My intuition says, I am mostly go with `Questionary` . Lets see. Will update the post after completed. 

Got to know about

* Text User Interface - TUI
* Seems python prompt toolkit is most [widely used](https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/PROJECTS.rst) and actively maintained. 
* [Inquirer.js](https://github.com/SBoudrias/Inquirer.js/) for NodeJS
* [Cobra](https://github.com/spf13/cobra) for Golang

Created Git [CLI](https://github.com/stars/arulrajnet/lists/cli) list. 