blog.arulraj.net
================

###Setup Environmental

Clone the blog from bitbucket

```
git clone bitbucket.org:arulrajnet/blog.arulraj.net.git --recursive
cd blog.arulraj.net
git submodule update --init --recursive
git fetch --recurse-submodules
git pull --recurse-submodules
```

__Install Dependencies__

```
sudo apt-get install python-pip
sudo pip install -U pelican fabric s3cmd Pygments requests BeautifulSoup4 
```

__Build__

```
fab help
fab build
fab serve
fab s3_upload
```
