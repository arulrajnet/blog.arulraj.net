blog.arulraj.net
================

### Setup

**Requirements**

Install python3 depends on your OS

    sudo apt-get install python3-pip python3-dev

Install pipenv module

    sudo pip3 install -U virtualenv
    python3 -m pip install --user pipenv

### Clone and install theme

Clone the blog

    git clone https://github.com/arulrajnet/blog.arulraj.net
    cd blog.arulraj.net
    git submodule update --init --recursive
    git fetch --recurse-submodules
    git pull --recurse-submodules

Install the following module for pelican inside `blog.arulraj.net` folder

    python3 -m pipenv shell
    python3 -m pipenv install

**Install attila theme**

    git clone --depth=1 https://github.com/arulrajnet/attila
    pelican-themes -i ${PWD}/attila
    pelican-themes -l

### Build

invoke commands

    invoke --list
    invoke build
    invoke serve

OR make commands

    make help
    make html
    make serve

Then visit [http://localhost:8000](http://localhost:8000)

**To publish to S3**

    make publish
    make s3_upload
