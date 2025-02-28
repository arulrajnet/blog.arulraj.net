blog.arulraj.net
================

### Setup

**Requirements**

Install python3 depends on your OS

    sudo apt-get install python3-pip python3-dev

Install poetry module

    sudo pip3 install -U virtualenv
    python3 -m pip install --user poetry

### Clone and install theme

Clone the blog

    git clone https://github.com/arulrajnet/blog.arulraj.net

Install the following module for pelican inside `blog.arulraj.net` folder

    python3 -m poetry install
    python3 -m poetry shell
    pip install awscli==1.33.44
    pip install docutils==0.21.2

**Install attila theme**

    pip install git+https://github.com/arulrajnet/attila.git@master

OR

    git clone --depth=1 https://github.com/arulrajnet/attila
    pelican-themes -i ${PWD}/attila
    pelican-themes -l

Install using pip is recommended

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


### Build using Devcontainer

Install and build devcontainer. This will be one time activity

```bash
npm install -g @devcontainers/cli
devcontainer build --workspace-folder ${PWD}
devcontainer up --id-label devcontainer_for=blog.arulraj.net --workspace-folder ${PWD}
```

Then exec to run the command.

In this case, I want to generate html using devcontainer

```bash
devcontainer exec --id-label devcontainer_for=blog.arulraj.net --workspace-folder ${PWD} make html
```

To upload

```bash
devcontainer exec --id-label devcontainer_for=blog.arulraj.net --workspace-folder ${PWD} make s3_upload
```
