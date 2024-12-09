---
title: Docker Desktop Hacks
date: 2024-10-24 19:18:06
author: arul
category: others
tags: others
slug: docker-desktop-hacks
disqus_identifier: docker-desktop-hacks
cover: /assets/images/default.png
color: gray
headline: Docker Desktop Hacks
status: draft
---


To open your docker-compose.yml inside the docker desktop

https://open.docker.com/dashboard/dev-envs?url=https://github.com/docker/awesome-compose/tree/master/nginx-golang


```
Installing credential helpers... 
done
Cloning into '/com.docker.devenvironments.code'...
Detecting main repo language...
Migration: no config.json detected
Migration: no .docker/docker-compose.yaml detected
Unsupported language "Rust" - using default base image
2024/10/24 19:26:20 INFO: [core] [Channel #1] Channel created
2024/10/24 19:26:20 INFO: [core] [Channel #1] original dial target is: "npipe:////./pipe/buildkitd"
2024/10/24 19:26:20 INFO: [core] [Channel #1] parsed dial target is: {URL:{Scheme:npipe Opaque: User: Host: Path://./pipe/buildkitd RawPath: OmitHost:false ForceQuery:false RawQuery: Fragment: RawFragment:}}
2024/10/24 19:26:20 INFO: [core] [Channel #1] fallback to scheme "passthrough"
2024/10/24 19:26:20 INFO: [core] [Channel #1] parsed dial target is: {URL:{Scheme:passthrough Opaque: User: Host: Path:/npipe:////./pipe/buildkitd RawPath: OmitHost:false ForceQuery:false RawQuery: Fragment: RawFragment:}}
2024/10/24 19:26:20 INFO: [core] [Channel #1] Channel authority set to "npipe:%2F%2F%2F%2F.%2Fpipe%2Fbuildkitd"
2024/10/24 19:26:20 INFO: [core] [Channel #1] Resolver state updated: {
```


what is `config.json` and `.docker/docker-compose.yaml`



Docker CLI 

docker desktop 4.34.3

