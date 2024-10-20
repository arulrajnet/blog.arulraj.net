---
title: WinGet Uninstall Multiple Package With Same Name
date: 2024-08-17 06:27:00
author: arul
category: Windows
tags: Tips-and-Tricks,Git-Bash
slug: winget-uninstall-multiple-package-with-same-name
status: published
disqus_identifier: winget-uninstall-multiple-package-with-same-name
cover: /assets/images/winget-unistall-success.png
headline: Explain about how to uninstall multiple package with same name using winget. Solving the error on uninstall with specific version and Id.
---
We want to remove a package from windows using `winget`.

Before uninstalling, list the package with the name.

![[winget-list-package.png]]

There is two packages with the same name "WhatsApp Web". But the Id and Version are different.

Use `winget list` to get all the installed packages.
## Error on uninstall with specific version

Tried this

```bash
winget uninstall --name "WhatsApp Web" --version "1.0.0.0"
```

Got the following error

```
Multiple installed packages found matching input criteria. Please refine the input.
```

![[winget-uninstall-with-version.png]]
## Error on uninstall with Id

Tried this

```bash
winget uninstall --name "WhatsApp Web" --id MSIX\web.whatsapp.com-6EC4871F_1.0.0.0_neutral__910631y4v73xw
```

Got the following error

```
No installed package found matching input criteria.
```

![[winget-uninstall-with-id.png]]
## The Fix

We have to escape the backslash (\)

```bash
winget uninstall --name "WhatsApp Web" --id MSIX\\web.whatsapp.com-6EC4871F_1.0.0.0_neutral__910631y4v73xw
```

Now its uninstalled successfully.

![[winget-unistall-success.png]]
