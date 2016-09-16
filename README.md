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

Add new submodule

```
git submodule add --force https://github.com/kura/ghastly my-pelican-themes/ghostly
```

__Install Dependencies__

```
sudo apt-get install python-pip
sudo pip install -U pelican fabric s3cmd pysvg Pygments requests webassets pillow jsmin cssmin BeautifulSoup4 
```

__Build__

```
fab help
fab build
fab serve
fab s3_upload
```

To build with specific theme

```
pelican -s pelicanconf.py -t my-pelican-themes/pelican-clean-blog-theme/
```
