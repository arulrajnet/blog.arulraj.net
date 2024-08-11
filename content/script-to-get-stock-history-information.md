---
title: Script to get Stock History Information
slug:   script-to-get-stock-history-information
date:   2015-09-06 23:06:45
tags:   share market, linux, python, shellscript
category:   Linux
author: arul
lang:   en
disqus_identifier:    /2015/09/script-to-get-stock-history-information.html
---

I wrote a python script to get stock market current and history
information based on Google finance API. Here I am going to explain
about that.

## How to setup

-   Download
    [GetStockInfo.py](https://gist.github.com/arulrajnet/cb1476234967717a4d6d)
    into /usr/local/bin folder as stockinfo
-   chmod +x /usr/local/bin/stockinfo
-   Run [stockinfo]{.title-ref} as command from anywhere in your
    terminal
-   I create alias command with different stock list and get info
    whenever I want

``` bash
wget --no-check-certificate https://gist.github.com/arulrajnet/cb1476234967717a4d6d/raw/GetStockInfo.py
chmod +x GetStockInfo.py
sudo cp GetStockInfo.py /usr/local/bin/stockinfo
```

To get given stock current and history information

``` bash
stockinfo -s NASDAQ:AAPL,NASDAQ:GOOG,NASDAQ:MSFT,INDEXBOM:SENSEX -i 7d,1m,1y
```

Instead of you can use

``` bash
python GetStockInfo.py -s NASDAQ:AAPL,NASDAQ:GOOG,NASDAQ:MSFT,INDEXBOM:SENSEX -i 7d,1m,1y
```

[![Stock Info with Stock and Interval
Selection](https://cloud.githubusercontent.com/assets/834529/9387826/f2011440-477f-11e5-94b3-dacf7fd595db.png)](https://cloud.githubusercontent.com/assets/834529/9387826/f2011440-477f-11e5-94b3-dacf7fd595db.png)

To get given stock current information

``` bash
stockinfo -s NASDAQ:AAPL,NASDAQ:GOOG,NASDAQ:MSFT,INDEXBOM:SENSEX
```

[![Stock Info with Stock Selection
only](https://cloud.githubusercontent.com/assets/834529/9387855/16dc856a-4780-11e5-9c28-1af6d3511fb0.png)](https://cloud.githubusercontent.com/assets/834529/9387855/16dc856a-4780-11e5-9c28-1af6d3511fb0.png)

To get default stock current information

``` bash
stockinfo
```

[![Stock Info with default
stock](https://cloud.githubusercontent.com/assets/834529/9387927/6be8b38a-4780-11e5-9e94-b5189264c9d6.png)](https://cloud.githubusercontent.com/assets/834529/9387927/6be8b38a-4780-11e5-9e94-b5189264c9d6.png)

To get default stock current and history information

``` bash
stockinfo -i 7d,1m
```

[![stock info with interval selection
only](https://cloud.githubusercontent.com/assets/834529/9387975/b09f5254-4780-11e5-853c-efc6ed2f0bd6.png)](https://cloud.githubusercontent.com/assets/834529/9387975/b09f5254-4780-11e5-853c-efc6ed2f0bd6.png)

## License

Free to copy paste. Back-link to this post if you are good coder :wink:
