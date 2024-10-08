---
title: Apisix Without etcd in Docker Compose
date: 2024-10-05 07:14
author: arul
category: APISix
tags: proxy,etcd,APISix
slug: apisix-without-etcd-and-ssl-in-compose
disqus_identifier: apisix-without-etcd-and-ssl-in-compose
cover: assets/images/apisix-without-etcd-cover.png
color: gray
headline: Docker compose example for running APISix without ETCD as standalone mode.
status: published
---
This  blog post for running apisix without ETCD.
## Why❓

By default, apisix depends on etcd for storing configuration.

But most of the time your upstream services are fixed. Not changed often. Then do we really need etcd for configuration. Maintain and managing etcd cluster is pain and money 💲

Here is the [standalone mode](https://apisix.apache.org/docs/apisix/deployment-modes/#standalone){:target="_blank"} to solve this.

## 🤔How ?

If you are geek, here is the [Github repo](https://github.com/arulrajnet/apisix_without_etcd) for docker-compose example with full source code. Go there.

### config.yaml

This file has the configuration as you do earlier

```yaml
deployment:
  role: data_plane
  role_data_plane:
    config_provider: yaml

#END
```

Here the `config_provider` as yaml.

This has to be mounted as `/usr/local/apisix/conf/config.yaml`
### apisix.yaml

This file is responsible for routes, services and upstreams.  The file will be look like

```yaml
routes:
  -
    uri: /*
    service_id: 1
services:
  -
    id: 1
    upstream_id: 1
upstreams:
  -
	id: 1
    nodes:
      "web1:80": 1
    type: roundrobin

#END
```

This has to be mounted as `/usr/local/apisix/conf/apisix.yaml`

### docker-compose.yml

```yaml
services:
  apisix:
    image: apache/apisix:3.10.0-debian
    environment:
      APISIX_STAND_ALONE: "true"
    volumes:
      - ${PWD}/apisix.yaml:/usr/local/apisix/conf/apisix.yaml
      - ${PWD}/config.yaml:/usr/local/apisix/conf/config.yaml
    ports:
      # Web - Proxy
      - 9080
```


The common areas where manual errors occur

* The mounting path of the files.
* The content of the files. The different content for different files.
* The `#END` line at the end of file.
* The environmental variable for apisix `APISIX_STAND_ALONE: "true"`
## What is on the Repo?

There are two upstreams behind the APISix.

The URI `/` and `/web1` forwards to the web1.

The URI `/web2` forwards to the web2.

These routes, services and upstreams configured in [apisix.yaml](https://github.com/arulrajnet/apisix_without_etcd/blob/main/apisix.yaml)

![[apisix-without-etcd.drawio.png]]
